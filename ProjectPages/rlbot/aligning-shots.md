---
title: RL Bot, Aligning Shots on Target
crumb: Aligning shots
permalink: /ProjectPages/rlbot/aligning-shots/
type: maths
section: rlbot
nav_order: 7
status: wip
applies: A design for ground shots at a roughly stationary ball. The code is illustrative and is not in the public bot, which currently steers straight at the ball.
reviewed: 2026-10-14
description: >
  Hitting the ball is easy; hitting it towards the goal means approaching through an
  offset point behind it, with angle checks to know when to commit.
---

A bot that simply drives at the ball will hit it, in whatever direction the contact happens to send it. The ball goes roughly the way it is struck, so to score, the car has to arrive at the ball **travelling along the line from the ball to the goal**. That turns shooting into a positioning problem: don't aim at the ball, aim at a point *behind* it.

The public bot doesn't do this yet. It steers at the ball's position. This page is the design I've worked out for what comes next, with illustrative code.
{:.note}

## The offset approach point

Take the unit vector from the ball to the target on the enemy goal:

$$
\hat{d} = \frac{G - b}{\lVert G - b \rVert}
$$

where $$G$$ is the goal location and $$b$$ the ball location. The approach point sits behind the ball, on the opposite side from the goal:

$$
P_{approach} = b - \hat{d}\,(r_{ball} + s)
$$

with $$r_{ball} \approx 92.75\,uu$$ (the ball's radius in the older documentation and the template; the current RLBot documentation uses 91.25) and $$s$$ an extra standoff distance. For a ground shot, take $$\hat{d}$$ in the flat plane so the point stays on the ground.

~~~python
ball_to_goal = (enemy_goal - ball_location).flat().normalized()
approach_point = ball_location - ball_to_goal * (BALL_RADIUS + standoff)
~~~

A worked example: ball at (1000, 2000), goal centre at (0, 5120). The ball-to-goal direction is (−0.305, 0.952), and with a 100 uu standoff the approach point is (1059, 1816), which is 192.75 uu behind the ball on the line to the goal. I checked that the point lies on that line, at that distance, behind the ball.

A larger `standoff` gives the car more room to straighten up before contact, which helps at speed, at the cost of a longer route. Note that the car's position in the game packet is not its nose. The nose is roughly 73 to 74 uu ahead of the origin on an Octane, so if the target point is where the car's *origin* should be, the standoff has to be at least that large or the car will already be overlapping the ball.

## How precisely do you have to point?

Driving through the approach point doesn't guarantee a good shot. Any heading error at that point moves the contact sideways from the ball's centre. With the approach point 192.75 uu from the ball (a 100 uu standoff), the sideways miss is 192.75 × sin(error):

| Heading error at the approach point | Sideways miss of the ball's centre |
| ---: | ---: |
| 5° | 17 uu |
| 10° | 33 uu |
| 20° | 66 uu |
| 30° | 96 uu |

A 30° error puts the contact more than a ball-radius off-centre, which is a glancing blow. A larger standoff makes the same angular error worse, which is the cost of the extra room.

## Aiming between the posts

Aiming at the goal's centre is a simplification. The goal mouth is 1,785.5 uu wide (892.755 uu from centre to each post), so there's room to aim for a point nearer a post, away from the keeper. The RLBot documentation's [method for shooting the ball towards a target](https://wiki.rlbot.org/v4/botmaking/shooting-the-ball-towards-or-away-from-a-target/) does this. It treats the goal as two post targets, clamps the car-to-ball direction so the approach falls between them, and offsets the approach point back along that direction by the ball radius. Two points give a range of acceptable approach angles instead of a single line, which is a better starting point than the plain centre line.

## Knowing when you're lined up

The offset point gets the geometry right, but the bot still needs to *check* its alignment before committing. Otherwise it clips the ball at an angle and gives up possession. Two angle checks do the job, both unsigned in the flat plane:

- **Car's heading against the direction to the ball:** is it actually driving at the ball?
- **Car to ball against ball to goal:** if it hit the ball now, would the ball go towards the goal?

Use the guarded `angle_between` from the [vectors page](/ProjectPages/rlbot/vectors/), not the template's bare `acos`, which raises an error exactly when two directions are perfectly aligned. When both angles are small, the car can drive through and boost. When the second angle is large, the bot is approaching from the wrong side, so instead of shooting it keeps steering for the approach point and slows if necessary, because [turning radius grows with speed](/ProjectPages/rlbot/movingpath/).

~~~python
to_ball = (ball_location - car_location).flat()
ball_to_goal = (enemy_goal - ball_location).flat()
shot_angle = angle_between(to_ball, ball_to_goal)     # unsigned, radians, safe for zero vectors

if shot_angle < 0.3:           # well aligned: commit
    controls.throttle, controls.boost = 1.0, True
elif shot_angle < 1.0:         # close: keep speed, keep correcting
    controls.throttle = 1.0
else:                          # wrong side of the ball: reposition
    controls.throttle = 0.5    # slow to tighten the turn
~~~

The thresholds are illustrative and need tuning against the car's turning behaviour at speed. The table above gives a feel for them: 0.3 rad is about 17°, which is a miss of roughly 57 uu at 192.75 uu, and the car would want to be much more aligned than that for a precise shot.

## Where this breaks down

The static offset assumes the ball is roughly stationary. Against a moving ball the bot has to aim at where the ball *will be*, which ties this page to time-to-target estimation and the intercept search described in the [path analysis](/ProjectPages/rlbot/movingpath/). Even then, the direction the ball leaves in depends on its incoming velocity as well as the car's, so the offset geometry is a first approximation, not the whole answer.

The debug renderer's line-to-target drawing (see the [overview](/ProjectPages/rlbot/overview/)) makes bad predictions obvious: the line points at empty grass where the ball used to be.
