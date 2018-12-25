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
def test_system_horizontal_translation_right1():
    print("==Testing horizontal movement to the right")
    space = Space()
    clock = Clock()
    shape = Box(Vec2(0,0), Vec2(100,100), 0)
    body = Body(Vec2(50,50), 10, shape)
    space.add_body(body)
    output = PhysicsOutput()
    opts = OutputOptions()
    opts.enable_option(Options.POSITION)
    opts.enable_option(Options.VELOCITY)
    output.options = opts
    output.add_body(body)
    plotter = Plotter(whatToPlot=[Options.POSITION, Options.VELOCITY], waitToPlot=True)
    plotter.add_to_output(output)

    body.apply_force(Vec2(0,0))
    lines = perform_plot_loop(space, output, plotter, clock)
   # print("Assert that x position increased over time")
   # assert data_increasing_over_time(lines[0])
   # print("Assert that x velocity increased over time")
   # assert data_increasing_over_time(lines[2])
   # print("Assert that y position didn't change")
   # assert data_around_same_value(lines[1]) #y position
   # print("Assert that y velocity didn't change")
    assert data_around_same_value(lines[3])
    print(lines[0])
    print(lines[1])
    print(lines[2])
    print(lines[3])