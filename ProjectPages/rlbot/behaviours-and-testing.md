---
title: RL Bot, Behaviours and Testing
crumb: Behaviours and testing
permalink: /ProjectPages/rlbot/behaviours-and-testing/
type: explainer
section: rlbot
nav_order: 9
status: growing
applies: RLBot v4 Python API. The behaviour code is illustrative; testing is described as a plan, because the public repository has no test scenarios yet.
reviewed: 2026-10-14
description: >
  How to choose between behaviours without tangling target selection with button
  presses, what the public bot's structure teaches, and how to test a bot repeatably.
---

The maths on the other pages answers "how do I get there". This page is about the decision before that, "where should I be going?", and about how to find out whether a change made the bot better or just different.

## What the public bot does

The snapshot picks a behaviour by label and a target point from it:

- **chase the ball**, the default, with the ball's position as the target;
- **defend**, when the car is closer to its own goal than the ball is, targeting a point back towards that goal;
- **get off the wall**, when the car's position matches a hand-written wall region, targeting the floor beneath it;
- **track the ball in the future**, when the ball is more than 1,500 uu away, targeting where the framework's ball prediction says it will be one second ahead.

Separately, scripted flip sequences fire at kick-off and at set distances, with a cooldown based on the whole seconds of game time. The behaviour label is also drawn on screen, so it's easy to see which state the bot is in.

## What the structure taught me

Reading the public snapshot back, three things stand out, and they're useful whatever the bot looks like.

**Select one target per tick, in one place.** In the snapshot the flip logic and the target selection are chained into one `if / elif` ladder, so the target is only assigned on some branches and is read before it is assigned on others. A cleaner shape is a function that always returns a label and a target, with the flip decision made separately:

~~~python
def choose_behaviour(car, ball, team):
    """Illustrative: always returns (label, target), checked in priority order."""
    if on_wall(car.location):
        return 'get_off_wall', car.location.flat()
    if behind_the_ball(car.location.y, ball.location.y, team):
        return 'defend', point_between(ball.location, own_goal(team))
    if car.location.dist(ball.location) > 1500:
        return 'track_ball', ball_in_one_second(ball)
    return 'chase', ball.location
~~~

**Never hard-code a team.** The snapshot's attacking goal is the positive-y goal, which is right for blue only, and its defence check treats the positive-y goal as "my goal", which is right for orange only. Both come from using a literal team index. Derive the goal and the direction of play from the car's own team (blue defends −y, orange defends +y):

~~~python
def behind_the_ball(car_y, ball_y, team):
    """True when the car is between the ball and its own goal."""
    team_sign = 1.0 if team == 0 else -1.0
    return (car_y - ball_y) * team_sign < 0
~~~

I tested that function for both teams against the snapshot's hard-coded version.

**Keep a state's rules next to each other, with hysteresis.** A condition that flips as soon as a number crosses a threshold makes the bot dither at the boundary, for example between "chase" and "track" at exactly 1,500 uu. Add a margin (switch to track above 1,600, back to chase below 1,400) or a minimum time in a state.

## Debugging in-game

The in-game renderer is the fastest feedback loop there is. Draw the label, the target and the line to it (the [overview](/ProjectPages/rlbot/overview/) has the calls), and add anything you're unsure of: the approach point, the predicted ball position, the turning circle. If the line points at empty grass, the prediction or the frame conversion is wrong. If it flickers between two targets, the state is dithering.

## Testing repeatably

Watching a match tells you about the average case once. To compare a change you need the same situation many times.

**Put the game in a known state.** The bot's `rlbot.cfg` has `enable_state_setting = True`, which lets a script set the ball's and cars' positions, velocities and rotations directly. That makes a scenario like "ball at rest at (1000, 2000), car 3,000 uu away at 600 uu/s" repeatable. The RLBot documentation notes state setting isn't enabled in official tournaments, so it's a development tool, not something a competition bot can depend on.

**Write scenarios as tests.** The RLBotTraining package (the bot's `requirements.txt` already lists it) lets you define exercises with pass and fail conditions, such as "reach the ball within 4 seconds" or "the ball ends up in the goal", and run them in bulk. I haven't written any exercises yet, so this is how I'd approach it, not something the public repository does.

**Measure outcomes, not impressions.** For each run log the time to contact, boost spent, the contact angle and whether the ball went where intended, into a CSV. Then graph them with Matplotlib against the parameter you changed. If a scenario uses random starting positions, seed the random generator so a run can be replayed.

**Test the maths on its own.** Most of the formulae on these pages are pure functions of numbers, so they can be tested without the game. I ran the worked examples here as ordinary `unittest` tests: the guarded angle function, the arc-then-line path (by driving the path it returns and checking it lands on the target), the aerial solution (by simulating the boost step by step) and the team-aware defence check. They run in about a second and caught several of my own mistakes while writing these pages, including a wrong example target and a reversed sign convention.

*The code on this page is illustrative. The behaviour list describes the public snapshot as it stands.*
