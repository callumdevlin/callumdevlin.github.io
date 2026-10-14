#!/usr/bin/env python3
"""Standalone checks for the maths and worked examples on the Rocket League notes.

Standard library only:   python -I rlbot_maths_tests.py

The code here is ILLUSTRATIVE: it is the maths from the site pages written out so it can be run.
It is not the bot's code. Constants are community-measured values (see research/rlbot-research.md);
game units are uu (1 uu = 1 cm) and uu/s, not SI.
"""
from __future__ import annotations

import math
import unittest

# ---- constants (community-measured) -------------------------------------------------------------
G = -650.0                  # gravity, uu/s^2 along +z (signed)
MAX_SPEED = 2300.0          # uu/s
BRAKE = 3500.0              # uu/s^2
COAST = 525.0               # uu/s^2
BOOST_GROUND = 991.667      # uu/s^2, added to throttle acceleration while boosting on the ground
BOOST_AIR = 1058.33         # uu/s^2 (RocketSim 3175/3; RLUtilities uses 1060)
BALL_RADIUS = 92.75         # uu (older wiki / RLBot template; current wiki/RocketSim use 91.25)

# speed (uu/s) -> maximum turning curvature (1/uu): RLUtilities Drive::max_turning_curvature
CURVATURE = [(0, 0.00690), (500, 0.00398), (1000, 0.00235), (1500, 0.00138), (1750, 0.00110), (2300, 0.00088)]


# ---- vectors ------------------------------------------------------------------------------------
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def mul(a, k): return tuple(x * k for x in a)
def norm(a): return math.sqrt(dot(a, a))


def ang_to_template(a, b):
    """The unsigned angle exactly as the RLBot Python template writes it. Fragile: see the tests."""
    return math.acos(dot(a, b) / (norm(a) * norm(b)))


def angle_between(a, b):
    """Unsigned angle in [0, pi]. Guards zero vectors and clamps the cosine."""
    na, nb = norm(a), norm(b)
    if na == 0.0 or nb == 0.0:
        return 0.0
    return math.acos(max(-1.0, min(1.0, dot(a, b) / (na * nb))))


def wrap_pi(angle):
    """Wrap any angle to [-pi, pi)."""
    return (angle + math.pi) % math.tau - math.pi


def steering_angle(rel_forward, rel_right):
    """Signed angle to a target given in the car's own frame: > 0 means the target is to the right
    (the world is left-handed; yaw 0 faces +x and 'right' is +y)."""
    return math.atan2(rel_right, rel_forward)


def signed_angle_flat(a, b):
    """Signed angle from direction a to direction b in the ground plane: positive when b is to the RIGHT of a
    in the game's left-handed frame."""
    return math.atan2(a[0] * b[1] - a[1] * b[0], a[0] * b[0] + a[1] * b[1])


def to_local(car_pos, yaw, target):
    """World -> car frame on the ground plane. Returns (forward, right)."""
    dx, dy = target[0] - car_pos[0], target[1] - car_pos[1]
    fx, fy = math.cos(yaw), math.sin(yaw)          # forward
    rx, ry = -math.sin(yaw), math.cos(yaw)          # right (for a car on the ground, no pitch/roll)
    return dx * fx + dy * fy, dx * rx + dy * ry


def orientation_axes(yaw, pitch, roll):
    """forward, right, up exactly as the RLBot Python template builds them from Euler angles."""
    cr, sr = math.cos(roll), math.sin(roll)
    cp, sp = math.cos(pitch), math.sin(pitch)
    cy, sy = math.cos(yaw), math.sin(yaw)
    f = (cp * cy, cp * sy, sp)
    r = (cy * sp * sr - cr * sy, sy * sp * sr + cr * cy, -cp * sr)
    u = (-cr * cy * sp - sr * sy, -cr * sy * sp + sr * cy, cp * cr)
    return f, r, u


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


