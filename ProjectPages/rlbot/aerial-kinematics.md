---
title: RL Bot, Aerial Kinematics
crumb: Aerial kinematics
permalink: /ProjectPages/rlbot/aerial-kinematics/
type: maths
section: rlbot
nav_order: 8
status: wip
applies: Standard car physics with community-measured constants. This is maths and a design sketch; there is no aerial code in the public bot.
reviewed: 2026-10-14
description: >
  Solving for the orientation and boost a Rocket League car needs to reach a target
  point in the air at a given time.
---

For the bot to hit an aerial it has to juggle a lot at once: ball height, ball speed, car speed, distance, angle and remaining boost. The idea is simple: point the car at the right place and boost. Getting it robust is fiddly. These notes set out the underlying kinematics, and the public bot doesn't contain an aerial yet.

An earlier version of this page had the main formula wrong: the elapsed time and the arrival time were swapped, which puts the wrong time in the numerator. The corrected version below has been checked against a numerical simulation. The derivation follows Sam Mish's [aerial hit write-up](https://smish.dev/rocket_league/aerial_hit).
{:.note}

Define the quantities of interest:

- $$c(t)$$ is the car's position
- $$f(t)$$ is the unit vector the car is facing
- $$B(t)$$ is the acceleration due to boost
- $$P$$ is the target location

All positions and directions are world vectors (x, y, z). Gravity is written as a signed value, $$g = -650\ \mathrm{uu/s^2}$$, acting along $$\hat{z}$$, so downward is negative.
{:.note}

While airborne, the only accelerations available are boost (along the facing direction) and gravity, so the car obeys

$$
\ddot{c}(t) = B(t)\, f(t) + g\,\hat{z}, \qquad c(0) = x_0,\quad \dot{c}(0) = v_0
$$

There is also a small air-throttle acceleration (66.7 uu/s² forward) and the extra push from holding jump for the first 0.2 s. I've left both out, so take $$x_0$$ and $$v_0$$ as the state just after take-off.
{:.note}

## The required boost

Suppose we want to be at $$P$$ at time $$T$$, and the car coasts (no boost) until time $$t_b$$ while it turns to face the right way. After that it boosts at a constant acceleration vector $$A$$ until $$T$$. With no boost at all, the car would end up at $$x_0 + v_0 T + \tfrac{1}{2} g T^2 \hat{z}$$. Boosting for the last $$T - t_b$$ seconds adds $$\tfrac{1}{2} A\,(T - t_b)^2$$ to that. Setting the sum equal to $$P$$ and solving for $$A$$:

$$
A \;=\; \frac{2}{(T - t_b)^2}\left(P - x_0 - v_0\,T - \tfrac{1}{2}\, g\, T^2\, \hat{z}\right)
$$

$$A$$ has units of acceleration, so it can be read as *the acceleration needed to be at $$P$$ at time $$T$$*, after accounting for where the car is, where its velocity is carrying it and what gravity will do. It splits into a magnitude and a direction:

$$
B_0 = \lVert A \rVert, \qquad f^* = \frac{A}{\lVert A \rVert}
$$

Because the ball keeps moving, the bot doesn't solve this once. It **re-solves every tick** with the car's *current* position and velocity as $$x_1$$ and $$v_1$$, and with $$\tau = T - t$$ as the time remaining. Then $$t_b$$ is "now", and the formula becomes

$$
A = \frac{2}{\tau^{2}}\left(P - x_1 - v_1\,\tau - \tfrac{1}{2}\, g\, \tau^2\, \hat{z}\right)
$$

I checked numerically that re-solving mid-flight from the current state gives the same answer as solving at the start.

## A worked example

A car at (0, 0, 300) moving at (800, 0, 300) uu/s wants to be at (1800, 0, 700) in $$T = 2$$ s, after 0.4 s spent turning to face the right way ($$t_b = 0.4$$).

- With no boost at all, the car would be at x = 1,600 and z = 300 + 600 − 1,300 = −400. It falls short by (200, 0, 1,100).
- $$A = \dfrac{2}{1.6^2} \times (200, 0, 1100) = (156.25,\ 0,\ 859.4)$$, so $$B_0 = 873.5$$ uu/s².
- The direction to face is about 79.7° above the horizontal, and the boost has to run for 1.6 s.

I ran that boost through a step-by-step simulation, and the car ends up at the target to within a thousandth of a uu. The formula as first printed here gives (1156, 0, 259) with a magnitude of 1,185, which is more than the car can produce, and it would have the car land about 1,490 uu from the target.

## Is it feasible?

Two practical checks fall straight out of the maths before committing to an aerial at all.

**Can the car produce the acceleration?** Boost in the air gives about 1,058 uu/s² (RocketSim's value; RLUtilities uses 1,060). If $$B_0$$ exceeds that, the target is unreachable in the time available, so don't jump. In the example, 873.5 is 83% of the limit. An open-source implementation (RLUtilities) wants a margin and calls an aerial viable only if the demand is under 90% of the maximum.

**Is there enough boost?** Boost drains at 33.33 per second, so 1.6 s of continuous boost costs about 53 units of the 100-unit tank.

**Can the car face the right way in time?** If $$f^*$$ points somewhere the car can't rotate to quickly enough, the time budget has to include the rotation or the aerial arrives late. The community-fitted pitch acceleration at full input is about 12 rad/s² (yaw about 9, roll about 36), with a maximum angular speed of 5.5 rad/s. Ignoring damping, a rough time to turn through an angle $$\Delta$$ with full acceleration to the halfway point and full braking after is $$2\sqrt{\Delta/\alpha}$$. For a 90° pitch that is about 0.7 s, so $$t_b$$ shouldn't be much smaller than that. It is a rough bound, since damping changes it, and it isn't a measurement.

## The simple version in code

Align the car with $$f^*$$ and boost while it is pointing close enough. As the ball (and so the target) moves, the bot re-aligns every tick, so the aerial is a continuous correction loop rather than a single launch calculation. Illustrative code for the planning step:

~~~python
def aerial_plan(x0, v0, target, T, t_b=0.0):
    """Boost acceleration needed (uu/s^2) and the direction to face, to be at `target` at time T."""
    g = Vec3(0, 0, -650)
    need = target - x0 - v0 * T - g * (0.5 * T * T)
    A = need * (2.0 / (T - t_b) ** 2)
    magnitude = A.length()
    return magnitude, (A / magnitude if magnitude > 0 else A)
~~~

Compare `magnitude` against the boost limit before jumping, and re-run it each tick with the current position, velocity and time remaining. I haven't tuned it against in-game behaviour.

## What this doesn't cover

The jump itself (its initial impulse and the extra acceleration while the button is held), dodges, air throttle, how fast the car can really reorient, and the ball's own bounces are left out. The ball's predicted path, from the framework's prediction, supplies $$P$$ and $$T$$.
