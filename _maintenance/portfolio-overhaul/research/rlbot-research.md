# Rocket League bot: research record (accessed 2026-10-14)

Produced by a research agent that read the public bot repository (a shallow clone, read-only, never executed) and community sources. The agent could not save its own file, so this is a condensed copy of its hand-back. Labels: **[DOC]** RLBot project docs/source (community-run, not Psyonix); **[COMM]** community-measured (Sam Mish / RLUtilities, RocketSim, RLGym); **[DERIV]** the agent's own computation; **[UNVERIFIED]** a source could not be opened. Key numeric claims are re-checked by `tools/rlbot_maths_tests.py`.

## The public bot repository

- `github.com/callumdevlin/RL-Bot`, branch `main`, head 846918ca "removed behaviour garbage" (6 Aug 2023). 716 lines of Python. `requirements.txt` is `rlbot==1.*`, `rlbot_gui`, `rlbottraining`.
- README: "Developed by Callum Devlin and Daniel McMurray. Rocket League bot coded in python." Daniel McMurray authored several commits.
- **It cannot run as committed.** `bot.py` imports a `behaviours` module that was deleted (only a stale Python 3.7 `.pyc` remains). If that were fixed, `target_location` is read before assignment (UnboundLocalError) and `car` is undefined (NameError). `get_output` returns a `Vec3` on one branch.
- **No offset approach point, arc-line path, curvature table, time estimator, intercept search, aerial solver or physics constants (1600/3500/525/991/1410/2300) appear anywhere.** `ang_to` is not used on any live path.
- What it does: template P-steering `clamp(5*atan2(rel.y, rel.x))`, throttle always 1, boost whenever boost is non-zero, scripted flip sequences, a string "behaviour" label, a fixed 1 s ball-prediction look-ahead.
- `middle_of_goal` uses `642.775//2` = 321.0 (true half-height 321.3875). `get_target_direction` calls `ang_to` on two position vectors (angle between vectors from the world origin, not the direction to the target). `fix_ang` and `is_closer_to_goal_than` lack `self`/`@staticmethod`. `fix_ang`'s docstring contains an expletive.
- Template: `vec.py` (`Vec3`, `ang_to`), `orientation.py`, `drive.py`, `sequence.py`, `boost_pad_tracker.py`, `ball_prediction_analysis.py` and the structure of `bot.py` come from RLBotPythonExample (MIT, "Copyright (c) 2018", holder blank). The repo's LICENSE is the same MIT text. Compared function by function through a fetch tool, not byte-diffed. Original to the repo: `target_tracker.py`, `teamcheck.py`, `car_movements.py`, `fix_ang`, `is_closer_to_goal_than`, the flip scripts, `on_wall`.

## Framework version

- PyPI `rlbot` 1.x is RLBot **"v4"** (latest 1.68.0, 2 Jun 2024, Python 3.6+). **v5** is pre-release (`rlbot` 2.0.0bNN, to 2.0.0b56 on 2 Oct 2026) with a different API: `Bot`/`ControllerState` instead of `BaseAgent`/`SimpleControllerState`, `GamePacket` (`players`, `boost_pads`, `balls`, `match_info`) instead of `GameTickPacket`, `.toml` configs, fractional (0-1) 2D draw coordinates with begin/end rendering, 120 Hz only, C# server over TCP + FlatBuffers (no DLL).
- v4 communication: Rocket League <-> `RLBot.exe` (core) <-> `RLBotInterface.dll` <-> Python bot processes (`BotManager` polls a packet, calls `get_output()`, returns the controller state). rlbot.org/faq: bots talk through sockets ("previously shared memory"); the `-rlbot` launch flag "simultaneously disables all online play". The meaning of `RLBot_ControllerURL` is not documented [UNVERIFIED that it is where the game connects].
- Tick rate: physics 120 Hz; the Python default is 60; this bot's `bot.cfg` requests 120. Ball prediction is about 6 s at 60 slices/s in v4.
- Coordinates [DOC]: Z up; x is "left" (not the usual Cartesian layout); team 0 (blue) defends -y and attacks +y; yaw 0 on +x, increasing clockwise; Euler order YZX; 1 uu = 1 cm. [DERIV] the template's forward/right/up vectors are orthonormal and (forward x right).up = +1, so the world is **left-handed**. Positive relative y means the target is on the right, so atan2 > 0 means steer right.
- Field: walls x = +/-4096, y = +/-5120 (back of net |y| = 6000); goal height 642.775, centre-to-post 892.755, depth 880. Ceiling 2044 (older wiki, RLGym) or 2048 (current wiki, RocketSim). **Ball radius 92.75** (older wiki, template) or **91.25** (current RLBot wiki, RocketSim, RLGym; resting z 93.15): cite which.
- Octane hitbox (RocketSim) 120.507 x 86.6994 x 38.6591, offset (13.8757, 0, 20.755) [COMM]; the car's packet origin is about 73-74 uu behind the nose. Resting origin height 17.01 [DOC].

## Physics constants (community-measured)

