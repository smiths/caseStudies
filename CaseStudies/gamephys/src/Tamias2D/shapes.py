import abc
import collision

from Tamias2D.vec2 import *
class Shape(object):
    __metaclass__ = abc.ABCMeta
    def set_angle(self, angle_):
        self.angle = angle_
        self.colShape.angle = angle_

    def set_pos(self, pos_):
        self.pos = pos_
        self.colShape.pos = collision.Vector(pos_.x, pos_.y)

    def get_center(self):
        return self.colShape.get_centroid()

    def get_width(self):
        return 0

    def get_height(self):
        return 0

    def _get_support(self, dir):
        best_proj = -math.inf
        best_point = 0

        for i in range(len(self.colShape.rel_points)):
            p = self.colShape.rel_points[i]
            proj = Vec2.dot(p, dir)
            if proj > best_proj:
                best_point = i
                best_proj = proj
        return best_point


class Polygon(Shape):
    def __init__(self, pos_, verts_, angle_=0):
        self.verts = verts_
        self.pos = pos_
        self.angle = angle_
        self.colShape = collision.Poly(pos_, verts_, 0)
        self.originalShape = self.colShape.base_points.copy()
        self._determine_shape_info()
        self.colShape.angle = angle_

    def _determine_shape_info(self):
        lowest = Vec2(math.inf,math.inf)
        highest = Vec2(-math.inf,-math.inf)
        for p in self.colShape.points:
            if p.x < lowest.x:
                lowest.x = p.x
            if p.y < lowest.y:
                lowest.y = p.y
            if p.x > highest.x:
                highest.x = p.x
            if p.y > highest.y:
                highest.y = p.y
        self.width = abs(highest.x - lowest.x)
        self.height = abs(highest.y - lowest.y)
        self.originalCenter = self.get_center()
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height


    def get_verts(self):
        return self.colShape.points

    def vertsAsList(self):
        _verts = []
        for v in self.get_verts():
            _v = [v.x, v.y]
            _verts.append(_v)
        return _verts
    def set_angle(self, angle_):
        dAngle = angle_ -  self.angle
        if dAngle == 0:
            return
        self.angle = angle_
        xDir=1
        if dAngle < 0:
            xDir = -1
        try:
            self.points
        except AttributeError:
            self.points = None
        if self.points == None:
            self.points = self.originalShape.copy()

        points = self.points
        original = self.originalShape

        support_i = self._get_support(Vec2.normalize(Vec2(xDir/5, 1)))
        support_p = original[support_i]
        #to rotate around support point, we first move everything then we move them back after rotation
        temp_move_by = Vec2(self.originalCenter.x, self.originalCenter.y)
        restorePos = original[support_i] - (original[support_i]-temp_move_by)
        for i in range(len(original)):
            p = Vec2.copy(original[i])
            p = p - temp_move_by
            p = p.rotate(angle_, p)
            p += restorePos
            points[i]=p
        self.colShape.set_points(points)





class Box(Polygon):
    def __init__(self, min_, max_, angle_=0):
        if isinstance(min_, Vec2) and isinstance(max_, Vec2) and isinstance(angle_, (int,float)):
            self.min = min_
            self.max = max_
            self.angle = angle_
            self.colShape = collision.Poly.from_box((min_+max_)/2 , max_.x - min_.x, max_.y - min_.y )
            self.originalShape = self.colShape.base_points.copy()
            self._determine_shape_info()
            self.colShape.angle = angle_



class Circle(Shape):
    def __init__(self, position, radius):
        self.colShape = collision.Circle(position, radius)
        self.pos = position
        self.radius = radius

    def get_center(self):
        return self.pos

    def get_width(self):
        return self.radius*2
    def get_height(self):
        return self.radius*2