# ---- ground motion ------------------------------------------------------------------------------
def throttle_accel(v):
    v = abs(v)
    if v <= 1400.0:
        return 1600.0 + (160.0 - 1600.0) * v / 1400.0
    if v <= 1410.0:
        return 160.0 * (1410.0 - v) / 10.0
    return 0.0


def accel(v, boost):
    a = throttle_accel(v)
    if boost and v < MAX_SPEED:
        a += BOOST_GROUND
    return a


def time_to_distance(dist, boost, v0=0.0, dt=1e-4):
    """Straight-line time to cover `dist` from speed v0 on full throttle (optionally boosting).
    Simple Euler integration; returns (time, speed on arrival)."""
    t = x = 0.0
    v = v0
    while x < dist:
        v = min(MAX_SPEED, v + accel(v, boost) * dt)
        x += v * dt
        t += dt
    return t, v


def radius_at(speed):
    pts = CURVATURE
    if speed <= pts[0][0]:
        k = pts[0][1]
    elif speed >= pts[-1][0]:
        k = pts[-1][1]
    else:
        for (s0, k0), (s1, k1) in zip(pts, pts[1:]):
            if s0 <= speed <= s1:
                k = k0 + (k1 - k0) * (speed - s0) / (s1 - s0)
                break
    return 1.0 / k


def arc_then_line(x, y, r):
    """Path to a target at (x forward, y right) in the car frame: turn right on a circle of radius r
    until pointing at the target, then go straight. Returns (arc_angle, tangent_length) or None if
    the target lies inside the turning circle (needs a slower speed)."""
    if y < 0:
        y = -y                                         # mirror a left-hand target
    cx, cy = 0.0, r                                    # centre of the right-hand turning circle
    d = math.hypot(x - cx, y - cy)
    if d < r:
        return None
    alpha = math.atan2(y - cy, x - cx)
    beta = math.acos(r / d)
    phi_p = alpha - beta                               # tangent point angle about the centre
    phi_s = -math.pi / 2                               # start point angle about the centre
    arc = (phi_p - phi_s) % math.tau
    return arc, math.sqrt(d * d - r * r)


def curvature_at(speed):
    return 1.0 / radius_at(speed)


def pursue(target, speed, gain=5.0, dt=1 / 120, tmax=12.0, reach=100.0):
    """Kinematic model of the bot's proportional steering: the car moves at constant `speed`, steers with
    clamp(gain * signed angle to the target) and turns at speed * curvature_limit(speed) * steer.
    Returns (time reached or None, closest approach in uu)."""
    x = y = yaw = 0.0
    t = 0.0
    closest = math.hypot(target[0], target[1])
    kappa = curvature_at(speed)
    while t < tmax:
        f, r = to_local((x, y), yaw, target)
        ang = math.atan2(r, f)
        steer = max(-1.0, min(1.0, gain * ang))
        yaw += speed * kappa * steer * dt                 # positive steer turns right: yaw increases
        x += speed * math.cos(yaw) * dt
        y += speed * math.sin(yaw) * dt
        t += dt
        d = math.hypot(target[0] - x, target[1] - y)
        closest = min(closest, d)
        if d < reach:
            return t, closest
    return None, closest


def max_speed_for_target(x_fwd, y_right):
    """Highest speed at which an arc-then-line path to the target exists (the target is outside the
    minimum turning circle). The circle tangent to the heading through the target has radius
    (x^2 + y^2) / (2|y|); the path exists while the car's minimum radius is no larger than that."""
    if y_right == 0.0:
        return MAX_SPEED
    lim = (x_fwd ** 2 + y_right ** 2) / (2.0 * abs(y_right))
    lo, hi = 0.0, MAX_SPEED
    if radius_at(MAX_SPEED) <= lim:
        return MAX_SPEED
    for _ in range(60):
        mid = (lo + hi) / 2
        if radius_at(mid) <= lim:
            lo = mid
        else:
            hi = mid
    return lo


