import esper
import pygame
from components.components import Position, GuiElement, CustomFont, ActiveElement, GuiElementSelected

class GuiElementsMenuProcessor(esper.Processor):

    def __init__(self, screen):
        super().__init__()
        self._screen: pygame.Surface = screen
    
    def process(self):
        for ent, (gui_element, pos, font, active) in esper.get_components(GuiElement, Position, CustomFont, ActiveElement):
            gui_element_selected = esper.try_component(ent, GuiElementSelected)

            if active.value == True:
                if gui_element_selected != None and gui_element_selected.value == True:
                    text_to_render = font.value.render(gui_element.string_value, True, gui_element_selected.color)
                    self._screen.blit(text_to_render, (pos.x, pos.y))
                else:
                    text_to_render = font.value.render(gui_element.string_value, True, (255, 255, 255))
                    self._screen.blit(text_to_render, (pos.x, pos.y))