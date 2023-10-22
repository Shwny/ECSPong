import esper
import pygame
from components.components import Position, GuiElement, CustomFont, ActiveElement, Timer, GuiElementSelected

class GuiElementsGameProcessor(esper.Processor):

    def __init__(self, screen):
        super().__init__()
        self._screen: pygame.Surface = screen
    
    # WHY ARE MENU GUI ELEMENTS NOT DISPLAYING CORRECTLY?
    def process(self):
        for ent, (gui_element, pos, font, active) in esper.get_components(GuiElement, Position, CustomFont, ActiveElement):
            if active.value == True:
                text_to_render = font.value.render(gui_element.string_value, True, (255, 255, 255))
                self._screen.blit(text_to_render, (pos.x, pos.y))
        
        for ent, (timer, gui_element, pos, font, active) in esper.get_components(Timer, GuiElement, Position, CustomFont, ActiveElement):
            if active.value == True:
                gui_element.string_value = f"{int(timer.current_value_integer_countdown / 100)}"
                text_to_render = font.value.render(gui_element.string_value, True, (255, 255, 255))
                self._screen.blit(text_to_render, (pos.x, pos.y))

            for ent, (timer, active) in esper.get_components(Timer, ActiveElement):
                if timer.active == False:
                    active.value = False