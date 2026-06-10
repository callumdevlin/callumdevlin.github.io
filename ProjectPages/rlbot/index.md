---
title: Rocket League Bot
permalink: /ProjectPages/rlbot/
description: >
  Notes from building a hard-coded Rocket League bot in Python — game-space
  vectors, ground and aerial kinematics, path planning and shot alignment.
---

Notes from building a Rocket League bot in Python using the [RLBot framework](https://rlbot.org). The bot is hard-coded rather than machine-learned — every behaviour is explicit maths and logic — which makes the project a nice excuse to work through the game's physics properly. These pages document that maths so it's useful to anyone building their own bot.

The bot's source code is on [GitHub](https://github.com/callumdevlin/RL-Bot).

## Sections

1. [**Project Overview**](/ProjectPages/rlbot/overview/) — what the RLBot framework provides, how the bot is structured, and the in-game debug rendering used during development.
2. [**3D Vector System**](/ProjectPages/rlbot/vectors/) — the `Vec3` class underpinning everything: distances, angles and dot products in game space.
3. [**Ground Kinematics**](/ProjectPages/rlbot/ground-kinematics/) — how the car accelerates, brakes, coasts and boosts on the ground, with the values that govern each.
4. [**Aerial Kinematics**](/ProjectPages/rlbot/aerial-kinematics/) — solving for the orientation and boost needed to reach a point in the air at a given time.
5. [**Aligning Shots on Target**](/ProjectPages/rlbot/aligning-shots/) — hitting the ball is easy; hitting it *towards the goal* needs an offset approach point.
6. [**Path Optimisation Analysis**](/ProjectPages/rlbot/movingpath/) — turning radius vs speed, and estimating time-to-target along realistic paths.