Sources: Sam Mish (smish.dev/rocket_league: ground_control, aerial_hit, aerial_control, path_analysis), RLUtilities `drive.cc`/`aerial.cc`/`car.cc`, RocketSim `RLConst.h`/`CarConfig.cpp`, RLGym game values, RLBot wiki "Useful game values" and "Jumping physics".

| Quantity | Value | Notes |
| --- | --- | --- |
| Throttle acceleration | 1600 uu/s^2 at 0, linearly to 160 at 1400 uu/s, to 0 at 1410 uu/s | RLUtilities `throttle_accel`; not constant |
| Brake deceleration | 3500 uu/s^2 | |
| Coast deceleration | 525 uu/s^2 | RocketSim: 0.15 x 3500 |
| Boost acceleration, ground | 991.667 uu/s^2 | added on top of throttle acceleration (boosting forces throttle 1): 2591.7 at rest |
| Boost acceleration, air | about 1058 uu/s^2 | RocketSim 3175/3; RLUtilities 1060; Mish ~1000 |
| Gravity | 650 uu/s^2 (-z) | |
| Max car speed | 2300 uu/s (82.8 km/h); supersonic 2200; throttle-only 1410 | |
| Boost use | 33.33 per second (3 s for a full tank) | RLUtilities comment says 30 "???" |
| Max angular velocity | 5.5 rad/s | |
| Air control, full input | pitch 12.15, yaw 8.92, roll 36.08 rad/s^2 (damping 2.80 / 1.89 / 4.47 per second) | Mish, fitted; RocketSim agrees within 1-6.5% |
| Jump | impulse about 292 uu/s, hold acceleration about 1460 for up to 0.2 s, dodge window 1.25 s | |

**Turning curvature table** (RLUtilities `Drive::max_turning_curvature`, linear interpolation; radius = 1/curvature is derived):

| Speed (uu/s) | Curvature (1/uu) | Radius (uu) | Radius (m) |
| ---: | ---: | ---: | ---: |
| 0 | 0.00690 | 144.9 | 1.45 |
| 500 | 0.00398 | 251.3 | 2.51 |
| 1000 | 0.00235 | 425.5 | 4.26 |
| 1500 | 0.00138 | 724.6 | 7.25 |
| 1750 | 0.00110 | 909.1 | 9.09 |
| 2300 | 0.00088 | 1136.4 | 11.36 |

So the minimum radius at the speed cap is about 1,136 uu, i.e. **11 m, not "a kilometre"** (1 km = 100,000 uu), and at rest it is about 1.45 m, not "on the spot". RocketSim's steer-angle curve agrees to about 10%.

## Aerial maths

The page's formula `B0 f* = 2/(T-dt)^2 (P - x0 - v0 dt - 1/2 g dt^2 z)` is wrong as written. Mish's source (aerial_hit) uses dt as the total time to contact and T as the turn time, so his numerator has the total time and the denominator the boost duration. The page swapped the symbols, putting the elapsed time in the numerator. Correct form, with g = -650 signed, state at t = 0, boost starting at t_b and arrival at T:

`A = 2/(T - t_b)^2 * (P - x0 - v0*T - 1/2*g*T^2*z_hat)`, with B0 = |A| and f* = A/|A|.

Re-solving at elapsed time dt with the current state (x1, v1) and tau = T - dt: `A = 2/tau^2 (P - x1 - v1*tau - 1/2*g*tau^2*z_hat)`. The agent's simulation: the page formula misses by 1,525-1,992 uu; the corrected form by under 1e-3 uu. Worked example: x0 = (0,0,300), v0 = (800,0,300), P = (1800,0,700), T = 2 s, t_b = 0.4 s gives A = (156.25, 0, 859.37), |A| = 873.5 (83% of 1058). The test script reproduces this.

## `ang_to` failure cases

`acos(a.b / (|a||b|))`: ZeroDivisionError for a zero vector; `ValueError: math domain error` when the cosine rounds to 1.0000000000000002, which happens for about 24% of random exactly-parallel pairs (so when the car is lined up). It is unsigned: (1,1,0) and (1,-1,0) both give 0.7854 from forward (1,0,0). Fix: clamp the cosine to [-1,1], guard zero length, and use `atan2` on local coordinates when the sign matters.

## Suggested additions (from the agent), and what was done

1. Tick loop, time and units; 2. coordinates, rotations, world-to-local, signed angle (atan2 vs acos); 3. steering as P control and the orbit trap; 4. speed control and numerical time-to-target; 5. intercepting a moving ball; 6. behaviour state machine; 7. air control and the re-orientation time budget; 8. debugging and repeatable testing. Rejected: generic Python tutorials and any page presenting a capability the public repository lacks, unless framed as maths.

Unresolved: byte-identity with the template; fork relationship to `bluesloth3109/RL-Bot`; meaning of `RLBot_ControllerURL`; whether v1 wraps `get_output` in begin/end rendering automatically; car air drag; the v5 `rlbot` 5.0.0 vs 2.0.0bNN numbering; RocketSim flip-constant semantics.
