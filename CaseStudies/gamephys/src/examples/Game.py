import pygame
from Tamias2D.draw import *
from Tamias2D import *
import collision
import random
body = None
def add_ball(space):
    min = 350
    max = 600
    circleShape = Circle(Vec2(200, 0), 50)
    circleBody = Body(Vec2(random.randint(min,max), 0), 100, circleShape, 0, Body.DYNAMIC, 2)
    space.add_body(circleBody)
pygame.init()
display_width = 800
display_height = 600
black = (0,0,0)
lblue = (220,240,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Physics Simulation')
space = Space()
floorShape1 = Box(Vec2(0,500), Vec2(800, 600), 0)
floor1 = Body(Vec2(400,560), 10000, floorShape1, 0, Body.STATIC, 2)
floorShape2 = Box(Vec2(0,0), Vec2(50, 600), 0)
floor2 = Body(Vec2(25,300), 10000, floorShape2, 0, Body.STATIC, 2)
space.set_gravity(Vec2(0, 1000))
space.add_body(floor1)
space.add_body(floor2)
#shape = Polygon(Vec2(0,0), [Vec2(0,-100), Vec2(50,-150), Vec2(100,-100), Vec2(100,100), Vec2(-50, 100)], 0)


for i in range(5):
    r = random.randint(1,10)
    if r % 2 ==0:
        shp = Box(Vec2(0,0), Vec2(60,60), 0)
    else:
        shp = Polygon(Vec2(0,0), [Vec2(0,30), Vec2(15,60), Vec2(30,30), Vec2(60,15), Vec2(30,0), Vec2(15, -30), Vec2(0,0), Vec2(-30, 15)], 0)
    x = i*150+100
    y = random.randint(-100, 300)
    bdy = Body(Vec2(x, y),1000, shp, 0, Body.DYNAMIC, 2)
    aV = random.randint(-400,40)
    bdy.angularVel =  aV
    body = bdy
    space.add_body(bdy)
draw = drawHandler(gameDisplay)
clock = pygame.time.Clock()
crashed = False


while not crashed:
    deltaTime = (1/60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                add_ball(space)
            if event.key == pygame.K_DOWN:
                body.velocity.x = -1000
                body.velocity.y = -1000


    gameDisplay.fill((100,0,150))
    space.step(deltaTime)
    draw.draw_space(space)
    pygame.display.update()

    clock.tick(60)
pygame.quit()
quit()