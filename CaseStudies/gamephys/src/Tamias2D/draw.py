from Tamias2D.space import *
from Tamias2D.shapes import *
import pygame
class drawHandler:
    def __init__(self, screen_):
        self.screen = screen_
    def draw_space(self, space_):
        for b in space_.get_bodies():
            s = b.shape
            if isinstance(s, Box):
                pygame.draw.polygon(self.screen, pygame.Color(255, 100, 100), s.vertsAsList(), 3)

            elif isinstance(s, Polygon):
                pygame.draw.polygon(self.screen, pygame.Color(100,0,100), s.vertsAsList(), 3)
            elif isinstance(s, Circle):
                pygame.draw.circle(self.screen, pygame.Color(200,0,0), (int(s.pos.x), int(s.pos.y)), int(s.radius))