def brake_time(v_from, v_to):
    """Time and distance to slow from v_from to v_to at the braking deceleration."""
    if v_to >= v_from:
        return 0.0, 0.0
    t = (v_from - v_to) / BRAKE
    return t, (v_from ** 2 - v_to ** 2) / (2 * BRAKE)


def eta(x_fwd, y_right, v0, boost=True, step=25.0):
    """Illustrative estimate of the time to reach a target at (ahead, right), arriving as soon as possible:
    brake (if needed) to an arc speed v, turn at the minimum radius for v, then accelerate in a straight line.
    Tries a grid of arc speeds and keeps the quickest. Returns (time, best arc speed) or (None, None)."""
    best = (None, None)
    v = min(v0, MAX_SPEED)
    while v > 0:
        r = radius_at(v)
        path = arc_then_line(x_fwd, y_right, r)
        if path is not None:
            arc, tan = path
            tb, db = brake_time(v0, v)
            t_arc = r * arc / v
            t_line, _ = time_to_distance(tan, boost, v0=v)
            total = tb + t_arc + t_line
            if best[0] is None or total < best[0]:
                best = (total, v)
        v -= step
    return best


def behind_the_ball(car_y, ball_y, team):
    """True when the car is between the ball and its OWN goal, in y. Team 0 (blue) defends -y, team 1 defends +y."""
    team_sign = 1.0 if team == 0 else -1.0
    return (car_y - ball_y) * team_sign < 0


# ---- aerial -------------------------------------------------------------------------------------
def phase(x, v, dur, boost, dt=1e-4):
    n = max(1, int(round(dur / dt)))
    h = dur / n
    a = add(boost, (0.0, 0.0, G))
    for _ in range(n):
        x = add(add(x, mul(v, h)), mul(a, 0.5 * h * h))
        v = add(v, mul(a, h))
    return x, v


def fly(x0, v0, T, t_b, A):
    """Coast (gravity only) until t_b, then constant boost acceleration A until T."""
    x, v = (phase(x0, v0, t_b, (0.0, 0.0, 0.0)) if t_b > 0 else (x0, v0))
    return phase(x, v, T - t_b, A)


def aerial_A(P, x0, v0, T, t_b=0.0):
    """Boost acceleration vector needed to be at P at time T. A = 2/(T-t_b)^2 (P - x0 - v0 T - 1/2 g T^2 z)."""
    need = sub(sub(sub(P, x0), mul(v0, T)), (0.0, 0.0, 0.5 * G * T * T))
    return mul(need, 2.0 / (T - t_b) ** 2)


def aerial_A_as_first_printed(P, x0, v0, T, dt):
    """The formula as the page first printed it (elapsed time in the numerator). WRONG; kept for the test."""
    need = sub(sub(sub(P, x0), mul(v0, dt)), (0.0, 0.0, 0.5 * G * dt * dt))
    return mul(need, 2.0 / (T - dt) ** 2)


