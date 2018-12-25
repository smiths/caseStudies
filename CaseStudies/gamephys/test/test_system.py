from Tamias2D import *
import matplotlib.pyplot as plt
import numpy as np
#helper functions
def perform_plot_loop(space, output, plotter, clock, get_time = False):
    closed = False
    lines = []
    times = []
    done_getting_info = False
    while not closed:
        deltaTime = clock.tick(30)
        space.step(deltaTime)
        output.update(deltaTime)

        if plotter.ready:
            if not done_getting_info:
                done_getting_info = True
                for i in plt.get_fignums():
                    fig = plt.figure(i)
                    for ax in fig.axes:
                        for l in ax.lines:
                            lines.append(l.get_ydata().tolist())
                            if get_time:
                                times.append(l.get_xdata().tolist())
                plotter.show()
        if plotter.done:
                closed = True
    if get_time:
        return lines, times
    return lines
def get_time_index(timeAr, target, slop = 0.3):
    potentialT = 0
    for i in range(len(timeAr)):
        t = timeAr[i]
        if abs(target - t) < slop:
            return i
        else:
            if math.ceil(t) == target:
                potentialT = i
    return potentialT

def data_increasing_over_time(data):
    last_d = -math.inf
    for d in data:
        if d < last_d:
            return False
        last_d = d
    return True

def data_decreasing_over_time(data):
    last_d = math.inf
    for d in data:
        if d > last_d:
            return False
        last_d = d
    return True

def data_around_same_value(data, slop = 2):
    last_d = data[0]
    for d in data:
        if abs(d - last_d) > slop:
            return False
        last_d = d
    return True
#System tests
def test_system_horizontal_translation_right():
    print("==Testing horizontal movement to the right")
    space = Space()
    clock = Clock()
    shape = Box(Vec2(0,0), Vec2(100,100), 0)
    body = Body(Vec2(20,20), 10, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True)
    plotter.add_to_output(output)

    body.apply_force(Vec2(100,0))
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Assert that x position increased over time")
    assert data_increasing_over_time(lines[0])
    print("Assert that x velocity increased over time")
    assert data_increasing_over_time(lines[2])
    print("Assert that y position didn't change")
    assert data_around_same_value(lines[1]) #y position
    print("Assert that y velocity didn't change")
    assert data_around_same_value(lines[3])
    print(lines[0])
    print(lines[2])
    print(lines[1])
    print(lines[3])

    print("==Testing static object with no force")
    space = Space()
    clock = Clock()
    shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body = Body(Vec2(50, 50), 10, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True)
    plotter.add_to_output(output)

    body.apply_force(Vec2(0, 0))
    lines = perform_plot_loop(space, output, plotter, clock)
    # print("Assert that x position increased over time")
    # assert data_increasing_over_time(lines[0])
    # print("Assert that x velocity increased over time")
    # assert data_increasing_over_time(lines[2])
    print("Assert that y position didn't change")
     #assert data_around_same_value(lines[1]) #y position
    print("Assert that y velocity didn't change")
    assert data_around_same_value(lines[3])
    print(lines[0])
    print(lines[2])
    print(lines[1])
    print(lines[3])

def test_system_horizontal_translation_left():
    print("==Testing horizontal movement to the left")
    space = Space()
    clock = Clock()
    shape = Box(Vec2(900,900), Vec2(1000,1000), 0)
    body = Body(Vec2(950,50), 10, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True)
    plotter.add_to_output(output)

    body.apply_force(Vec2(-100,0))
    lines = perform_plot_loop(space, output, plotter, clock)

    print("Assert that x position decreased over time")
    assert data_decreasing_over_time(lines[0])
    print("Assert that x velocity decreased over time")
    assert data_decreasing_over_time(lines[2])
    print("Assert that y position didn't change")
    assert data_around_same_value(lines[1])
    print("Assert that y velocity didn't change")
    assert data_around_same_value(lines[3])
    print(lines[0])
    print(lines[2])
    print(lines[1])
    print(lines[3])

