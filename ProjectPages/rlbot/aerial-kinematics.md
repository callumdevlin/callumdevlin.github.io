---
title: RL Bot — Aerial Kinematics
permalink: /ProjectPages/rlbot/aerial-kinematics/
description: >
  Solving for the orientation and boost a Rocket League car needs to reach
  a target point in the air at a given time.
---

For the bot to hit an aerial it has to juggle a lot of factors at once: ball height, ball speed, car speed, distance, angle, remaining boost. The idea is simple — point the car at the right place and boost — but getting it robust is fiddly. These notes set out the underlying kinematics.

Define the quantities of interest:

- $$c(t)$$ — the car's position
- $$f(t)$$ — the unit vector in which the car is facing
- $$B(t)$$ — acceleration due to boost
- $$P$$ — the target location

All positions and directions are world vectors (X, Y, Z).
{:.note}

While airborne, the only accelerations available are boost (along the facing direction) and gravity, so the car's motion is governed by the differential equation:

$$
\ddot{c}(t) = B(t)\, f(t) + g\,\hat{z}, \qquad \dot{c}(0) = v_0,\quad c(0) = x_0,\quad f(0) = f_0
$$

$$\hat{z}$$ is the unit vector in the z-direction; in Rocket League $$g$$ is negative (downward) with magnitude $$650\frac{uu}{s^2}$$.
{:.note}

Suppose we want to arrive at $$P$$ at time $$T$$, and we start solving at elapsed time $$\Delta t$$. Integrating twice with constant boost acceleration $$B_0$$ along a fixed direction $$f^*$$, and rearranging for that boost term, gives:

$$
B_0 f^* \;=\; \frac{2}{(T-\Delta t)^2}\left(P - x_0 - v_0\,\Delta t - \tfrac{1}{2} g\, \Delta t^2\, \hat{z}\right) \;=\; \bar{A}
$$

$$T$$ is the total time at which we want to arrive at the target; $$T - \Delta t$$ is the time remaining.
{:.figcaption}

Both sides of this equation have units of acceleration — so the right-hand side $$\bar{A}$$ can be read as *the acceleration required to be at target $$P$$ in the time remaining*, after accounting for where the car already is, where its current velocity is carrying it, and what gravity will do along the way.

From there the solution separates neatly into a magnitude and a direction:

$$
B_0 = \lVert \bar{A} \rVert, \qquad f^* = \frac{\bar{A}}{\lVert \bar{A} \rVert}
$$

## The Simple Answer

Align the car with the required direction $$(f = f^*)$$ and feather the boost so the average acceleration matches $$B_0$$. Because the ball — and therefore the target — keeps moving, this isn't solved once: the bot re-evaluates $$\bar{A}$$ every tick and keeps re-aligning, so the aerial is really a continuous correction loop rather than a single launch calculation.

Two practical checks fall straight out of the maths before committing to an aerial at all:

- If $$B_0$$ exceeds the boost acceleration the car can actually produce, the target is unreachable in the time available — don't jump.
- If $$f^*$$ points somewhere the car can't rotate to face quickly enough, the time budget needs to include the reorientation, or the aerial will arrive late.

*Related: [aligning shots on target](/ProjectPages/rlbot/aligning-shots/) — because arriving at the ball is only half the job.*