# ---- tests --------------------------------------------------------------------------------------
class VectorTests(unittest.TestCase):
    def test_template_ang_to_fails_on_zero_vector(self):
        with self.assertRaises(ZeroDivisionError):
            ang_to_template((0, 0, 0), (1, 0, 0))

    def test_template_ang_to_domain_error_when_parallel(self):
        # exact multiples whose cosine rounds to 1.0000000000000002
        a = (1.0, 1.0, 1.0)
        with self.assertRaises(ValueError):
            ang_to_template(a, a)

    def test_template_ang_to_fails_often_for_parallel_vectors(self):
        import random
        rng = random.Random(1)
        fails = 0
        n = 20000
        for _ in range(n):
            a = tuple(rng.uniform(-3000, 3000) for _ in range(3))
            b = mul(a, rng.uniform(0.1, 9.0))
            try:
                ang_to_template(a, b)
            except ValueError:
                fails += 1
        self.assertGreater(fails / n, 0.05)        # a large share of exactly-parallel pairs raise

    def test_clamped_version_is_safe(self):
        a = (1.0, 1.0, 1.0)
        self.assertEqual(angle_between(a, a), 0.0)
        self.assertAlmostEqual(angle_between(a, mul(a, -1)), math.pi)
        self.assertEqual(angle_between((0, 0, 0), a), 0.0)

    def test_unsigned_angle_cannot_tell_left_from_right(self):
        self.assertAlmostEqual(angle_between((1, 0, 0), (1, 1, 0)), angle_between((1, 0, 0), (1, -1, 0)))

    def test_signed_steering_angle(self):
        self.assertGreater(steering_angle(100, 100), 0)        # target ahead-right
        self.assertLess(steering_angle(100, -100), 0)          # target ahead-left
        self.assertAlmostEqual(steering_angle(100, 100), math.pi / 4)

    def test_signed_flat_angle_matches_the_local_frame(self):
        import random
        rng = random.Random(5)
        for _ in range(500):
            yaw = rng.uniform(-math.pi, math.pi)
            target = (rng.uniform(-4000, 4000), rng.uniform(-5000, 5000))
            fwd = (math.cos(yaw), math.sin(yaw))
            f, r = to_local((0.0, 0.0), yaw, target)
            self.assertAlmostEqual(signed_angle_flat(fwd, target), math.atan2(r, f), places=9)
        self.assertGreater(signed_angle_flat((1, 0), (0, 1)), 0)           # +y is to the right when facing +x
        self.assertLess(signed_angle_flat((1, 0), (0, -1)), 0)

    def test_wrap_pi(self):
        self.assertAlmostEqual(wrap_pi(math.radians(190)), math.radians(-170))
        self.assertAlmostEqual(wrap_pi(math.radians(-190)), math.radians(170))
        # the classic wrap error: 170 deg minus -170 deg is 340 deg raw, but only 20 deg apart
        self.assertAlmostEqual(math.degrees(wrap_pi(math.radians(170 - (-170)))), -20.0)

    def test_world_to_local(self):
        # car at the origin facing +y (yaw 90 deg). With the template's orientation maths, 'right' is
        # then -x: a target at world (0, 1000) is dead ahead, (-1000, 0) is to the right, (1000, 0) to the left
        f, r = to_local((0, 0), math.pi / 2, (0, 1000))
        self.assertAlmostEqual(f, 1000.0); self.assertAlmostEqual(r, 0.0, places=6)
        f, r = to_local((0, 0), math.pi / 2, (-1000, 0))
        self.assertAlmostEqual(f, 0.0, places=6); self.assertAlmostEqual(r, 1000.0)
        f, r = to_local((0, 0), math.pi / 2, (1000, 0))
        self.assertAlmostEqual(r, -1000.0)
        # facing +x (yaw 0): right is +y
        f, r = to_local((0, 0), 0.0, (0, 1000))
        self.assertAlmostEqual(r, 1000.0)


class FrameTests(unittest.TestCase):
    def test_orientation_axes_are_orthonormal_and_the_world_is_left_handed(self):
        import random
        rng = random.Random(3)
        for _ in range(2000):
            yaw = rng.uniform(-math.pi, math.pi)
            pitch = rng.uniform(-math.pi / 2, math.pi / 2)
            roll = rng.uniform(-math.pi, math.pi)
            f, r, u = orientation_axes(yaw, pitch, roll)
            for v in (f, r, u):
                self.assertAlmostEqual(norm(v), 1.0, places=9)
            self.assertAlmostEqual(dot(f, r), 0.0, places=9)
            self.assertAlmostEqual(dot(f, u), 0.0, places=9)
            self.assertAlmostEqual(dot(r, u), 0.0, places=9)
            # (forward x right) . up = +1: for a real car forward x right points down, so the coordinates are mirrored
            self.assertAlmostEqual(dot(cross(f, r), u), 1.0, places=9)

    def test_yaw_zero_faces_plus_x_and_right_is_plus_y(self):
        f, r, u = orientation_axes(0.0, 0.0, 0.0)
        self.assertAlmostEqual(f[0], 1.0); self.assertAlmostEqual(r[1], 1.0); self.assertAlmostEqual(u[2], 1.0)
        f, r, u = orientation_axes(math.pi / 2, 0.0, 0.0)
        self.assertAlmostEqual(f[1], 1.0); self.assertAlmostEqual(r[0], -1.0)