def test_system_free_falling():
    print("==Testing 3 bodies free falling")
    space = Space()
    space.set_gravity(Vec2(0,9.8))
    clock = Clock()
    shape = Box(Vec2(0,0), Vec2(100,100), 0)
    body = Body(Vec2(100,50), 100, shape)
    space.add_body(body)

    shape2 = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body2 = Body(Vec2(300, 50), 1000, shape2)
    space.add_body(body2)

    shape3 = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body3 = Body(Vec2(600, 50), 1000, shape3)
    space.add_body(body3)

    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    output.add_body(body2)
    output.add_body(body3)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True)
    plotter.add_to_output(output)
    lines, times = perform_plot_loop(space, output, plotter, clock,get_time=True)
    t = times[0]
    tI = get_time_index(t, 4)
    print("Checking result by approximation to the free fall formula after 4 seconds")
    print("h=V0t+(1/2)g(t^2)")
    h = 0.5 * 9.8 * (4*4)
    print("Height after 4 seconds using the equation: "+str(h))
    bPos = lines[4]
    h2 = bPos[tI]
    print("Height as calculated by the engine in real time: {}".format(h2))

    slop = 10
    print("Assert that the prediction was accurate enough")
    assert abs(h-h2) <slop

    # print("==Testing a rigid body free falling")
    # space = Space()
    # space.set_gravity(Vec2(0, 9.8))
    # clock = Clock()
    # shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    # body = Body(Vec2(100, 50), 100, shape)
    # space.add_body(body)
    #
    # output = PhysicsOutput()
    # opts = OutputOptions()
    # opts.enable_option(Options.POSITION)
    # opts.enable_option(Options.VELOCITY)
    # output.options = opts
    # output.add_body(body)
    # plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True)
    # plotter.add_to_output(output)
    # lines, times = perform_plot_loop(space, output, plotter, clock, get_time=True)
    # t = times[0]
    # tI = get_time_index(t, 4)
    # print("Checking result by approximation to the free fall formula after 4 seconds")
    # print("h=V0t+(1/2)g(t^2)")
    # h = 0.5 * 9.8 * (4 * 4)
    # print("Height after 4 seconds using the equation: " + str(h))
    # bPos = lines[4]
    # h2 = bPos[tI]
    # print("Height as calculated by the engine in real time: {}".format(h2))
    #
    # slop = 10
    # print("Assert that the prediction was accurate enough")
    # assert abs(h - h2) < slop

def test_system_free_bodies_forces():
    print("==Testing 3 floating bodies by applying forces to them")
    space = Space()
    clock = Clock()
    shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body = Body(Vec2(0, 50), 1, shape)
    space.add_body(body)

    shape2 = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body2 = Body(Vec2(300, 50), 4000, shape2)
    space.add_body(body2)

    shape3 = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body3 = Body(Vec2(600, 50), 10, shape3)
    space.add_body(body3)
    body.apply_force(Vec2(-300,0))
    body2.apply_force(Vec2(0,80000))
    body3.apply_force(Vec2(1000,-2000))

    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    output.add_body(body2)
    output.add_body(body3)

    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True)
    plotter.add_to_output(output)
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Assert that body0 has x position and x velocity decreased due to applying the force.")
    assert data_decreasing_over_time(lines[0])
    assert data_decreasing_over_time(lines[6])

    print("Assert that body1 has y position and y velocity increased due to applying the force.")
    assert data_increasing_over_time(lines[4])
    assert data_increasing_over_time(lines[10])

    print("Assert that body2 has both x position and x velocity increased. It also had y position and y velocity decreased due to applying the force.")
    assert data_increasing_over_time(lines[2])
    assert data_increasing_over_time(lines[8])
    assert data_decreasing_over_time(lines[5])
    assert data_decreasing_over_time(lines[11])

def test_system_projectile_45deg():
    print("==Testing 45 degree projectile motion")

    space = Space()
    space.set_gravity(Vec2(0,-100))
    clock = Clock()
    shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body = Body(Vec2(0, 0), 10, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True, timeToPlot=20000)
    plotter.add_to_output(output)

    rad45 = 45 * math.pi / 180
    dir = Vec2(math.cos(rad45), math.sin(rad45)) #(0.707, 0.707
    vel = dir * 1200
    body.velocity = vel
    lines = perform_plot_loop(space, output, plotter, clock)
    print(lines)


def test_system_projectile_60deg():
    print("==Testing 60 degree projectile motion")
    space = Space()
    space.set_gravity(Vec2(0, -40))
    clock = Clock()
    shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body = Body(Vec2(50, 50), 1000, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True, timeToPlot=20000)
    plotter.add_to_output(output)
    rad60 = 60 * math.pi / 180
    dir = Vec2(math.cos(rad60), math.sin(rad60))
    vel = dir * 300
    body.velocity = vel
    lines = perform_plot_loop(space, output, plotter, clock)

def test_system_rotation_around_axis():
    print("==Testing rotation of an object around its axis due to applying torque")
    space = Space()
    space.set_gravity(Vec2(0, 0))
    clock = Clock()
    shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body = Body(Vec2(50, 50), 0.5, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.TORQUE)
    opts.enable_option(Options.ANGLE)
    opts.enable_option(Options.ANGVEL)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.TORQUE, Options.ANGLE], waitToPlot=True, timeToPlot=4000)
    plotter.add_to_output(output)
    body.apply_torque(100)
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Assert that applying the torque has caused the angle's value to increase")
    assert data_increasing_over_time(lines[1])

