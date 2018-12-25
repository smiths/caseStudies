from collision import *
from Tamias2D.body import *
from Tamias2D.shapes import *
from Tamias2D.vec2 import *
from Tamias2D.collision_util import *
import pygame
class CollisionHandler:
    def __init__(self):
        return
    @classmethod
    def resolve_collision(self, a, b, resp):
        self.pos_correction(a, b, resp)

        #relative velocity
        rv = b.velocity - a.velocity

        #relative velocity in terms of normal direciton
        normal = Vec2(resp.overlap_n.x, resp.overlap_n.y)

        velAlongNormal = Vec2.dot(rv, normal)
        # do not resolve if velocity is separating
        if (velAlongNormal > 0):
            return;
        both_are_polygons = False
        if isinstance(a.shape, Polygon) and isinstance(b.shape, Polygon):
            both_are_polygons = True
        # calculate restitution
        e = min(a.restitution, b.restitution)
        rniA = 0
        rniB = 0
        rA=0
        rB=0
        if both_are_polygons:
            n = poly_closest_intersection(a.shape.colShape, b.shape.colShape)
            if n is not None:
                rA = n - a.position
                rniA = Vec2.cross(rA, normal)
                rniA *= rniA
                rniA /= a.inertia

                rB = n - b.position
                rniB = Vec2.cross(rB, normal)
                rniB *= rniB
                rniB /= b.inertia

        # impulse scalar
        j = -(1 + e) * velAlongNormal
        j /= max((a.inv_mass+b.inv_mass), 1)
        # Apply impulse
        impulse = normal * j

        if a.bodyType == Body.DYNAMIC:
             a.velocity -= (impulse * a.inv_mass)
        if b.bodyType == Body.DYNAMIC:
             b.velocity += (impulse * b.inv_mass)
        self.rot_response(a, b, impulse, rA, rB, resp)




        if resp.overlap_n.x == 0.0 and resp.overlap_n.y > 0.0:
            a.isBotCol = True
        if resp.overlap_n.x == 0.0 and resp.overlap_n.y < 0.0:
            b.isBotCol = True
        resp.reset()

        if(a.bodyType == Body.STATIC or b.bodyType == Body.STATIC):
            stat = a
            dyn = b
            if(b.bodyType == Body.STATIC):
                stat = b
                dyn = a

            if self._is_intersecting_with(dyn, stat, resp):
                if both_are_polygons:
                    return False

        return True

    @classmethod
    def rot_response(self, a, b,impulse, rA, rB, resp):
        j = impulse
        if isinstance(a.shape, Polygon) and isinstance(b.shape, Polygon):
            tA = 0
            tB = 0
            if isinstance(rA, Vec2) or isinstance(rA, Vector):
                if a.bodyType == Body.DYNAMIC:
                    tA = (1.0 / a.inertia) * Vec2.cross(rA, j)
                if b.bodyType == Body.DYNAMIC:
                    tB = (1.0 / b.inertia) * Vec2.cross(rB, j)

                a.angularVel += tA
                b.angularVel -= tB
                return
        elif isinstance(a.shape, Circle) or isinstance(b.shape, Circle):
            if isinstance(a.shape, Polygon) or isinstance(b.shape, Circle):
                circle = a if isinstance(a.shape, Circle) else b
                p = b if isinstance(b.shape, Polygon) else a
                dir = Vec2.normalize(Vec2(v = p.position - circle.position))
                n = circle.position + (dir*circle.shape.radius)
                rC = circle.position - n
                rP = p.position - n
                if a.bodyType == Body.DYNAMIC:
                    tC = (1.0 / a.inertia) * Vec2.cross(rC, j)
                    circle.angularVel += tC
                if b.bodyType == Body.DYNAMIC:
                    tP = (1.0 / b.inertia) * Vec2.cross(rP, j)
                    p.angularVel -= tP
                    return






    @classmethod
    def _get_contact_point(cls, a, b, resp):
        colPoint = Vec2.ZERO
        if b.bodyType == Body.DYNAMIC:
            if isinstance(a.shape, Polygon) or isinstance(a.shape, Box):
                aPoints = a.shape.colShape.points
                for p in aPoints:
                    if isinstance(b.shape, Polygon) or isinstance(b.shape, Box):
                        if point_in_poly(p, b.shape.colShape):
                            colPoint = p
                    else:
                        if point_in_circle(p, b.shape.colShape):
                            colPoint = p
        success = False
        if colPoint != Vec2.ZERO:
            colPoint = colPoint - resp.overlap_v
            success = True
        return success, colPoint
    @classmethod
    def _get_col_point(cls, a, b):
        colPoint = a.position
        if b.bodyType == Body.DYNAMIC:
            if isinstance(a.shape, Polygon) or isinstance(a.shape, Box):
                aPoints = a.shape.colShape.points
                for p in aPoints:
                    if isinstance(b.shape, Polygon) or isinstance(b.shape, Box):
                        if point_in_poly(p, b.shape.colShape):
                            colPoint = p
                    else:
                        if point_in_circle(p, b.shape.colShape):
                            colPoint = p
        return colPoint

    @classmethod
    def _is_intersecting_with(self, a, b, resp=None):
        if isinstance(a.shape, Circle) and isinstance(b.shape, Circle):
            return col_circle_circle(a,b, resp)
        elif isinstance(a.shape, Polygon) and isinstance(b.shape, Polygon):
            return col_poly_poly(a.shape.colShape, b.shape.colShape, resp)
        elif isinstance(a.shape, Circle) or isinstance(b.shape, Circle):
            circle = a.shape.colShape
            poly = b.shape.colShape
            if isinstance(b.shape, Circle):
                circle = b.shape.colShape
                poly = a.shape.colShape
            return test_circle_poly(circle,poly, resp)
        return  False
    @classmethod
    def pos_correction(self, a, b, resp):
        percent = 1
        slop = 0.3
        penetration = Vec2(abs(resp.overlap_v.x), abs(resp.overlap_v.y)).mag() - slop

        if penetration < 0:
            return
        if a.bodyType == Body.STATIC or b.bodyType == Body.STATIC:
            percent = 1.4

        correction = (penetration / (a.inv_mass + b.inv_mass)) * percent * (Vec2(resp.overlap_n.x, resp.overlap_n.y))
        if a.bodyType == Body.DYNAMIC:
            a.position -= correction * a.inv_mass
        if b.bodyType == Body.DYNAMIC:
            b.position += correction * b.inv_mass