class GroundTests(unittest.TestCase):
    def test_throttle_acceleration_curve(self):
        self.assertAlmostEqual(throttle_accel(0), 1600.0)
        self.assertAlmostEqual(throttle_accel(1400), 160.0)
        self.assertAlmostEqual(throttle_accel(1410), 0.0)
        self.assertAlmostEqual(throttle_accel(2000), 0.0)

    def test_boost_adds_to_throttle(self):
        self.assertAlmostEqual(accel(0, True), 1600.0 + BOOST_GROUND)       # 2591.667
        self.assertAlmostEqual(accel(0, True), 2591.667, places=3)

    def test_straight_line_times(self):
        t, v = time_to_distance(1000, boost=False)
        self.assertAlmostEqual(t, 1.380, delta=0.01); self.assertAlmostEqual(v, 1179, delta=15)
        t, v = time_to_distance(1000, boost=True)
        self.assertAlmostEqual(t, 1.034, delta=0.01); self.assertAlmostEqual(v, 1645, delta=15)
        t, _ = time_to_distance(4000, boost=False)
        self.assertAlmostEqual(t, 3.571, delta=0.02)

    def test_step_size_barely_matters(self):
        fine, _ = time_to_distance(2000, boost=True, dt=1e-4)
        coarse, _ = time_to_distance(2000, boost=True, dt=1 / 60)
        self.assertLess(abs(fine - coarse), 0.02)                            # within about one tick at 60 Hz

    def test_turning_radius_table(self):
        self.assertAlmostEqual(radius_at(0), 144.9, delta=0.1)
        self.assertAlmostEqual(radius_at(2300), 1136.4, delta=0.1)
        self.assertAlmostEqual(radius_at(2300) / 100.0, 11.36, delta=0.01)    # metres: 1 uu = 1 cm
        self.assertLess(radius_at(2300) / 100000.0, 0.012)                    # nowhere near a kilometre
        self.assertGreater(radius_at(1250), radius_at(1000))                  # radius grows with speed


class BehaviourTests(unittest.TestCase):
    def test_which_side_is_defence_depends_on_the_team(self):
        self.assertTrue(behind_the_ball(-2000.0, 0.0, team=0))      # blue defends -y: car at -2000 is behind the ball
        self.assertFalse(behind_the_ball(-2000.0, 0.0, team=1))
        self.assertTrue(behind_the_ball(2000.0, 0.0, team=1))       # orange defends +y
        self.assertFalse(behind_the_ball(2000.0, 0.0, team=0))
        # the snapshot's defence check is `is_closer_to_goal_than(car, ball, 1)`, i.e. car.y > ball.y: it treats the
        # +y goal as 'my goal' for every car, which is right for orange (team 1) only
        hard_coded = lambda car_y, ball_y: car_y > ball_y
        for car_y, ball_y in ((-2000.0, 0.0), (2000.0, 0.0)):
            self.assertEqual(hard_coded(car_y, ball_y), behind_the_ball(car_y, ball_y, 1))
            self.assertNotEqual(hard_coded(car_y, ball_y), behind_the_ball(car_y, ball_y, 0))


