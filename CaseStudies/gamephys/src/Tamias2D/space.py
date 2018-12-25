from Tamias2D.vec2 import *
from Tamias2D.body import *
from Tamias2D.shapes import *
from Tamias2D.collision2d import *
import pygame
import collision
from Tamias2D.collision_util import *
class Space:
    def __init__(self):
        self.bodies = []
        self.gravity = 0


    def set_gravity(self, gravity_):
        if isinstance(gravity_, Vec2):
         self.gravity = gravity_
         for b in self.bodies:
             b.gravity = gravity_

    def add_body(self, body_):
        if isinstance(body_, Body):
            assert body_ not in self.bodies, "body already added to space"
            self.bodies.append(body_)
            body_.set_space(self)

    def get_bodies(self):
        return self.bodies

    def check_collision(self):
        i = 0
        while i < len(self.bodies):
            b = self.bodies[i]
            b.isBotCol = False
            i+=1
        i=0
        slop = 0.2
        while i < len(self.bodies):

            j=i+1
            b1 = self.bodies[i]
            while j < len(self.bodies):
                resp = Response()
                b2 = self.bodies[j]
                if (isinstance(b1.shape, Polygon) and isinstance(b2.shape, Box)) or (isinstance(b1.shape, Box) and isinstance(b2.shape, Polygon)):

                    _box = b2
                    _pol = b1
                    if isinstance(b1.shape, Box):
                        _box = b1
                        _pol = b2

                    if col_poly_poly(_pol.shape.colShape, _box.shape.colShape, resp):
                        should_res = True
                        if abs(resp.overlap) < slop:
                            if resp.overlap_n.x == 0.0 and resp.overlap_n.y > 0.0:
                                b1.isBotCol = True
                                should_res = False
                            if resp.overlap_n.x == 0.0 and resp.overlap_n.y < 0.0:
                                b2.isBotCol = True
                        if should_res:
                            CollisionHandler.resolve_collision(_pol, _box, resp)
                elif isinstance(b1.shape, Polygon) and isinstance(b2.shape, Polygon):
                    if col_poly_poly(b1.shape.colShape, b2.shape.colShape, resp):
                        CollisionHandler.resolve_collision(b1, b2, resp)
                elif isinstance(b1.shape, Circle) or isinstance(b2.shape, Circle):
                    #circle count
                    c = 0
                    #circle number if there's only one
                    cN = 0
                    if isinstance(b1.shape, Circle):
                        c +=1
                        cN=1
                    if isinstance(b2.shape, Circle):
                        c += 1
                        cN=2

                    if c==2:
                        if col_circle_circle(b1.shape.colShape, b2.shape.colShape, resp):
                            CollisionHandler.resolve_collision(b1, b2, resp)
                    else:
                        circle = b1
                        poly = b2
                        if cN ==2:
                            circle = b2
                            poly = b1
                        if col_poly_circle(poly.shape.colShape, circle.shape.colShape,resp):
                            CollisionHandler.resolve_collision(b1, b2, resp)


                j+=1
            i+=1

    def step(self, deltaTime):
        for b in self.bodies:
            b.update(deltaTime)
        self.check_collision()