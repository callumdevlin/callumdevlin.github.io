---
layout: default
title: Aerial Kinematics
---

In order for our bot to be able to calculate ball position and how to hit an aerial there is many factors to consider: ball height, ball speed, car speed, distance, angle, boost etc. The idea seems simple but can be rather fidgety when implementing.

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
c(t) = B(t) \times f(t) + g z : \dot c(0) = v_0, c(0) = x_0, f(0) = f_0
\end{aligned}
$$

$$z$$ is the unit vector in the z-direction.
{:.note}

After some further integration, rearranging and a whole lot of implementing some expressions we get:

$$
\begin{aligned}
B_0 f^* = \frac{2}{(T-\Delta t)^2}(P-x_0-v_0\Delta t -\frac{1}{2}g \Delta t^2 z) = \bar A
\end{aligned}
$$

$$T$$ = boost
{:.figcaption}

It becomes evident that both sides of the given equation have the characteristic of acceleration. As a result, we can interpret the right-hand side as representing the acceleration that is needed to be at the target location $$P$$ in the time $$\Delta t$$.

As a result of rearranging: $$B_0 = \Vert \bar A \Vert$$ and $$f^* = \frac{\bar A}{\Vert \bar A \Vert}$$

## The simple answer

The main objective of this is to align the car in the right direction $$(f = f^*)$$ and feather the boost to achieve the right acceleration, make sure to keep aligning the car throughout this as the target location will change.
Now to actually implement this into our code, we can use it to find the following:

- To tell if our target($$P$$) can be reached in the amount of time, check if $$B_0$$ is less than the cars boost acceleration ($$991.667 \frac{uu}{s^2}$$). If $$B_0 > T$$ then the car wont reach it's target in time.

You can use this equation to find the magnitude and direction of acceleration required to make contact:

$$
\begin{aligned}
  \bar A = \frac{2}{(T-\Delta t)^2}(P-x_0-v_0\Delta t -\frac{1}{2}g \Delta t^2 z)
\end{aligned}
$$

- To calculate how much boost is required, use the average acceleration $$B_0$$ and how long we will be boosting for $$(\Delta t - T)$$ this will tell us how long to boost for. To reach the target your car might need to 'feather' the boost so it can remain airborn, this was achieved using the following code:

~~~python
class Do_Aerial:

  def __init__(self):
    self.boost_counter = 0.0
    self.max_boost_acc = 1000.0

  def get_output():

    # find B_0 using A
    A = ...
    B_0 = norm(A) #normalises as a vector
    use_boost = 0
    
    # compute the average boost ratio per time using boost clock
    use_boost -= round(self.boost_counter)
    self.boost_counter += B_0 / self.max_boost_acc
    use_boost += round(self.boost_counter)
    
    self.controls.boost = 1 if use_boost else 0
~~~


Credit to Sam Mish for the assisted research
{:.note}