class SteeringTests(unittest.TestCase):
    def test_gain_saturates_beyond_a_small_angle(self):
        self.assertAlmostEqual(math.degrees(1.0 / 5.0), 11.46, places=2)

    def test_slow_car_reaches_a_close_target_and_fast_car_orbits_it(self):
        target = (0.0, 500.0)                                   # 500 uu to the right, car facing +x
        t_slow, _ = pursue(target, 300.0)
        t_mid, _ = pursue(target, 500.0)
        t_fast, closest_fast = pursue(target, 1400.0)
        self.assertIsNotNone(t_slow); self.assertIsNotNone(t_mid)
        self.assertIsNone(t_fast)                               # never gets within 100 uu in 12 s
        self.assertGreater(closest_fast, 300.0)

    def test_max_speed_for_target(self):
        self.assertAlmostEqual(max_speed_for_target(600, 800), 1387, delta=5)
        self.assertAlmostEqual(max_speed_for_target(0, 500), 497, delta=5)
        self.assertEqual(max_speed_for_target(2000, 0), MAX_SPEED)
        # at or below that speed the car gets there; well above it, it does not
        t_ok, _ = pursue((0.0, 500.0), 450.0)
        self.assertIsNotNone(t_ok)

    def test_braking_distance(self):
        d = (1400.0 ** 2 - 497.0 ** 2) / (2 * BRAKE)
        self.assertAlmostEqual(d, 244.7, delta=0.5)


class EtaTests(unittest.TestCase):
    def test_eta_is_never_better_than_the_straight_line(self):
        t, v = eta(600, 800, 1400.0)
        straight, _ = time_to_distance(1000.0, True, v0=1400.0)
        self.assertIsNotNone(t)
        self.assertGreater(t, straight)
        self.assertLessEqual(v, 1387 + 1)                     # must slow to a speed at which the target is reachable

    def test_a_slower_start_needs_no_braking(self):
        t_slow, v_slow = eta(600, 800, 800.0)
        self.assertIsNotNone(t_slow)
        self.assertAlmostEqual(v_slow, 800.0, delta=25.0)     # keeping speed is best when it is already feasible


class PathTests(unittest.TestCase):
    def test_target_inside_circle_is_unreachable(self):
        self.assertIsNone(arc_then_line(100, 100, 500))
        self.assertIsNone(arc_then_line(0, 200, 500))

    def test_arc_line_reaches_the_target(self):
        for (x, y, r) in [(2000, 1000, 500), (3000, 300, 700), (500, 1500, 250), (1500, -900, 400)]:
            arc, tan = arc_then_line(x, y, r)
            yy = abs(y)
            # walk the arc, then the tangent, and see where we land
            cx, cy = 0.0, r
            phi = -math.pi / 2 + arc
            px, py = cx + r * math.cos(phi), cy + r * math.sin(phi)
            heading = phi + math.pi / 2                                       # counter-clockwise travel
            ex, ey = px + tan * math.cos(heading), py + tan * math.sin(heading)
            self.assertAlmostEqual(ex, x, delta=1e-6)
            self.assertAlmostEqual(ey, yy, delta=1e-6)
            self.assertGreater(arc, 0.0)

    def test_worked_example(self):
        # target 600 forward and 800 to the right, minimum-radius circle of 400 uu
        arc, tan = arc_then_line(600, 800, 400)
        self.assertAlmostEqual(math.degrees(arc), 67.4, delta=0.1)
        self.assertAlmostEqual(tan, 600.0, delta=0.1)
        self.assertAlmostEqual(400 * arc + tan, 1070.4, delta=0.2)
        self.assertAlmostEqual(math.hypot(600, 800), 1000.0)               # the straight-line 'lie'

    def test_a_close_target_is_unreachable_above_a_speed(self):
        # the circle through the origin tangent to the heading and through (600, 800) has radius
        # (x^2 + y^2) / (2y) = 625 uu; the arc-then-line path exists only while r(v) <= that
        self.assertAlmostEqual((600 ** 2 + 800 ** 2) / (2 * 800), 625.0)
        lo, hi = 0.0, 2300.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if arc_then_line(600, 800, radius_at(mid)) is None:
                hi = mid
            else:
                lo = mid
        self.assertAlmostEqual(lo, 1387, delta=5)


