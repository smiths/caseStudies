import math
from numbers import Real
from typing import Any, Union
import collision
class Vec2:
    PI = 3.14159265358979323846
    def __init__(self, x=0, y=0, z=0, v=None):
        self.x = x
        self.y = y
        self.z = z

        if v != None:
            self.x = v.x
            self.y = v.y
    def __add__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x + other
            y = self.y + other
        else:
            x = self.x + other.x
            y = self.y + other.y
        return Vec2(x,y)
    def __sub__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x - other
            y = self.y - other
        else:
            x = self.x - other.x
            y = self.y - other.y
        return Vec2(x, y)
    def __mul__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x * other
            y = self.y * other
        else:
            x = self.x * other.x
            y = self.y * other.y
        return Vec2(x, y)
    def __rmul__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x * other
            y = self.y * other
        else:
            x = self.x * other.x
            y = self.y * other.y
        return Vec2(x, y)
    def __truediv__(self, other):
        types = (int, float)
        if isinstance(other, types):
            if other ==0:
                other=1
            x = self.x / other
            y = self.y / other
        else:
            x = self.x / other.x
            y = self.y / other.y
        return Vec2(x, y)
    def __str__(self):
        s = "({}, {})".format(round(self.x, 4), round(self.y, 4))
        return s
    def __eq__(self, other):
        if isinstance(other, Vec2):
            if self.x == other.x and self.y == other.y:
                return True
        return False
    def set(self, other):
        self.x = other.x
        self.y = other.y
    def reverse(self):
        return Vec2(-self.x, -self.y)
    def getX(self):
        return round(self.x, 2)
    def getY(self):
        return round(self.y, 2)
    def mag(self):
       return math.sqrt(self.x * self.x + self.y * self.y)

    def ln2(self):
        return self.dot(self, self)

    def ln(self):
        return math.sqrt(self.ln2())
    @classmethod
    def cross(cls, a, b):
        z = (a.x * b.y) - (a.y * b.x)
        return z

    @classmethod
    def dot(cls, a, b=None):
        if b == None:
            b=a
        return (a.x * b.x) + (a.y * b.y)
    @classmethod
    def normalize(cls, a):
        if a.mag() == 0:
            return Vec2(0,0)
        return Vec2(a.x/a.mag(), a.y/a.mag())
    @classmethod
    def rotate(cls, angle, v):
        angle = round(angle * math.pi/180, 5)
        return Vec2(round(v.x * math.cos(angle) - v.y * math.sin(angle),5),
                    round(v.x * math.sin(angle) + v.y * math.cos(angle),5))

    def to_vector(self):
        return collision.Vector(self.x, self.y)
    def to_list(self):
        return [self.x, self.y]
    @classmethod
    def copy(cls, other):
        return Vec2(other.x, other.y)

Vec2.DOWN = Vec2(0,1)
Vec2.UP = Vec2(0,-1)
Vec2.LEFT = Vec2(-1,0)
Vec2.RIGHT = Vec2(1,0)
Vec2.ZERO = Vec2(0,0)
Vec2.NONE = None