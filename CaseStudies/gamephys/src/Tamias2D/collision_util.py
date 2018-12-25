import math
from numbers import Real
from typing import Any, Union
from Tamias2D.vec2 import Vec2
import collision
LEFT_VORONOI_REGION = -1
MIDDLE_VORONOI_REGION = 0
RIGHT_VORONOI_REGION = 1
ALLOWED_NUM_TYPES = (int, float)

def flatten_points_on(points, normal, result):
    minpoint = math.inf
    maxpoint = -math.inf

    for i in range(len(points)):
        dot = points[i].dot(normal)
        if dot < minpoint:
            minpoint = dot
        if dot > maxpoint:
            maxpoint = dot

    result[0] = minpoint
    result[1] = maxpoint


def is_separating_axis(a_pos, b_pos, a_points, b_points, axis, response=None):
    range_a = [0, 0]
    range_b = [0, 0]

    offset_v = b_pos - a_pos

    projected_offset = offset_v.dot(axis)

    flatten_points_on(a_points, axis, range_a)
    flatten_points_on(b_points, axis, range_b)

    range_b[0] += projected_offset
    range_b[1] += projected_offset

    if range_a[0] > range_b[1] or range_b[0] > range_a[1]:
        return True

    if response:

        overlap = 0

        if range_a[0] < range_b[0]:
            response.a_in_b = False

            if range_a[1] < range_b[1]:
                response.b_in_a = False

            else:
                option_1 = range_a[1] - range_b[1]
                option_2 = range_b[1] - range_a[1]
                overlap = option_1 if option_1 < option_2 else option_2

        else:
            response.b_in_a = False

            if range_a[1] > range_b[1]:
                overlap = range_a[0] - range_b[1]
                response.a_in_b = False

            else:
                option_1 = range_a[1] - range_b[0]
                option_2 = range_b[1] - range_a[0]

                overlap = option_1 if option_1 < option_2 else option_2

        abs_overlap = abs(overlap)
        if abs_overlap > 0 and abs_overlap < response.overlap:
            response.overlap = abs_overlap
            response.overlap_n.set(axis)
            if overlap < 0:
                response.overlap_n = response.overlap_n.reverse()
    return False


def voronoi_region(line, point):
    dp = point.dot(line)

    if dp < 0:
        return LEFT_VORONOI_REGION
    elif dp > line.ln2():
        return RIGHT_VORONOI_REGION
    return MIDDLE_VORONOI_REGION

def col_poly_poly(a, b, response=None):
    a_points = a.rel_points
    b_points = b.rel_points
    a_pos = a.pos
    b_pos = b.pos

    for n in a.normals:
        if is_separating_axis(a_pos, b_pos, a_points, b_points, n, response):
            return False
    for n in b.normals:
        if is_separating_axis(a_pos, b_pos, a_points, b_points, n, response):
            return False
    if response:
        response.a = a
        response.b = b
        response.overlap_v = response.overlap_n * response.overlap
    return True
def col_poly_circle(polygon, circle, response = None):
    circle_pos = circle.pos - polygon.pos
    radius = circle.radius
    radius2 = radius * radius
    points = polygon.rel_points
    ln = len(points)

    for i in range(ln):
        nextn = 0 if i == ln - 1 else i + 1
        prevn = ln - 1 if i == 0 else i - 1

        overlap = 0
        overlap_n = None

        edge = polygon.edges[i].copy()
        point = circle_pos - points[i]

        if response and point.ln2() > radius2:
            response.a_in_b = False

        region = voronoi_region(edge,point)

        if region == LEFT_VORONOI_REGION:
            edge.set(polygon.edges[prevn])

            point2 = circle_pos - points[prevn]

            region = voronoi_region(edge, point2)

            if region == RIGHT_VORONOI_REGION:

                dist = point.ln()

                if dist > radius:
                    return False

                elif response:
                    response.b_in_a = False
                    overlap_n = point.normalize()
                    overlap = radius - dist

        elif region == RIGHT_VORONOI_REGION:
            edge.set(polygon.edges[nextn])
            point = circle_pos - points[nextn]
            region = voronoi_region(edge,point)

            if region == LEFT_VORONOI_REGION:
                dist = point.ln()

                if dist > radius:
                    return False

                elif response:
                    response.b_in_a = False
                    overlap_n = point.normalize()
                    overlap = radius - dist

        else:

            normal = edge.perp().normalize()

            dist = point.dot(normal)

            dist_abs = abs(dist)

            if dist > 0 and dist_abs > radius:
                return False

            elif response:
                overlap_n = normal
                overlap = radius - dist

                if dist >= 0 or overlap < 2 * radius:
                    response.b_in_a = False

        if overlap_n and response and abs(overlap) < abs(response.overlap):
            response.overlap = overlap
            response.overlap_n.set(overlap_n)

    if response:
        response.a = polygon
        response.b = circle
        response.overlap_v = response.overlap_n * response.overlap

    return True
