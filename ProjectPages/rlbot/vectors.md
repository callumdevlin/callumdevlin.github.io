---
title: RL Bot — 3D Vector System
permalink: /ProjectPages/rlbot/vectors/
description: >
  The Vec3 class underpinning the bot — distances, angles and dot products
  in Rocket League's game space.
---

Everything the bot does starts with positions and velocities read from the game tick packet as X, Y, Z coordinates. To work with them cleanly there is a `Vec3` class, which wraps the three components and provides the vector operations — addition, subtraction, scaling, dot products and so on — that the rest of the bot's maths is built from. Each component remains individually accessible, which is handy when, say, only the height (Z) matters.

~~~python
class Vec3:
    __slots__ = [
        'x',
        'y',
        'z'
    ]
    def __init__(self, x: Union[float, 'Vec3', 'Vector3']=0, y: float=0, z: float=0):
        if hasattr(x, 'x'):
            self.x = float(x.x)
            self.y = float(x.y) if hasattr(x, 'y') else 0
            self.z = float(x.z) if hasattr(x, 'z') else 0
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
~~~

The basic structure of the vector class. The constructor also accepts an existing vector, so the game's own `Vector3` objects convert directly.
{:.figcaption}

Operations are added as methods. Addition, for example, lets two vectors be summed with the normal `+` operator:

~~~python
def __add__(self, other: 'Vec3') -> 'Vec3':
    return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
~~~

## Distance

The most-used operation in the whole bot is distance — to the ball, to the goal, to a boost pad:

~~~python
def length(self):
    return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def dist(self, other: 'Vec3') -> float:
    return (self - other).length()
~~~

`dist` subtracts one vector from the other and takes the length of the result — Pythagoras in three dimensions. The magnitude of a velocity vector via `length()` is also how the bot knows its own speed.

## Angles

In 3D space the bot constantly needs to know whether it's *facing* something — the ball, a target point, the goal. The angle between two vectors comes from the dot product identity:

$$
\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\lVert\mathbf{a}\rVert \, \lVert\mathbf{b}\rVert}
$$

~~~python
def ang_to(self, ideal: 'Vec3') -> float:
    cos_ang = self.dot(ideal) / (self.length() * ideal.length())
    return math.acos(cos_ang)
~~~

This returns a value between 0 and π: zero means perfectly aligned, π means facing exactly the wrong way. Calling it with the car's facing direction and the direction to a target gives the steering error — small angle, drive on; large angle, turn harder or slow down. That single function does a lot of heavy lifting in [shot alignment](/ProjectPages/rlbot/aligning-shots/).

*Next: [ground kinematics](/ProjectPages/rlbot/ground-kinematics/) — what the car can actually do with throttle, brake and boost.*
