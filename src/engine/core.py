import pygame
import esper
import sys
import random

from components.components import Position, RenderableRectangle, Color, Inputs, Velocity, Direction, CurrentDirection, Event
from processors.renderable_rectangle_processor import RenderableRectangleProcessor
from processors.player_movement_processor import PlayerMovementProcessor
from processors.inputs_processor import InputsProcessor
from processors.ball_movement_processor import BallXMovementProcessor, BallYMovementProcessor
from processors.ball_collision_processor import BallXCollisionProcessor, BallYCollisionProcessor

class Engine:

    # GAME INITIALIZATION

    def __init__(self):
        
        # Pygame initialization
        pygame.init()

        # Window title
        
        # Window managment related stuff
        self._window_width: int = 640
        self._window_height: int = 360
        self._resolution_width: int = 320
        self._resolution_height: int = 180
        self._screen: pygame.Surface = pygame.display.set_mode((self._window_width, self._window_height))
        
        # Time and frame managment related stuff
        self._fps_clock: pygame.Clock = pygame.time.Clock()
        self._fps: int = 60

    # GAME EXECUTION

    def run(self) -> None:

        # COMPONENTS

        inputs = esper.create_entity()
        esper.add_component(inputs, Inputs())

        player = esper.create_entity()
        esper.add_component(player, Position(10, 10))
        esper.add_component(player, RenderableRectangle(50, 50)) # (10, 30)
        esper.add_component(player, Color(255, 255, 255))
        esper.add_component(player, Velocity(2))

        enemy = esper.create_entity()
        esper.add_component(enemy, Position(620, 10))
        esper.add_component(enemy, RenderableRectangle(10, 30))
        esper.add_component(enemy, Color(255, 255, 255))
        esper.add_component(enemy, Velocity(2))

        ball = esper.create_entity()
        esper.add_component(ball, Position(315, 175))
        esper.add_component(ball, RenderableRectangle(10, 10))
        esper.add_component(ball, Color(255, 255, 255))
        esper.add_component(ball, Velocity(3))
        random_value_for_vertical_direction: Direction = random.choice([Direction.up, Direction.down])
        random_value_for_horizontal_direction: Direction = random.choice([Direction.left, Direction.right])
        esper.add_component(ball, CurrentDirection(horizontal_value = random_value_for_horizontal_direction, vertical_value = random_value_for_vertical_direction))

        central_line = esper.create_entity()
        esper.add_component(central_line, Position(319, 0))
        esper.add_component(central_line, RenderableRectangle(1, 360))
        esper.add_component(central_line, Color(255, 255, 255))

        # PROCESSORS

        # TODO: fix inputs paramteter name from "inputs" to "inputs_entity"
        player_movement_processor = PlayerMovementProcessor(player_entity = player, inputs_entity = inputs)
    
        ball_x_movement_processor = BallXMovementProcessor(ball_entity = ball)
        ball_x_collision_processor = BallXCollisionProcessor(ball_entity = ball, player_entity = player, enemy_entity = enemy)
        ball_y_movement_processor = BallYMovementProcessor(ball_entity = ball)
        ball_y_collision_processor = BallYCollisionProcessor(ball_entity = ball, player_entity = player, enemy_entity = enemy)

        input_processor = InputsProcessor(inputs_entity = inputs)
        renderable_rectangle_processor = RenderableRectangleProcessor(screen = self._screen)    
        # EVENTS

        esper.set_handler(Event.ball_horizontal_collision, ball_x_movement_processor.invert_ball_horizontal_direction)
        esper.set_handler(Event.ball_vertical_collision, ball_y_movement_processor.invert_ball_vertical_direction)

        # GAME LOOP

        while True:
            self._screen.fill((0, 0, 0))
  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()

            input_processor.process()
            player_movement_processor.process()
            ball_x_movement_processor.process()
            ball_x_collision_processor.process()
            ball_y_movement_processor.process()
            ball_y_collision_processor.process()

            renderable_rectangle_processor.process()
            
            pygame.display.flip()
            self._fps_clock.tick(self._fps)