def col_circle_circle(a, b, response = None):

    difference_v = b.pos - a.pos
    total_radius = a.radius + b.radius
    total_radius_sq = total_radius * total_radius
    distance_sq = difference_v.ln2()

    if distance_sq > total_radius_sq:
        return False

    if response:
        dist = math.sqrt(distance_sq)
        response.a = a
        response.b = b
        response.overlap = total_radius - dist
        if difference_v.ln2() != 0:
            response.overlap_n = difference_v.normalize()
            response.overlap_v = response.overlap_n * response.overlap
        else:
            response.overlap_n = Vec2(0, 1)
            response.overlap_v = Vec2(0, response.overlap)
        response.a_in_b = a.radius <= b.radius and dist <= b.radius - a.radius
        response.b_in_a = b.radius <= a.radius and dist <= a.radius - b.radius

    return True
def point_in_poly(p, poly):
    resp = collision.Response()
    point = collision.Poly(collision.Vector(0, 0), [collision.Vector(0, 0), collision.Vector(0.0000001, 0.0000001)])
    point.pos = p
    result = col_poly_poly(point, poly, resp)

    if result:
        return resp.a_in_b

    return result
def is_equal(a, b):
    return abs(a-b) < 0.000001

def line_intersection_point(l1p1, l1p2, l2p1, l2p2):
    A1 = l1p2.y - l1p1.y
    B1 = l1p1.x - l1p2.x
    C1 = A1 * l1p1.x + B1 * l1p1.y

    A2 = l2p2.y - l2p1.y
    B2 = l2p1.x - l2p2.x
    C2 = A2 * l2p1.x + B2 * l2p1.y
    det = A1 * B2 - A2 * B1
    if is_equal(det, 0):
        return None
    else:
        x = (B2 * C1 - B1 * C2) / det
        y = (A1 * C2 - A2 * C1) / det
        online1 = ((min(l1p1.x, l1p2.x) < x or is_equal(min(l1p1.x, l1p2.x), x)) and
        (max(l1p1.x, l1p2.x) > x or is_equal(max(l1p1.x, l1p2.x), x)) and
        (min(l1p1.y, l1p2.y) < y or is_equal(min(l1p1.y, l1p2.y), y)) and
        (max(l1p1.y, l1p2.y) > y or is_equal(max(l1p1.y, l1p2.y), y)))

        online2 = ((min(l2p1.x, l2p2.x) < x or is_equal(min(l2p1.x, l2p2.x), x))
        and (max(l2p1.x, l2p2.x) > x or is_equal(max(l2p1.x, l2p2.x), x))
        and (min(l2p1.y, l2p2.y) < y or is_equal(min(l2p1.y, l2p2.y), y))
        and (max(l2p1.y, l2p2.y) > y or is_equal(max(l2p1.y, l2p2.y), y)))

        if online1 and online2:
            return Vec2(x,y)
    return None
def poly_line_intersection_points(l1p1, l1p2, polygon):
    intersection_points = []
    #overlap = option_1 if option_1 < option_2 else option_2
    points = polygon.points
    for i in range(len(points)):
        next = i + 1 if i + 1 < len(points) else 0
        ip = line_intersection_point(l1p1, l1p2, points[i], points[next])
        if ip != None:
            if ip not in intersection_points:
                intersection_points.append(ip)
    return intersection_points


def col_poly_poly_intersection_points(poly1, poly2):
    clipped_corners = []
    poly1_points = poly1.points
    poly2_points = poly2.points
    #Add  the corners of poly1 which are inside poly2
    for i in range(len(poly1_points)):
        if point_in_poly(poly1_points[i], poly2):
            if poly1_points[i] not in clipped_corners:
                clipped_corners.append(poly1_points[i])

    #Add  the corners of poly2 which are inside poly1
    for i in range(len(poly2_points)):
        if point_in_poly(poly2_points[i], poly1):
            if poly2_points[i] not in clipped_corners:
                clipped_corners.append(poly2_points[i])

    #Add intersection points
    for i in range(len(poly1_points)):
        next = i + 1 if (i + 1) < len(poly1_points) else 0
        points = poly_line_intersection_points(poly1_points[i], poly1_points[next], poly2)
        for p in points:
            if p not in clipped_corners:
                clipped_corners.append(p)
    pos = poly1.pos
    if len(clipped_corners) == 0:
        return None, None

    #Find closest point
    closest_p = clipped_corners[0]
    closest_dist = math.inf
    for p in clipped_corners:
        d = Vec2(v=pos-p).mag()
        if d < closest_dist:
            closest_dist = d
            closest_p = p

    return clipped_corners, closest_p

def poly_closest_intersection(poly1, poly2):
    clipped_corners, closest_p = col_poly_poly_intersection_points(poly1, poly2)
    return closest_p