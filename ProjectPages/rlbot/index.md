---
title: Rocket League Bot Notes
crumb: Rocket League
permalink: /ProjectPages/rlbot/
type: index
section: rlbot
nav_order: 0
status: growing
toc: false
description: >
  The maths and code behind a hard-coded Rocket League bot in Python: coordinates,
  vectors, steering, ground and aerial motion, paths and shot alignment.
---

These are notes on the maths and code behind a Rocket League bot written in Python on the [RLBot](https://rlbot.org) framework. The bot is hard-coded rather than machine-learned. Every behaviour is explicit maths and logic, which makes it a good excuse to work through the game's physics properly. Two of us wrote the bot (the repository README credits Daniel McMurray and me), and these pages are my write-up of the maths, so that it's useful to anyone building their own.

**What the public repository contains.** The bot's source is on [GitHub](https://github.com/callumdevlin/RL-Bot). The public snapshot is an early one built on the RLBot Python template. It steers with a proportional controller, always drives at full throttle and boosts whenever it has boost, runs scripted flips and picks between a few behaviour labels. It is also incomplete: it imports a `behaviours` module that isn't in the repository. The offset approach point, arc-and-line paths, time estimates and aerial solver in these notes are maths and designs I've worked out, written as **illustrative code**. They aren't in that repository, and I haven't published results from them.
{:.note}

**Framework version.** The bot uses RLBot's Python API for v4 of the framework, which is the `rlbot` 1.x package on PyPI. RLBot v5 is in pre-release with a different API (different class names, packet structure and rendering calls), so code and API names here won't carry over unchanged.
{:.note}

## The pages

1. [**Project overview**](/ProjectPages/rlbot/overview/): what the framework provides, how the bot is structured and what it actually does today.
2. [**Game state, coordinates and units**](/ProjectPages/rlbot/coordinates-and-units/): the tick loop, the world's handedness, converting a world position into the car's own frame, and units.
3. [**3D vector system**](/ProjectPages/rlbot/vectors/): the `Vec3` class, distances, angles, and the ways `acos` fails.
4. [**Steering and driving**](/ProjectPages/rlbot/steering/): turning an angle into a steering input, and why a proportional controller can circle a target forever.
5. [**Ground kinematics**](/ProjectPages/rlbot/ground-kinematics/): how the car accelerates, brakes, coasts and boosts, and how far and how fast it gets.
6. [**Path optimisation analysis**](/ProjectPages/rlbot/movingpath/): turning radius against speed, arc-then-line paths and time-to-target.
7. [**Aligning shots on target**](/ProjectPages/rlbot/aligning-shots/): hitting the ball is easy; hitting it towards the goal needs an offset approach point.
8. [**Aerial kinematics**](/ProjectPages/rlbot/aerial-kinematics/): solving for the orientation and boost needed to reach a point in the air at a given time.
9. [**Behaviours and testing**](/ProjectPages/rlbot/behaviours-and-testing/): behavioural states, debug rendering and repeatable tests.

## How to read them

Distances are in Unreal Units (uu, where 1 uu = 1 cm) and speeds in uu/s, because that is what the game reports. I only convert to SI where a page says so. The constants come from community measurements, not from Psyonix, and each page says where. I ran the worked examples as tests against a numerical simulation, so the numbers quoted have been computed rather than estimated. Rocket League is a game by Psyonix, and this site isn't affiliated with it.
