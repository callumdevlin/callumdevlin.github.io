---
title: RL Bot, Steering and Driving
crumb: Steering
permalink: /ProjectPages/rlbot/steering/
type: maths
section: rlbot
nav_order: 4
applies: RLBot v4 Python API. `steer_toward_target` is from the RLBot template; the speed-control code is illustrative.
reviewed: 2026-10-14
description: >
  Turning an angle into a steering input, and why a simple proportional controller
  can circle a target forever unless speed is controlled too.
---

The bot's steering is about as simple as a controller gets. It converts the target into the car's own frame, takes the angle to it and multiplies by a constant. That works well enough to chase a ball at moderate speed, and it fails in an instructive way when it doesn't.

## The controller in the bot

This is the template's `steer_toward_target`, which the bot uses:

~~~python
def steer_toward_target(car, target: Vec3) -> float:
    relative = relative_location(Vec3(car.physics.location), Orientation(car.physics.rotation), target)
    angle = math.atan2(relative.y, relative.x)          # right / forward: positive = target on the right
    return limit_to_safe_range(angle * 5)               # clamp to [-1, 1]
~~~

`atan2(right, forward)` is a signed angle, so the sign of the result says which way to steer and it has none of the `acos` problems from the [vectors page](/ProjectPages/rlbot/vectors/). The gain of 5 means the output reaches full lock at an angle of 1/5 rad, which is about 11.5°. Inside that cone the steering is proportional to the error. Outside it the car steers at full lock, however large the error is.

## What a steering input does

The input is not a wheel angle. To a good approximation it sets how tightly the car turns, as a fraction of the tightest turn it can manage at its current speed. That limit shrinks as speed rises, from a radius of about 145 uu at rest to 1,136 uu at the 2,300 uu/s cap (see the [path analysis](/ProjectPages/rlbot/movingpath/#turning-radius-grows-with-speed)). The turn rate is then roughly speed × curvature limit × steering input.

## The orbit trap

Here is the failure. If the target is closer to the car than the car's turning circle allows, then full lock isn't enough to bring it round. The car goes into orbit and circles the target at a distance, because the proportional controller keeps asking for a tighter turn than the car can physically do.

I simulated this with the bot's controller (gain 5, full lock capped at the speed's curvature limit) for a target 500 uu to the right of a car facing straight ahead, counting the target as reached within 100 uu. It is a kinematic model with constant speed, so it shows the effect rather than predicting in-game behaviour.

| Constant speed | Result |
| ---: | --- |
| 300 uu/s | Reaches the target in 1.9 s |
| 500 uu/s | Reaches it in 1.4 s |
| 800 uu/s | Never gets closer than 166 uu |
| 1,000 uu/s | Never closer than 351 uu |
| 1,400 uu/s and 2,000 uu/s | Never closer than 500 uu: the car just keeps going round |

The condition is a geometric one. The tightest circle that starts tangent to the car's heading and passes through a target at (ahead x, right y) has a radius of (x² + y²) / (2y). The target is reachable by turning and then driving straight only while the car's minimum turning radius at its current speed is no larger than that. For the target above that is 250 uu, which the car manages at up to about 500 uu/s. A target 600 uu ahead and 800 uu to the right allows a radius of 625 uu, which the car manages at up to about 1,390 uu/s.

## The fix: control the speed too

Steering only works if speed is under control. The simplest approach is to compute the highest speed at which the target is reachable and slow to it before turning. This is illustrative code, using the community-measured turning table:

~~~python
def max_speed_for_target(ahead: float, right: float) -> float:
    """Highest speed (uu/s) at which an arc-then-line path to the target exists."""
    if right == 0.0:
        return MAX_SPEED
    limit = (ahead**2 + right**2) / (2.0 * abs(right))       # largest usable turning radius
    if min_turn_radius(MAX_SPEED) <= limit:
        return MAX_SPEED
    lo, hi = 0.0, MAX_SPEED
    for _ in range(40):                                       # bisection on the monotonic radius table
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if min_turn_radius(mid) <= limit else (lo, mid)
    return lo
~~~

If the car is faster than that, brake or lift off. Braking is strong: the deceleration is 3,500 uu/s² against 525 uu/s² for coasting (see [ground kinematics](/ProjectPages/rlbot/ground-kinematics/)). Slowing from 1,400 uu/s to 500 uu/s takes about 245 uu, which is about a quarter of a second, so leaving it late costs little. Coasting would take far longer.

## Edge cases

- **Target directly behind.** The angle is near ±π and its sign flips with tiny changes in position, so the steering can swing between full left and full right. Pick a side and hold it for a while rather than recomputing each tick.
- **Tight turns at low speed.** A handbrake slide can turn tighter than the steering limit, but I haven't modelled it, so these notes don't cover powersliding.
- **The target moves.** For a ball in motion the target changes every tick. The [path analysis](/ProjectPages/rlbot/movingpath/) covers aiming where the ball will be.
- **Model limits.** My simulation holds speed constant and treats steering as scaling the curvature limit. The real car also changes speed and loses speed in a tight turn, so use these numbers to understand the shape of the problem, not as in-game predictions.

*Apart from the template's `steer_toward_target`, the code on this page is illustrative.*
