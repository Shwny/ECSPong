import esper
import pygame
from components.components import Position, RenderableRectangle, Color

class RenderableRectangleProcessor(esper.Processor):

    def __init__(self, screen):
        super().__init__()
        self._screen = screen

    def process(self):
        for ent, (pos, rend, color) in esper.get_components(Position, RenderableRectangle, Color):
            pygame.draw.rect(self._screen, (color.r, color.g, color.b), pygame.Rect(pos.x, pos.y, rend.w, rend.h))