---
title: RL Bot, 3D Vector System
crumb: Vectors
permalink: /ProjectPages/rlbot/vectors/
type: maths
section: rlbot
nav_order: 3
applies: RLBot v4 Python API. The `Vec3` class is the one from the RLBot Python template, as used in the bot.
reviewed: 2026-10-14
description: >
  The Vec3 class under the bot: distances, projections, angles, and the ways the
  usual acos angle formula fails.
---

Everything the bot does starts with positions and velocities read from the game packet as x, y, z coordinates. To work with them cleanly there is a `Vec3` class. It wraps the three components and provides the vector operations the rest of the maths is built from: addition, subtraction, scaling, dot and cross products and length. Each component stays individually accessible, which is handy when only the height (z) matters.

The class is from the [RLBot Python template](https://github.com/RLBot/RLBotPythonExample) (MIT licence), which the bot is built on. The bot adds a few helpers of its own around it.

~~~python
class Vec3:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x: Union[float, 'Vec3', 'Vector3'] = 0, y: float = 0, z: float = 0):
        if hasattr(x, 'x'):
            # Given a vector: copy it, so the game's own Vector3 objects convert directly
            self.x = float(x.x)
            self.y = float(x.y) if hasattr(x, 'y') else 0
            self.z = float(x.z) if hasattr(x, 'z') else 0
        else:
            self.x, self.y, self.z = float(x), float(y), float(z)

    def __add__(self, other): return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other): return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, scale): return Vec3(self.x * scale, self.y * scale, self.z * scale)
~~~

## Distance and speed

The most-used operation is distance, to the ball, to the goal or to a boost pad:

~~~python
def length(self):
    return math.sqrt(self.x2 + self.y2 + self.z2)

def dist(self, other: 'Vec3') -> float:
    return (self - other).length()
~~~

`dist` subtracts one vector from the other and takes the length of the result, which is Pythagoras in three dimensions. The same `length()` on the velocity vector gives the car's speed. For ground play it is often more useful to ignore height with `flat()`, which zeroes z, so a ball in the air above the car doesn't count as "far away".

## Projection: how fast am I closing?

The dot product of the velocity with a unit direction is the part of the velocity along that direction. That answers "how fast am I moving towards the ball?":

~~~python
to_ball = (ball_location - car_location).flat()
closing_speed = car_velocity.flat().dot(to_ball.normalized())   # uu/s; negative means moving away
~~~

`normalized()` divides by the length, so it fails on a zero vector. A car sitting exactly on the ball is rare, but a target equal to the car's own position is not, so guard it.

## Angles

The unsigned angle between two vectors comes from the dot product identity:

$$
\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\lVert\mathbf{a}\rVert \, \lVert\mathbf{b}\rVert}
$$

The template implements it as:

~~~python
def ang_to(self, ideal: 'Vec3') -> float:
    cos_ang = self.dot(ideal) / (self.length() * ideal.length())
    return math.acos(cos_ang)
~~~

It returns a value between 0 and π: zero means perfectly aligned and π means exactly opposite. It has three weaknesses.

- A zero-length vector divides by zero.
- Floating-point rounding can push the cosine to 1.0000000000000002 for two vectors that are exactly parallel, and `acos` then raises a "math domain error". In a test of random exactly-parallel pairs, about one in five failed this way. That is the worst moment for it to happen, because "exactly lined up" is when the car is doing well.
- It is unsigned. Targets 45° to the left and 45° to the right both give 0.785, so it can say how far to turn but not which way.

A guarded version fixes the first two:

~~~python
def angle_between(a: Vec3, b: Vec3) -> float:
    """Unsigned angle in [0, pi]; 0.0 if either vector has no length."""
    la, lb = a.length(), b.length()
    if la == 0.0 or lb == 0.0:
        return 0.0
    return math.acos(max(-1.0, min(1.0, a.dot(b) / (la * lb))))
~~~

The third needs a signed angle. For steering, the cleanest way is in the car's own frame (see [coordinates](/ProjectPages/rlbot/coordinates-and-units/)): `atan2(right, forward)` is positive when the target is on the right. That is what the bot's steering uses, and it never has the `acos` problems. In the flat world plane, the same thing for two direction vectors is `atan2(a.x*b.y - a.y*b.x, a.dot(b))`, where a positive result means `b` is to the right of `a`.

## Wrapping angles

Subtracting two headings can land outside the range you expect. 170° minus −170° is 340° raw, but the two headings are only 20° apart. Wrap any difference back into [−π, π) before using it:

~~~python
def wrap_pi(angle: float) -> float:
    return ((angle + math.pi) % math.tau) - math.pi
~~~

*The code on this page is illustrative, apart from the template's `Vec3` and `ang_to`.*
