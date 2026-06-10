---
title: RL Bot — Path Optimisation Analysis
permalink: /ProjectPages/rlbot/movingpath/
description: >
  Why turning radius grows with speed, what that means for choosing paths,
  and estimating time-to-target along realistic arc-and-line routes.
---

The straight-line distance to a target is a lie. A car at speed can't pivot on the spot — it sweeps an arc — so the *real* question for the bot is: what path can the car physically follow to the target, and how long will it take? This page is my working analysis of that problem.

## Turning Radius Grows with Speed

At full steering lock, the car's minimum turning radius is a function of its speed: the faster it travels, the wider the tightest arc it can manage. At low speed the car turns almost on the spot; near the $$2300\frac{uu}{s}$$ speed cap, the minimum radius is on the order of a full kilometre of Unreal Units. There's no single formula in the game for this — the relationship comes from the game's curvature limits at different speeds and is effectively a decreasing curvature curve $$\kappa(v)$$, with radius $$r = 1/\kappa$$.

The practical consequence is a fundamental trade-off:

> **Faster is not always sooner.** A car that slows down can take a tighter line; a car at full speed may have to sweep a huge arc — or overshoot and double back.

This is exactly why the [shot alignment logic](/ProjectPages/rlbot/aligning-shots/) reduces throttle when the approach angle is poor.

## Arc–Line Paths

A simple and effective path model is **arc then line**: the car turns along a circle of its current minimum radius until its heading points at the target, then drives straight.

Construction:
1. Place two candidate turning circles of radius $$r(v)$$ either side of the car, perpendicular to its current heading.
2. Pick the circle on the same side as the target, and find the tangent line from that circle to the target point.
3. The path length is (arc swept) + (tangent length); with the car's speed profile, that converts to a time.

This is the same geometry used in Dubins paths from robotics, simplified to a single turn. It's cheap enough to evaluate every tick, and gives a far more honest time-to-target than straight-line distance ever can.

## Estimating Time-to-Target

With a path length in hand, time still depends on the speed profile along it — and from [ground kinematics](/ProjectPages/rlbot/ground-kinematics/), acceleration is itself a function of velocity. Rather than solving that analytically, the practical approach is numerical: step the velocity forward in small time increments using the throttle/boost acceleration values, accumulating distance until it matches the path length. A coarse step (say 1/60 s, one game tick) is plenty accurate for decision-making.

That estimator unlocks the questions the bot actually cares about:

- **Can I beat the opponent to the ball?** Compare time-to-target estimates.
- **Intercepting a moving ball:** for each candidate time $$t$$ along the ball's predicted trajectory, ask whether the car can reach that ball position in $$\le t$$. The earliest feasible $$t$$ is the intercept.
- **Is boost worth it here?** Run the estimate with and without the boost acceleration term and compare arrival times against boost cost.

## Status & Next Steps

This analysis is the part of the project I'm still actively iterating on. The arc–line model and the numerical time estimator work; what's in progress is tuning the curvature-vs-speed data against measured bot behaviour (using the Matplotlib logging mentioned in the [overview](/ProjectPages/rlbot/overview/)) and extending the intercept search to aerial targets, where the [aerial kinematics](/ProjectPages/rlbot/aerial-kinematics/) feasibility check replaces the ground-path estimator. I'll update this page as that lands.