def test_system_angular_velocity():
    print("==Testing rotation of an object around its axis due to applying torque")
    space = Space()
    space.set_gravity(Vec2(0, -40))
    clock = Clock()
    shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body = Body(Vec2(50, 50), 0.5, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.TORQUE)
    opts.enable_option(Options.ANGVEL)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.TORQUE, Options.ANGVEL], waitToPlot=True, timeToPlot=4000)
    plotter.add_to_output(output)
    torque = 100
    t = 4
    body.apply_torque(torque)
    print("Inertia: "+ str(body.inertia))
    lines, times = perform_plot_loop(space, output, plotter, clock, get_time = True)
    print("Assert that the resulting angular velocity from applying a torque is accurate enough by calculating it manually then comparing with the engine's result")
    print("a=T/I, a=w/t")
    accel = torque / body.inertia
    angVel = accel * t
    print ("Angular velocity after 4 seconds as calculated by the formula: {}".format(angVel))

    _time = times[0]
    i = get_time_index(_time, t)
    l = lines[1]
    angVel2 = l[i]
    print ("Angular velocity as calculated in real time by the engine: {}".format(angVel2))
    slop = 5
    assert abs(angVel2 - angVel) < slop

def test_system_torque_and_inertia():
    print("==Testing to see if applying the same torque to two bodies with different moment of inertias would result in different angular velocities")
    space = Space()
    space.set_gravity(Vec2(0, -40))
    clock = Clock()
    shape = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body0 = Body(Vec2(50, 50), 0.5, shape)

    shape2 = Box(Vec2(500, 500), Vec2(1000, 1000), 0)
    body1 = Body(Vec2(50, 50), 500, shape2)
    body0.should_clamp_angle = False
    body1.should_clamp_angle = False
    space.add_body(body0)
    space.add_body(body1)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.TORQUE)
    opts.enable_option(Options.ANGVEL)
    output.options = opts
    output.add_body(body0)
    output.add_body(body1)

    plotter = Plotter(whatToPlot=[Options.TORQUE, Options.ANGVEL], waitToPlot=True, timeToPlot=4000)
    plotter.add_to_output(output)
    body0.apply_torque(100)
    body1.apply_torque(100)
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Assert that body1's angular velocity didn't change much due to having a higher inertia, while the same is not true for body0.")
    assert data_around_same_value(lines[3])
    assert data_around_same_value(lines[2]) == False

def test_system_collision_same_mass():
    print("==Testing collision between two bodies who have the same mass")
    space = Space()
    clock = Clock()
    mass =100
    shape0 = Box(Vec2(0, 0), Vec2(300, 300), 0)
    body0 = Body(Vec2(0, 50), mass, shape0)
    space.add_body(body0)

    shape1 = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body1 = Body(Vec2(300, 50), mass, shape1)
    space.add_body(body1)

    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body0)
    output.add_body(body1)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True, timeToPlot=4000)
    plotter.add_to_output(output)
    body0.apply_force(Vec2(500,0))
    body1.apply_force(Vec2(-500,0))
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Figure shows that the collision happened")
def test_system_col_impulse_against_static_object():
    print("==Testing the impulse resulting from collision between a free falling object and a static object")
    space = Space()
    space.set_gravity(Vec2(0, 9.8))
    clock = Clock()
    shape0 = Box(Vec2(0, 500), Vec2(800, 600), 0)
    body0 = Body(Vec2(0, 560), 10000, shape0,0, Body.STATIC)
    space.add_body(body0)

    shape1 = Box(Vec2(0, 0), Vec2(300, 300), 0)
    body1 = Body(Vec2(0, 400), 100, shape1)
    space.add_body(body1)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body0)
    output.add_body(body1)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True, timeToPlot=4000)
    plotter.add_to_output(output)
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Figure shows the effect of the impulse")

def test_system_stress_test():
    print("==Testing performance by adding 50 bodies to the simulation")
    space = Space()
    space.set_gravity(Vec2(0, 98))
    clock = Clock()
    output = PhysicsOutput()
    for i in range(50):
        shape = Box(Vec2(0, 0), Vec2(200, 200), 0)
        body = Body(Vec2(100 + 500 *i, 560), 200, shape)
        space.add_body(body)
        output.add_body(body)

    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True, timeToPlot=4000)
    plotter.add_to_output(output)
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Assert that the simulation ran without crashing and returned data from all bodies")
    assert len(lines) >= 50
def test_system_collision_response_rotation():
    print("==Testing collision between two bodies and confirming that their angular velocity changes due to collision")
    space = Space()
    clock = Clock()

    shape0 = Box(Vec2(0, 0), Vec2(300, 300), 0)
    body0 = Body(Vec2(0, 50), 100, shape0)
    space.add_body(body0)

    shape1 = Box(Vec2(0, 0), Vec2(100, 100), 0)
    body1 = Body(Vec2(300, 50), 1000, shape1)
    space.add_body(body1)

    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.ANGVEL)
    output.options = opts
    output.add_body(body0)
    output.add_body(body1)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.ANGVEL], waitToPlot=True, timeToPlot=4000)
    plotter.add_to_output(output)
    body0.apply_force(Vec2(5000,0))
    body1.apply_force(Vec2(-5000,0))
    lines = perform_plot_loop(space, output, plotter, clock)
    print("Figure shows that the collision happened")