---
title: RL Bot, Path Optimisation Analysis
crumb: Path analysis
permalink: /ProjectPages/rlbot/movingpath/
type: maths
section: rlbot
nav_order: 6
status: wip
applies: Community-measured turning data for the standard car. The path and time-estimate code is illustrative.
reviewed: 2026-10-14
description: >
  Why turning radius grows with speed, what that means for choosing a path, and
  estimating time-to-target along arc-then-line routes.
---

The straight-line distance to a target is misleading. A car at speed can't pivot on the spot. It sweeps an arc, so the real question for the bot is what path the car can physically follow to the target and how long that takes.

## Turning radius grows with speed

At full steering lock, the car's minimum turning radius depends on its speed: the faster it goes, the wider the tightest arc it can manage. The game has no single formula for it. The community-measured data (RLUtilities' `max_turning_curvature`) is a table of maximum curvature against speed, interpolated linearly, with radius = 1 / curvature.

{% include figure.html src="/assets/rlbot/turning-radius.svg" alt="Chart of the minimum turning radius against speed, rising from 145 uu at rest through 251, 426, 725 and 909 uu to 1,136 uu at the 2,300 uu/s speed cap" caption="Minimum turning radius against speed, from the published curvature table. The markers are the table's own points." %}

| Speed (uu/s) | 0 | 500 | 1,000 | 1,500 | 1,750 | 2,300 |
|:---|---:|---:|---:|---:|---:|---:|
| Minimum radius (uu) | 145 | 251 | 426 | 725 | 909 | 1,136 |
| In metres (1 uu = 1 cm) | 1.5 | 2.5 | 4.3 | 7.3 | 9.1 | 11.4 |

At the speed cap the tightest turning radius is therefore about 11 m, so the circle is about 23 m across. At rest the radius is about 1.5 m, so the car doesn't turn on the spot either.

The practical consequence is a trade-off:

Faster is not always sooner. A car that slows down can take a tighter line, while a car at full speed may have to sweep a wide arc, or overshoot and double back.

This is why the [shot alignment](/ProjectPages/rlbot/aligning-shots/) logic would slow the car when the approach angle is poor.

## Arc-then-line paths

A simple and useful path model is arc then line: the car turns along a circle of its current minimum radius until it points at the target, then drives straight. It is a single-turn simplification of the Dubins paths used in robotics.

For a target `x` ahead and `y` to the right of the car (turn right; mirror the sign for a target on the left), with minimum radius `r`:

1. The turning circle has its centre at (0, r) in the car's frame.
2. Let `d` be the distance from that centre to the target. If `d < r` the target is inside the circle and unreachable by this path. The car must slow down, which shrinks `r`.
3. Otherwise the tangent length is √(d² − r²), and the arc angle follows from the tangent point.

~~~python
def arc_then_line(x, y, r):
    """Turn right on a circle of radius r, then go straight. Returns (arc angle, tangent length)
    or None if the target is inside the turning circle."""
    y = abs(y)                                  # mirror a left-hand target
    cx, cy = 0.0, r                             # centre of the turning circle
    d = math.hypot(x - cx, y - cy)
    if d < r:
        return None
    alpha = math.atan2(y - cy, x - cx)          # direction from the centre to the target
    beta = math.acos(r / d)
    arc = (alpha - beta + math.pi / 2) % math.tau   # from the start point (straight below the centre)
    return arc, math.sqrt(d * d - r * r)
~~~

A worked example: a target 600 uu ahead and 800 uu to the right, with a 400 uu minimum radius. The arc is 67.4° (470 uu long) and the straight section is 600 uu, so the path is 1,070 uu against a straight-line 1,000 uu, 7% longer.

The reachability condition has a neat form. The largest usable radius for that target is (x² + y²) / (2y) = 625 uu. From the turning table, the car's minimum radius is 625 uu at about 1,390 uu/s, so above that speed the target is inside the circle and this path doesn't exist.

## Estimating time-to-target

With a path length in hand, the time still depends on the speed along it, and from the [ground kinematics](/ProjectPages/rlbot/ground-kinematics/) acceleration is itself a function of speed. Rather than solving that analytically, the practical approach is numerical.

One estimator that works with that, still illustrative: pick an arc speed `v`, brake to it from the current speed, turn at that speed's minimum radius, then accelerate down the tangent. Try a range of arc speeds and keep the quickest.

~~~python
def eta(x, y, v0, boost=True, step=25.0):
    best = None
    v = v0
    while v > 0:
        r = radius_at(v)                              # from the curvature table
        path = arc_then_line(x, y, r)
        if path:
            arc, tangent = path
            t_brake = max(0.0, (v0 - v) / 3500.0)     # braking deceleration
            t_arc = r * arc / v
            t_line, _ = time_to_distance(tangent, boost, v0=v)
            total = t_brake + t_arc + t_line
            best = total if best is None else min(best, total)
        v -= step
    return best
~~~

For the target above, 600 ahead and 800 right, the estimator gives these times (straight-line time in brackets: the time it would take if the car could go in a straight line to the target):

| Speed now | Estimated time | Best arc speed | Straight-line time |
| ---: | ---: | ---: | ---: |
| 800 uu/s | 1.03 s | 800 uu/s | 0.76 s |
| 1,000 uu/s | 0.95 s | 1,000 uu/s | 0.70 s |
| 1,400 uu/s | 0.84 s | 1,375 uu/s | 0.59 s |
| 2,000 uu/s | 1.01 s | 1,375 uu/s | 0.45 s |

Two things stand out. The straight-line figure is always optimistic, and increasingly so at speed: at 2,000 uu/s the real time is more than twice it. And arriving sooner does not mean starting faster. Starting at 2,000 uu/s the car loses time braking to the highest speed it can turn at, so it is slower than the car starting at 1,400 uu/s.

The model is deliberately crude. It brakes instantly to a constant arc speed, ignores the speed lost in a turn, and treats the car as a point. Treat it as a ranking tool for comparing options rather than a prediction, and tune it against logged runs of the real car.

That estimator unlocks the questions the bot actually cares about:

- Can I beat the opponent to the ball? Compare time estimates.
- Intercepting a moving ball. For each candidate time `t` along the ball's predicted path, ask whether the car can reach that ball position in `t` or less. The earliest feasible `t` is the intercept.
- Is boost worth it here? Run the estimate with and without the boost term and compare the arrival times against the boost cost.

## Status and next steps

This analysis is still in progress. The curvature data hasn't been tuned against measured bot behaviour, and the intercept search doesn't yet cover aerial targets, where the [aerial kinematics](/ProjectPages/rlbot/aerial-kinematics/) feasibility check replaces the ground-path estimator.
