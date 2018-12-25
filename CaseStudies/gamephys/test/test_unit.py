from Tamias2D import *

#Vec2
def test_vec2_add():
    print("testing vector addition")
    assert (Vec2(1, 2) + Vec2(2, 4)) == Vec2(3, 6)

    print("testing vector addition")
    assert (Vec2(-1, 2) + Vec2(2, -4)) == Vec2(1, -2)
def test_vec2_sub():
    print("testing vector subtraction")
    assert (Vec2(1, 2) - Vec2(2, 4)) == Vec2(-1, -2)

    print("testing vector subtraction")
    assert (Vec2(11, 2) - Vec2(-2, -4)) == Vec2(13, 6)

def test_vec2_mul():
    print("testing scalar multiplication with a vector")
    assert (Vec2(2, 4)*2) == Vec2(4, 8)

    print("testing scalar multiplication with a vector")
    assert (Vec2(12, -4) * 2) == Vec2(24, -8)
def test_vec2_mag():
    print("testing vector magnitude")
    assert Vec2(0, 4).mag() == 4

    print("testing vector magnitude")
    assert Vec2(3, 4).mag() == 5
def test_vec2_dot():
    print("testing vector dot product")
    assert Vec2.dot(Vec2(1,2), Vec2(2,1)) == 4

#Shape
def test_shape_set_angle():
    print("testing shape set angle")
    shp = Box(Vec2(0,0), Vec2(100,100))
    shp.set_angle(45)
    assert shp.angle == 45
def test_shape_set_pos():
    print("testing shape set position")
    shp = Box(Vec2(0,0), Vec2(100,100))
    shp.set_pos(Vec2(2,2))
    assert shp.pos == Vec2(2,2)

#Body
def test_body_apply_force():
    print("testing body apply force")
    shp = Box(Vec2(0, 0), Vec2(100, 100))
    mass = 1000
    body = Body(Vec2(0, 0), mass, shp)
    force = Vec2(1000,0)
    body.apply_force(force)
    body.update(1/60)
    expectedAccel = force/mass
    assert body.accel == expectedAccel

def test_body_apply_torque():
    print("testing body apply torque")
    shp = Box(Vec2(0, 0), Vec2(100, 100))
    body = Body(Vec2(0, 0), 100, shp)
    torque = 1000
    body.apply_torque(torque)
    body.update(1/60)
    expectedAngularAccel = torque/body.inertia
    assert body.angularAccel == expectedAngularAccel

#space
def test_space_set_gravity():
    print("testing space set gravity")
    shp = Box(Vec2(0, 0), Vec2(100, 100))
    body = Body(Vec2(0, 0), 100, shp)
    space = Space()
    gravity = Vec2(0, 9800)
    time = 2
    space.set_gravity(gravity)
    space.add_body(body)
    body.update(time)
    expectedAccel = gravity * time
    assert body.accel == expectedAccel

#collision
def test_CollisionHandler_is_intersecting_with():
    shape1 = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body1 = Body(Vec2(250, 0), 1000, shape1, 0, Body.DYNAMIC, 0)
    shape2 = Box(Vec2(0, 0), Vec2(100, 200), 0)
    body2 = Body(Vec2(300, 50), 1000, shape2, 0, Body.DYNAMIC, 0)
    CollisionHandler._is_intersecting_with(body1, body2)

    shape1 = Box(Vec2(0, 0), Vec2(100, 50), 0)
    body1 = Body(Vec2(50, 0), 1000, shape1, 0, Body.DYNAMIC, 0)
    shape2 = Box(Vec2(10, 10), Vec2(150, 200), 0)
    body2 = Body(Vec2(300, 50), 1000, shape2, 0, Body.DYNAMIC, 0)
    CollisionHandler._is_intersecting_with(body1, body2)
