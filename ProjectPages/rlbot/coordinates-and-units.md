---
title: RL Bot, Game State, Coordinates and Units
crumb: Coordinates and units
permalink: /ProjectPages/rlbot/coordinates-and-units/
type: maths
section: rlbot
nav_order: 2
status: growing
applies: RLBot v4 (`rlbot` 1.x). Field sizes and axis conventions come from the RLBot documentation and the framework's template code.
reviewed: 2026-10-14
description: >
  The tick loop, time step, units, the world's axes and handedness, and how to turn a
  world position into the car's own frame.
---

Most of the bugs I've seen in bot code come from mixing up frames and units, not from hard maths. This page pins down the conventions the other pages rely on: what the bot is given each tick, how long a tick is, which way the axes point, and how to express a target in the car's own frame.

## The tick loop

The bot's decision step is one method, called once per tick:

~~~python
def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
    my_car = packet.game_cars[self.index]
    ball = packet.game_ball
    ...
    return controls
~~~

The packet carries, for every car and the ball, a `physics` block with `location`, `velocity` and `rotation`, plus the car's boost and the match state (`packet.game_info.seconds_elapsed`, whether the kick-off pause is active, and so on). The bot returns a `SimpleControllerState` of throttle, steer, pitch, yaw, roll, jump, boost and handbrake. These are the v4 names; RLBot v5 renames most of them.

## Time step

The game's physics runs at 120 Hz. The framework's default tick rate for a bot is 60 and this bot's config asks for 120, so a tick is 1/120 s or 1/60 s depending on that setting. Don't hard-code it. Either read the time between packets from `seconds_elapsed`, or state the step you assume.

Step size matters less than you might fear for decision-making. Integrating the car's straight-line motion in 1/60 s steps gives times within about 0.02 s of a very fine reference (checked for a 2,000 uu run), which is plenty for choosing between options. It matters more for anything that counts frames: a scripted 0.05 s button press is a different number of ticks, and a slightly different real length, at 60 and 120 Hz.

## Units

The game reports lengths in Unreal Units (**uu**), speeds in uu/s, accelerations in uu/s² and angles in radians.

| Quantity | Unit | Useful conversion |
| --- | --- | --- |
| Length | uu | 1 uu = 1 cm |
| Speed | uu/s | 2,300 uu/s (the speed cap) = 23 m/s = 82.8 km/h |
| Acceleration | uu/s² | 650 uu/s² (gravity) = 6.5 m/s² |
| Angle | rad | Euler pitch, yaw and roll; convert with `math.degrees` only for display |

I keep everything in game units and convert only for display. Mixing uu with SI inside a formula is the quickest way to get a result that is wrong by a factor of 100.

## The world frame

The field is a long box with the goals at either end:

- **z is up.** The ground is z = 0, and a car resting on its wheels has its origin at about z = 17.
- **The goals are at y = ±5120.** Team 0 (blue) defends the goal at negative y and attacks the one at positive y. Walls are at x = ±4096, and the back of each net is at |y| = 6000.
- **The goal is 642.775 uu tall**, so its centre is at z ≈ 321.4.
- **Yaw 0 faces +x**, and yaw increases from +x towards +y. The RLBot documentation notes that x is not laid out the usual Cartesian way.

That last point is the one that catches people. With forward, right and up built from the car's Euler angles as below, (forward × right) · up comes out as +1. For a real car, forward × right points *down*, so a +1 means the coordinates are mirrored: the world is **left-handed**. Facing +x (yaw 0), the car's right-hand side is +y. Turn to face +y (yaw 90°) and its right-hand side is −x.

~~~python
# From the RLBot Python template (MIT licence), as used in the bot.
class Orientation:
    def __init__(self, rotation):
        self.yaw = float(rotation.yaw)
        self.roll = float(rotation.roll)
        self.pitch = float(rotation.pitch)

        cr, sr = math.cos(self.roll), math.sin(self.roll)
        cp, sp = math.cos(self.pitch), math.sin(self.pitch)
        cy, sy = math.cos(self.yaw), math.sin(self.yaw)

        self.forward = Vec3(cp * cy, cp * sy, sp)
        self.right = Vec3(cy*sp*sr - cr*sy, sy*sp*sr + cr*cy, -cp*sr)
        self.up = Vec3(-cr*cy*sp - sr*sy, -cr*sy*sp + sr*cy, cp*cr)
~~~

## Into the car's frame

Almost every decision is easier in the car's own frame, where the question is "how far ahead and how far to the right is the target?" The template's `relative_location` does it with three dot products:

~~~python
def relative_location(center: Vec3, ori: Orientation, target: Vec3) -> Vec3:
    d = target - center
    return Vec3(d.dot(ori.forward), d.dot(ori.right), d.dot(ori.up))   # ahead, right, above
~~~

Check it on a case you can picture. A car at the origin with yaw 90° faces +y. A target at world (0, 1000) is dead ahead, so the local result is (1000, 0). A target at world (−1000, 0) is on its right, so the result is (0, 1000). One at (1000, 0) is on its left, so the right-hand component is −1000. I ran exactly these as tests, along with the yaw-0 case, so the sign convention above is checked rather than assumed.

Once the target is in the car's frame, the steering decision is the signed angle `atan2(right, forward)`, which the [steering page](/ProjectPages/rlbot/steering/) builds on.

## Things that go wrong

- **Team-dependent goals.** Which goal you attack depends on your team. In the public snapshot the attacking goal is hard-coded to the positive-y goal, which is only correct for the blue team. Look it up from the team index instead.
- **Ball radius.** Older documentation and the template use 92.75 uu. The current RLBot documentation and the RocketSim simulator use 91.25 uu. The 1.5 uu gap rarely matters, but cite which one you use.
- **The car's origin isn't its nose.** The packet's position is the centre of the car's hitbox offset, roughly 73 to 74 uu behind the nose of an Octane, so "distance to the ball" is not "distance to contact".
- **Ball prediction is an estimate.** The framework's ball path gives about six seconds of future positions at 60 slices a second in v4. Treat far-future slices as less reliable than near ones.

## Sources

- RLBot documentation: [useful game values](https://wiki.rlbot.org/v4/botmaking/useful-game-values/) and [tick rate](https://wiki.rlbot.org/v4/botmaking/tick-rate/), read 2026-10-14.
- [RLBotPythonExample](https://github.com/RLBot/RLBotPythonExample) (MIT licence) for `Orientation` and `relative_location`. The handedness is my own check of those formulas.
