---
title: RL Bot, Ground Kinematics
crumb: Ground kinematics
permalink: /ProjectPages/rlbot/ground-kinematics/
type: maths
section: rlbot
nav_order: 5
status: growing
applies: Community-measured constants for the standard Rocket League car physics. The numbers describe the game, not any one bot.
reviewed: 2026-10-14
description: >
  How the Rocket League car accelerates, brakes, coasts and boosts on the ground,
  the values that govern each, and how far and how fast it gets.
---

When the car is on the ground, the bot controls it through throttle, boost and steering. To reach a target point reliably, and arrive at the right time and speed, it has to be able to answer questions like:

- How fast do I need to go to reach a point at a certain time?
- How much do I need to turn to reach that point?
- How much boost will that cost?
- How fast should I be travelling when I arrive?

Answering them means knowing how the car actually behaves, so here is how it accelerates and how its motion can be predicted.

Lengths are in Unreal Units (uu), speeds in uu/s and accelerations in uu/s², the game's native units. The values below are community measurements, mainly [Sam Mish's research](https://smish.dev/rocket_league/ground_control) and the RLUtilities source, cross-checked against the RocketSim simulator. Psyonix doesn't publish them.
{:.note}

## The constants

| Quantity | Value | Notes |
| --- | ---: | --- |
| Throttle acceleration | 1,600 uu/s² at rest, falling to 160 at 1,400 uu/s and 0 at 1,410 uu/s | Depends on speed; see below |
| Braking deceleration | 3,500 uu/s² | When the throttle opposes the direction of motion |
| Coasting deceleration | 525 uu/s² | No throttle, no boost |
| Boost acceleration (ground) | 991.667 uu/s² | Added to the throttle acceleration while boosting |
| Boost consumption | 33.33 per second | A full tank is about 3 seconds |
| Maximum speed | 2,300 uu/s (82.8 km/h) | The game's cap; throttle alone stops at 1,410 |
| Gravity | 650 uu/s² downward | |

## Acceleration

The car's acceleration from throttle depends entirely on its current speed. It is **not constant**, and it falls as the car speeds up. It is greatest at rest, falls in a straight line to 160 uu/s² at 1,400 uu/s, and then drops to zero over the last 10 uu/s, so throttle alone cannot take the car past 1,410 uu/s.

{% include figure.html src="/assets/rlbot/throttle-acceleration.svg" alt="Chart of forward acceleration against speed: a throttle-only line falling from 1,600 at rest to zero at 1,410 uu/s, and a throttle-plus-boost line about 992 higher, ending at the 2,300 uu/s speed cap" caption="Throttle acceleration, and throttle plus boost, against speed. Drawn from the community-measured values in the table above." %}

| Speed (uu/s) | 0 | 1,400 | 1,410 | 2,300 |
|:---|---:|---:|---:|---:|
| Throttle acceleration (uu/s²) | 1,600 | 160 | 0 | 0 |

### Boosting

While boosting, the throttle is treated as fully pressed and an additional 991.667 uu/s² is applied. At rest the car therefore accelerates at about 2,592 uu/s². Past 1,410 uu/s only the boost term is left, so acceleration is about 992 uu/s² until the 2,300 uu/s cap, where it stops regardless of input.

### Braking and coasting

If the car's forward velocity has the opposite sign to the throttle input, a constant deceleration of 3,500 uu/s² acts against the motion. Braking is far stronger than accelerating, which matters when deciding how late to leave it before slowing for a turn. With no throttle or boost, a gentler 525 uu/s² applies. Coasting is gentle enough that "lift off early" is rarely a substitute for braking properly.

### Gravity on slopes and walls

Gravity has a magnitude of 650 uu/s² and acts straight down. On flat ground it is cancelled by the normal force. On a wall, a ramp or in the air, the component of gravity along the direction the car faces is −650 (f̂ · ẑ) uu/s², where f̂ is the unit vector the car is facing and ẑ is up. Facing uphill, it opposes the motion. That term is what makes wall driving and [aerials](/ProjectPages/rlbot/aerial-kinematics/) interesting.

## How far, how fast

Because acceleration depends on speed, the time to cover a distance has no tidy closed form, so the practical way is to step the speed forward numerically:

~~~python
def throttle_accel(v):                       # uu/s^2, from the measured curve
    v = abs(v)
    if v <= 1400: return 1600 + (160 - 1600) * v / 1400
    if v <= 1410: return 160 * (1410 - v) / 10
    return 0.0

def time_to_distance(dist, boost, v0=0.0, dt=1/120):
    t = x = 0.0
    v = v0
    while x < dist:
        a = throttle_accel(v) + (991.667 if boost and v < 2300 else 0.0)
        v = min(2300.0, v + a * dt)
        x += v * dt
        t += dt
    return t, v                              # time taken, speed on arrival
~~~

For a straight run from rest on full throttle (from my own run of that loop, not an in-game measurement):

| Distance | Throttle only | Throttle and boost |
| ---: | --- | --- |
| 500 uu | 0.91 s, arriving at 948 uu/s | 0.70 s, arriving at 1,287 uu/s |
| 1,000 uu | 1.38 s, arriving at 1,179 uu/s | 1.03 s, arriving at 1,644 uu/s |
| 2,000 uu | 2.15 s, arriving at 1,385 uu/s | 1.56 s, arriving at 2,165 uu/s |
| 4,000 uu | 3.57 s, arriving at 1,410 uu/s | 2.43 s, arriving at 2,300 uu/s |

That makes the boost decision concrete. Over 1,000 uu, boosting saves about 0.35 s and costs about 34 of the 100 boost units (1.03 s at 33.33 per second). The saving per unit of boost is poorer over shorter runs and better over long ones, where the car would otherwise sit at its 1,410 uu/s throttle limit. Whether that's worth it depends on how much boost the bot has and what else it needs it for.

The step size isn't critical for decisions. Stepping at 1/60 s instead of a very fine step changes a 2,000 uu run by less than 0.02 s. Straight-line numbers like these are the best case; they ignore turning, which is where [the path analysis](/ProjectPages/rlbot/movingpath/) picks up.

*The code on this page is illustrative and isn't in the public bot. Credit to Sam Mish, whose research the constants come from.*
