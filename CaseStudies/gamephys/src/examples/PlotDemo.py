from Tamias2D import *
import collision
import random

space = Space()

space.set_gravity(Vec2(0, 1000))
floorShape = Box(Vec2(-900,800), Vec2(1800, 2000), 0)
floor = Body(Vec2(-900,4400), 1000, floorShape, 0, Body.STATIC, 0.1)
space.add_body(floor)
shape = Box(Vec2(0,0), Vec2(100,200), 0)
body = Body(Vec2(250,0), 1000, shape, 0, Body.DYNAMIC,0)
space.add_body(body)

shape2 = Polygon(Vec2(0,0), [Vec2(0,0), Vec2(50,-50), Vec2(100,0), Vec2(100,100), Vec2(0, 100)], 0)
body2 = Body(Vec2(250,280), 1000, shape2, 0, Body.DYNAMIC,2)
space.add_body(body2)
#body2.apply_force(Vec2(1000,0))

circleShape = Circle(Vec2(200, 0), 50)
circleBody = Body(Vec2(200,0), 1000, circleShape, 0, Body.DYNAMIC, 1.5)
clock = Clock()

output = PhysicsOutput()
opt = OutputOptions()
opt.enable_option(Options.POSITION)
opt.enable_option(Options.VELOCITY)
opt.enable_option(Options.ANGVEL)
output.set_options(opt)
output.add_body(body)
output.add_body(body2)
output.add_body(circleBody)

body.apply_torque(1000)
body2.apply_torque(2000000)
plotter = Plotter( timeToPlot=5000, whatToPlot=[Options.POSITION, Options.VELOCITY])
plotter.add_to_output(output)

closed = False
while not closed:

    deltaTime = clock.tick(30)
    if plotter.done:
        windowCount = len(plt._pylab_helpers.Gcf.figs.values())
        if windowCount == 0:
            closed=True
    else:
        space.step(deltaTime)
        output.update(deltaTime)



