---
title: RL Bot — Aligning Shots on Target
permalink: /ProjectPages/rlbot/aligning-shots/
description: >
  Hitting the ball is easy — hitting it towards the goal requires approaching
  through an offset point behind the ball, plus angle checks to know when
  to commit.
---

A bot that simply drives at the ball will hit it — in a random direction. The ball goes (roughly) the way it's struck, so to score, the car needs to arrive at the ball **travelling along the line from ball to goal**. That turns shooting into a positioning problem: don't target the ball, target a point *behind* it.

## The Offset Approach Point

Take the unit vector from the ball to the centre of the enemy goal:

$$
\hat{d} = \frac{G - b}{\lVert G - b \rVert}
$$

where $$G$$ is the goal location and $$b$$ the ball location. The approach point sits behind the ball along the *opposite* of that direction:

$$
P_{approach} = b - \hat{d}\,(r_{ball} + s)
$$

with $$r_{ball} \approx 92.75\,uu$$ (the ball's radius) and $$s$$ an extra standoff distance. Driving through $$P_{approach}$$ means that by the time the car contacts the ball, its velocity is pointing through the ball at the goal.

In code, using the [`Vec3` class](/ProjectPages/rlbot/vectors/):

~~~python
ball_to_goal = (enemy_goal - ball_location).normalized()
approach_point = ball_location - ball_to_goal * (BALL_RADIUS + standoff)
~~~

A larger `standoff` gives the car more room to straighten up before contact — useful at speed — at the cost of a longer route.

## Knowing When You're Lined Up

The offset point gets the geometry right; the bot still needs to *check* its alignment before committing, otherwise it clips the ball at an angle and concedes possession. Two angle checks (via `ang_to`) do the job:

- **Car → ball vs car facing** — am I actually driving at the ball?
- **Car → ball vs ball → goal** — if I hit it now, does it go towards the goal?

When both angles are small, floor it (and boost). When the second angle is large, the bot is approaching from the wrong side — so instead of shooting, it keeps steering for the approach point, slowing down if necessary, because [turning radius grows with speed](/ProjectPages/rlbot/movingpath/). A simple threshold scheme works surprisingly well:

~~~python
if shot_angle < 0.3:           # well aligned — commit
    controls.throttle, controls.boost = 1.0, True
elif shot_angle < 1.0:         # close — keep speed, keep correcting
    controls.throttle = 1.0
else:                          # wrong side of the ball — reposition
    controls.throttle = 0.5    # slow to tighten the turn
~~~

Illustrative thresholds — the real values want tuning against the car's turning behaviour at speed.
{:.figcaption}

## Where This Breaks Down

This static-offset approach assumes the ball is roughly stationary. Against a moving ball, the bot has to aim at where the ball *will be*, which couples this page with time-to-target estimation — exactly the problem explored in [path optimisation](/ProjectPages/rlbot/movingpath/). The debug renderer's line-to-target drawing (see the [overview](/ProjectPages/rlbot/overview/)) makes mis-predictions immediately visible: the white line points at empty grass where the ball used to be.