class AerialTests(unittest.TestCase):
    CASES = [((-1200.0, 600.0, 300.0), (900.0, -150.0, 250.0), (1100.0, 400.0, 900.0), 2.0)]

    def test_corrected_formula_hits_the_target(self):
        for x0, v0, P, T in self.CASES:
            for t_b in (0.0, 0.3, 0.6):
                A = aerial_A(P, x0, v0, T, t_b)
                miss = norm(sub(fly(x0, v0, T, t_b, A)[0], P))
                self.assertLess(miss, 1e-3)

    def test_first_printed_formula_misses_badly(self):
        for x0, v0, P, T in self.CASES:
            for t_b in (0.0, 0.3, 0.6):
                A = aerial_A_as_first_printed(P, x0, v0, T, t_b)
                miss = norm(sub(fly(x0, v0, T, t_b, A)[0], P))
                self.assertGreater(miss, 100.0)

    def test_resolving_with_the_current_state_gives_the_same_answer(self):
        x0, v0, P, T = self.CASES[0]
        dt_e = 0.7
        x1, v1 = phase(x0, v0, dt_e, (0.0, 0.0, 0.0))
        tau = T - dt_e
        A2 = mul(sub(sub(sub(P, x1), mul(v1, tau)), (0.0, 0.0, 0.5 * G * tau * tau)), 2.0 / tau ** 2)
        self.assertLess(norm(sub(A2, aerial_A(P, x0, v0, T, dt_e))), 1e-6)
        self.assertLess(norm(sub(phase(x1, v1, tau, A2)[0], P)), 1e-3)

    def test_worked_example_numbers(self):
        x0, v0, P, T, t_b = (0.0, 0.0, 300.0), (800.0, 0.0, 300.0), (1800.0, 0.0, 700.0), 2.0, 0.4
        A = aerial_A(P, x0, v0, T, t_b)
        self.assertAlmostEqual(A[0], 156.25, places=2)
        self.assertAlmostEqual(A[2], 859.375, places=2)
        self.assertAlmostEqual(norm(A), 873.5, delta=0.1)
        self.assertLess(norm(A) / BOOST_AIR, 0.9)                              # feasible with margin
        self.assertLess(norm(sub(fly(x0, v0, T, t_b, A)[0], P)), 1e-3)

    def test_infeasible_when_boost_demand_exceeds_the_limit(self):
        x0, v0, P, T = self.CASES[0]
        self.assertGreater(norm(aerial_A(P, x0, v0, T, 0.6)), BOOST_AIR)


class AlignmentTests(unittest.TestCase):
    def test_offset_point_lies_behind_the_ball_on_the_goal_line(self):
        ball = (1000.0, 2000.0)
        goal = (0.0, 5120.0)
        d = sub(goal, ball)
        n = norm(d)
        u = mul(d, 1.0 / n)
        standoff = 100.0
        p = sub(ball, mul(u, BALL_RADIUS + standoff))
        # behind the ball: moving from p towards the goal passes through the ball
        to_ball = sub(ball, p)
        self.assertAlmostEqual(norm(to_ball), BALL_RADIUS + standoff, places=9)
        self.assertGreater(dot(to_ball, u), 0.0)
        self.assertAlmostEqual(abs(dot(to_ball, u)) / norm(to_ball), 1.0, places=9)

    def test_heading_error_at_the_offset_point(self):
        r_plus_s = BALL_RADIUS + 100.0                                          # 192.75
        for deg, expect in ((10, 33.5), (30, 96.4)):
            miss = r_plus_s * math.sin(math.radians(deg))                       # sideways miss of the ball centre
            self.assertAlmostEqual(miss, expect, delta=0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
