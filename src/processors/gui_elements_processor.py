import logging
import esper
import pygame
from components.components import Position, Event, EntityType, GuiElement

class GuiElementsProcessor(esper.Processor):

    def __init__(self, screen, font):
        super().__init__()
        self._screen: pygame.Surface = screen
        self._font: pygame.font.Font = font

    def process(self):
        for ent, (gui_element, pos) in esper.get_components(GuiElement, Position):
            print(ent)
            text_to_render = self._font.render(gui_element.string_value, True, (255, 255, 255))
            self._screen.blit(text_to_render, (pos.x, pos.y))