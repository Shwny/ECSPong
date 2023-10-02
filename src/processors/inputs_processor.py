import esper
import pygame
from components.components import Inputs

class InputsProcessor(esper.Processor):

    def __init__(self, inputs):
        super().__init__()
        self._inputs = inputs

    def process(self):
        pressed_keys = pygame.key.get_pressed()
        input_component = esper.try_component(self._inputs, Inputs)
        assert(input_component != None)
        
        if pressed_keys[pygame.K_UP]:
            input_component.up = True
        else:
            input_component.up = False 

        if pressed_keys[pygame.K_DOWN]:
            input_component.down = True
        else:
            input_component.down = False 