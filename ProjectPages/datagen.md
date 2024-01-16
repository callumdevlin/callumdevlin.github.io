---
layout: default
title: Synthetic Data Generation
---
This project was part of a hackathon for Thales and the aim was to develop a method to generate realistic synthetic images of industrial components from their CAD models and use them to train a machine learning model for automated inspection. The goal is to reduce the time and cost of training the machine learning model, and to enable automated inspection in low volume high mix industrial environments.

## Blender API
Taking advantage of Blender's open-source API allows you to create and execute Python scripts. This enables us to automate and customize various aspects of 3D model editing within Blender. By running scripts inside blender, you can efficiently perform tasks such as modifying geometry, adjusting textures, creating objects, and more, all through programmatic control of Blender's features.

## Creating the synthetic images
When planning i tried to think of component defects that there could be with an product coming along a production line, such as:
- Imperfections/scratches/dents
- Missing Components
- PCB Errors

The aim was to create a script to take the product and randomly apply these defects, then render it with random lighting and camera angles to give the ML model a large data set.



## Creating Lights
...

##Creating Surface Defects
In blender there is a feature called texture painting, This lets you 'draw' on an object and will create a displaced normal on the object. You can use this to create scratches, dents or imperfections on faces.
I would also use a feature to hide and move around some objects at random to emulate them being missing or wrongly placed.
