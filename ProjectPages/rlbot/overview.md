---
title: Rocket League Bot, Project Overview
crumb: Overview
permalink: /ProjectPages/rlbot/overview/
type: explainer
section: rlbot
nav_order: 1
image: /Images/optimised/rlbot-hero-1200.webp
applies: RLBot v4 (the `rlbot` 1.x Python package); RLBot v5 has a different API.
reviewed: 2026-10-14
description: >
  What the RLBot framework provides, how the bot is structured, what it does today
  and the in-game debug rendering used during development.
---

{% include figure.html src="/Images/rlbot-hero.jpg" alt="In-game screenshot of a blue and black Octane-style car with its boost flame lit, driving across a Rocket League arena floor" caption="An in-game screenshot of a car boosting. Rocket League is a game by Psyonix; this site is not affiliated with it." eager=true %}

The goal of this project was a bot that plays Rocket League by itself, written in Python on top of the [RLBot framework](https://rlbot.org). Daniel McMurray and I wrote it together, and these notes are my write-up of the maths. The bot is hard-coded, with no machine learning, and has a simple behavioural state system for choosing what to do. That constraint is deliberate: every behaviour has to be expressed as explicit maths, which is what these notes document.

## The RLBot framework

RLBot is a community-built framework that makes custom bots possible. Rocket League has a bot API built into the game, and launching the game with the `-rlbot` flag enables it. The framework's FAQ says that flag also disables all online play, so bots can't take part in online matches.

In the v4 framework the bot uses, the game talks to the RLBot core, which hands each bot process a snapshot of the game every tick: positions, velocities and rotations for the ball and every car, plus boost and match state. In the Python API that snapshot is a `GameTickPacket`. The core also carries the bot's controls (throttle, steer, boost, jump and so on) back into the game, and the framework's FAQ says the core and bots communicate over sockets.

From the bot's point of view the whole game reduces to a loop: receive the packet, decide what to do, return a controller state. Everything else in these notes (vectors, kinematics, path maths) lives inside that "decide" step.

## What the bot does today

The prototype follows the RLBot Python template. Each tick it reads the packet, computes a steering input towards a target point with a proportional controller, holds full throttle, boosts whenever it has boost, and triggers scripted flip sequences at kick-off and at set distances. A behaviour label (chase the ball, defend, get off the wall, track the ball a second ahead) picks the target, using the framework's built-in ball prediction for the look-ahead.

## Running the prototype

The repository has no run instructions of its own. It is an RLBot v4 bot configured through `bot.cfg`, with `rlbot==1.*`, `rlbot_gui` and `rlbottraining` in `requirements.txt`. As committed it won't start: `bot.py` imports a `behaviours` module that is no longer in the repository, so that module has to be restored or rewritten first.

## Debug rendering

To see what the bot is thinking while it plays, RLBot provides draw functions for overlaying text and 3D geometry in the game itself. I use these constantly while developing. The snippets below are from the bot, written for the v4 Python API; check the rendering documentation for your framework version, since v5 changes the calls.

Text overlays for live variables:

~~~python
self.renderer.draw_string_2d(50, 50, 1, 1, f'Player co-ords: {car_location}', self.renderer.white())
self.renderer.draw_string_2d(50, 70, 1, 1, f'Speed: {car_velocity.length():.1f}', self.renderer.white())
self.renderer.draw_string_2d(50, 90, 1, 1, f'Dist. to ball: {distance_to_ball:.1f}', self.renderer.white())
self.renderer.draw_string_2d(50, 110, 1, 1, f'Behaviour: {self.behaviour}', self.renderer.white())
~~~

And 3D lines and shapes to show targets and orientation at a glance:

~~~python
# Draw a line to the target location and a rectangle on the target
self.renderer.draw_line_3d(car_location, target_location, self.renderer.white())
self.renderer.draw_rect_3d(target_location, 8, 8, True, self.renderer.cyan(), centered=True)

# Draw goal locations
self.renderer.draw_line_3d(car_location, enemy_goal, self.renderer.orange())
self.renderer.draw_line_3d(car_location, my_goal, self.renderer.blue())
~~~

Watching the white target line swing round while the behaviour label changes is the fastest way I know to spot logic bugs, far faster than reading logs.
