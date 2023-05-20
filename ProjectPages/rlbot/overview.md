---
layout: default
title: Project Overview

---

![RLBOT](/Images/rlbot.JPG){:.lead width="800" height="100" loading="lazy"}


Check out this project on Github here
{:.figcaption}


- The basis of the project was to make a Bot that would play Rocket League itself, this was coded in Python using the [RL Bot GUI API](https://rlbot.org). It is hard coded (Not AI based) and has its own implemented behavioural system to help make smart decisions.

## RL BOT GUI
- This is a community driven API that is built for multiple languages, RLBot enables custom bots in Rocket League and helps pull game data from a game into readable values. 

-   RLBot uses an API in Rocket League specifically made for us. This API is activated when the game is launched with the '-rlbot' flag, which simultaneously disables all online play. The RLBotCore dll communicates with the game through this API and this is where most of the magic happens. Communication with bots are done through sockets (shared memory in the past) which allow us to support a wide range of languages.

## Behaviour System
