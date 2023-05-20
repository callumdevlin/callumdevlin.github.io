---
layout: default
title: 3D Vector System
---

In order to help our bot read in the X, Y and Z coordinates from the game tick packet there is a Vector class, this can have functions added
to it in order to add, subtract, multiple etc different vectors together.
These vector functions are stored as a singular variable, we made this as list so each X,Y,Z value could still be accessed individually.

~~~python
class Vec3:
    __slots__ = [
        'x',
        'y',
        'z'
    ]
    def __init__(self, x: Union[float, 'Vec3', 'Vector3']=0, y: float=0, z: float=0):
        if hasattr(x, 'x'):
            self.x = float(x.x)
            self.y = float(x.y) if hasattr(x, 'y') else 0
            self.z = float(x.z) if hasattr(x, 'z') else 0
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
~~~

This is the basic code for the vector class
{:.figcaption}

Within this class there are function such as the add function, this allows us to pass in 2 vectors and find the sum:

~~~python
    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
~~~

## Distance
One of the most useful vectors we used is the distance vector:

~~~python
    def length(self):
            return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dist(self, other: 'Vec3') -> float:
            return (self - other).length()
~~~

This Returns the distance between this vector and another vector using pythagoras that's calculated in the 'Vec3.length()' function as it's passed through.

## Angles

When dealing with 3D space it is important to make sure the car is angled correctly when hitting the ball or finding out where things are. To find this out we use a vector function that can find the angle between 2 desired vectors and returns a value between 0 and pi:

~~~python
def ang_to(self, ideal: 'Vec3') -> float:
        cos_ang = self.dot(ideal) / (self.length() * ideal.length())      
        return math.acos(cos_ang)
~~~
