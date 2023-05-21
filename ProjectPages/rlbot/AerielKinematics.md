---
layout: default
title: Aeriel Kinematics
---

In order for our bot to be able to calculate ball position and how to hit an aeriel there is many factors to consider: ball height, ball speed, car speed, distance, angle, boost etc. The idea seems simple but can be rather fidgety when implementing.

The general kinematics of air control can be defined as the following:

- $$c(t) =$$ car's position

- $$f(t) =$$ unit directional vector in which our car faces

- $$B(t) =$$ acceleration due to boost

- $$P =$$ Target Location

These will both be in world vector coordinates (X, Y, Z).
{:.note}

The car's motion can be represented by a differential equation:

$$
\begin{aligned}
c(t) = B(t) \times f(t) + g z : \Dot c(0) = v_0, c(0) = x_0, f(0) = f_0
\end{aligned}
$$

$$z$$ is the unit vector in the z-direction.
{:.note}

After some further integration, rearranging and a whole lot of implementing some expressions we get:

$$
\begin{aligned}
B_0 f^* = \frac{2}{(T-\Delta t)^2}(P-x_0-v_0\Delta t -\frac{1}{2}g \Delta t^2 z) = \Bar A
\end{aligned}
$$