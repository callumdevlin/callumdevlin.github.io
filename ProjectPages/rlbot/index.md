---
title: Rocket League Bot Notes
crumb: Rocket League
permalink: /ProjectPages/rlbot/
type: index
section: rlbot
nav_order: 0
toc: false
description: >
  The maths and Python behind a hard-coded Rocket League bot: vectors, steering, path
  planning and aerial motion.
---

I wrote the bot with Daniel McMurray on the [RLBot](https://rlbot.org) framework. The [repository](https://github.com/callumdevlin/RL-Bot) is an early prototype, and some examples in these notes explore designs that are not yet implemented in it. Code here is for the RLBot v4 Python API (the `rlbot` 1.x package); the v5 pre-release has a different API.

## The pages

1. [Project overview](/ProjectPages/rlbot/overview/): what the framework provides, how the bot is structured and what it does today.
2. [Game state, coordinates and units](/ProjectPages/rlbot/coordinates-and-units/): the tick loop, the world's handedness, converting a world position into the car's own frame, and units.
3. [3D vector system](/ProjectPages/rlbot/vectors/): the `Vec3` class, distances, angles, and the ways `acos` fails.
4. [Steering and driving](/ProjectPages/rlbot/steering/): turning an angle into a steering input, and why a proportional controller can circle a target forever.
5. [Ground kinematics](/ProjectPages/rlbot/ground-kinematics/): how the car accelerates, brakes, coasts and boosts, and how far and how fast it gets.
6. [Path optimisation analysis](/ProjectPages/rlbot/movingpath/): turning radius against speed, arc-then-line paths and time-to-target.
7. [Aligning shots on target](/ProjectPages/rlbot/aligning-shots/): hitting the ball is easy; hitting it towards the goal needs an offset approach point.
8. [Aerial kinematics](/ProjectPages/rlbot/aerial-kinematics/): solving for the orientation and boost needed to reach a point in the air at a given time.
9. [Behaviours and testing](/ProjectPages/rlbot/behaviours-and-testing/): behavioural states, debug rendering and repeatable tests.

Distances are in Unreal Units (uu, where 1 uu = 1 cm) and speeds in uu/s, because that is what the game reports. The constants come from community measurements, not from Psyonix, and each page says where. Rocket League is a game by Psyonix, and this site isn't affiliated with it.
