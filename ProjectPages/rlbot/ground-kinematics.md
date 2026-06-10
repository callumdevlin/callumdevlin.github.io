---
title: RL Bot — Ground Kinematics
permalink: /ProjectPages/rlbot/ground-kinematics/
description: >
  How the Rocket League car accelerates, brakes, coasts and boosts on the
  ground — the values that govern each, and why they matter for a bot.
---

When the car is on the ground, the bot controls it through throttle, boost and steering. For the bot to reach a target point reliably — and arrive at the right time, at the right speed — it has to be able to answer questions like:

- How fast do I need to go to reach a point at a certain time?
- How much do I need to turn to reach that point?
- How much boost will that cost?
- How fast should I be travelling when I arrive?

Answering those requires knowing how the car actually behaves, so here is roughly how it accelerates and how its motion can be predicted.

Units throughout are $$\frac{uu}{s}$$ — Unreal Units per second, the game engine's native vector magnitudes.
{:.note}

## Acceleration

The car's acceleration from throttle is entirely dependent on its current velocity — it is **not constant**, and decreases as velocity increases. At rest the acceleration is at its greatest, then it falls roughly uniformly to zero at $$1410 \frac{uu}{s}$$:

![Velocity vs acceleration graph](/Images/v_agraph.JPG){:.lead loading="lazy"}

| Velocity | 0.0 | 1400.0 | 1410.0 | 2300.0 |
|:--------:|:---:|:------:|:------:|-------:|
| Acceleration | 1600.0 | 160.0 | 0.0 | 0.0 |

The maximum speed using throttle alone is $$1410 \frac{uu}{s}$$ — reaching the game's true cap of $$2300 \frac{uu}{s}$$ requires boost (or flips).
{:.note}

### Braking

If the car's forward velocity has the opposite sign to the input throttle, the car applies a constant deceleration of $$3500 \frac{uu}{s^2}$$ against the direction of motion. Braking is therefore much stronger than accelerating, which matters when deciding how late the bot can leave it before slowing for a turn.

### Coasting

With no throttle or boost input, a constant deceleration of $$525 \frac{uu}{s^2}$$ acts against the car, slowing it gradually to a stop. Coasting is gentle enough that "lift off early" is rarely a substitute for braking properly.

### Boosting

While boosting, the throttle is treated as maxed and an additional acceleration of $$991.667 \frac{uu}{s^2}$$ is applied. Boost is also the only way to push past the throttle-limited $$1410 \frac{uu}{s}$$ up to the hard cap of $$2300 \frac{uu}{s}$$, where acceleration is clamped to zero regardless of input.

### Gravity

Gravity is always present, with magnitude $$g = 650 \frac{uu}{s^2}$$ acting straight down (−z). On flat ground it's cancelled by the normal force, but the moment the car is on a wall, on a ramp, or airborne, the component of gravity along the car's direction of travel — $$g \,(\hat{f} \cdot \hat{z})$$, where $$\hat{f}$$ is the unit vector the car is facing — starts adding to or fighting the car's acceleration. This term is what makes wall driving and [aerials](/ProjectPages/rlbot/aerial-kinematics/) interesting.

Credit to Sam Mish, whose RLBot physics research assisted these notes.
{:.note}
