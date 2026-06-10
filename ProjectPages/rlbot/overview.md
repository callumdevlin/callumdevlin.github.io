---
title: RL Bot — Project Overview
permalink: /ProjectPages/rlbot/overview/
image: /Images/rlbot-hero.jpg
description: >
  What the RLBot framework provides, how the bot is structured, and the
  in-game debug rendering used during development.
---

![RL Bot in action](/Images/rlbot-hero.jpg){:.lead loading="lazy"}

Check out this project on [GitHub](https://github.com/callumdevlin/RL-Bot).
{:.figcaption}

The goal of this project was to build a bot that plays Rocket League by itself, written in Python on top of the [RLBot framework](https://rlbot.org). The bot is hard-coded — there's no machine learning involved — with its own behavioural state system to make decisions about when to attack, defend, collect boost and so on. That constraint is deliberate: every behaviour has to be expressed as explicit maths, which is exactly what these notes document.

## The RLBot Framework

RLBot is a community-built framework that makes custom bots possible. Psyonix added a dedicated bot API to Rocket League for the project: launching the game with the `-rlbot` flag enables it (and disables online play at the same time, so bots can never touch ranked matches). Through that API, the framework's core reads live game state — positions, velocities and rotations for the ball and every car — and exposes it to your bot as a structured "game tick packet" each frame, while carrying your control inputs (throttle, steer, boost, jump…) back into the game. Bots talk to the framework over sockets, which is what lets people write them in Python, C++, Rust and several other languages against the same interface.

From the bot's point of view, the whole game reduces to a loop: receive the tick packet, decide what to do, return a controller state. Everything else on these pages — vectors, kinematics, path maths — lives inside that "decide" step.

## Debug Rendering

To see what the bot is "thinking" while it plays, RLBot provides draw functions for overlaying text and 3D geometry in the game itself. I use these constantly during development.

Text overlays for live variables:

~~~python
self.renderer.draw_string_2d(50, 50, 1, 1, f'Player co-ords: {car_location}', self.renderer.white())
self.renderer.draw_string_2d(50, 70, 1, 1, f'Speed: {car_velocity.length():.1f}', self.renderer.white())
self.renderer.draw_string_2d(50, 90, 1, 1, f'Dist. to ball: {distance_to_ball:.1f}', self.renderer.white())
self.renderer.draw_string_2d(50, 110, 1, 1, f'Behaviour: {self.behaviour}', self.renderer.white())
~~~

And 3D lines and shapes to show targets and orientation at a glance:

~~~python
# Draw line to target location and a rectangle on the target
self.renderer.draw_line_3d(car_location, target_location, self.renderer.white())
self.renderer.draw_rect_3d(target_location, 8, 8, True, self.renderer.cyan(), centered=True)

# Draw goal locations
self.renderer.draw_line_3d(car_location, enemy_goal, self.renderer.orange())
self.renderer.draw_line_3d(car_location, my_goal, self.renderer.blue())
~~~

Watching the white target line swing around while the behaviour label changes is the fastest way to spot logic bugs — far faster than reading logs. I'm also working on exporting match data to Matplotlib so the bot's performance can be graphed against different variables between runs.

*Next: the [3D vector system](/ProjectPages/rlbot/vectors/) everything else is built on.*
