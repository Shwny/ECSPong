import logging
import esper
import pygame
from components.components import Position, GuiElement, CustomFont, ActiveElement

class GuiElementsProcessor(esper.Processor):

    def __init__(self, screen):
        super().__init__()
        self._screen: pygame.Surface = screen

    def process(self):
        for ent, (gui_element, pos, font, active) in esper.get_components(GuiElement, Position, CustomFont, ActiveElement):
            if active.value == True:
                text_to_render = font.value.render(gui_element.string_value, True, (255, 255, 255))
                self._screen.blit(text_to_render, (pos.x, pos.y))