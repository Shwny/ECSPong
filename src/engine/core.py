import pygame
import esper
import sys
import random
import logging

from components.components import *
from processors.renderable_rectangle_processor import RenderableRectangleProcessor
from processors.player_movement_processor import PlayerMovementProcessor
from processors.inputs_processor import InputsProcessor
from processors.ball_movement_processor import BallXMovementProcessor, BallYMovementProcessor
from processors.ball_collision_processor import BallXCollisionProcessor, BallYCollisionProcessor
from processors.score_processor import ScoreProcessor
from processors.timers_processor import TimersProcessor
from processors.gui_elements_processor import GuiElementsProcessor

class Engine:

    # GAME INITIALIZATION

    def __init__(self):

        # Logging configuration
        logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        
        # Pygame initialization
        pygame.init()

        # Window title
        pygame.display.set_caption('ECSPong')
        
        # Window managment related stuff
        self._window_width: int = 640
        self._window_height: int = 360
        self._resolution_width: int = 320
        self._resolution_height: int = 180
        self._screen: pygame.Surface = pygame.display.set_mode((self._window_width, self._window_height))
        
        # Time and frame managment related stuff
        self._fps_clock: pygame.Clock = pygame.time.Clock()
        self._fps: int = 60

        # Font loading
        self._monogram_font = pygame.font.Font('assets/monogram.ttf', 50)

    # GAME EXECUTION

    def run(self) -> None:

        # COMPONENTS
        
        # SYSTEM DATA

        inputs = esper.create_entity()
        esper.add_component(inputs, Inputs())

        delta_time = esper.create_entity()
        esper.add_component(delta_time, DeltaTime())

        # ENTITIES

        player = esper.create_entity()
        esper.add_component(player, Position(x = 10, y = 10))
        esper.add_component(player, RenderableRectangle(w = 10, h = 50))
        esper.add_component(player, Color(r = 255, g = 255, b = 255))
        esper.add_component(player, Velocity(value = 2))

        enemy = esper.create_entity()
        esper.add_component(enemy, Position(x = 620, y = 10))
        esper.add_component(enemy, RenderableRectangle(w = 10, h = 50))
        esper.add_component(enemy, Color(r = 255, g = 255, b = 255))
        esper.add_component(enemy, Velocity(value = 2))

        ball = esper.create_entity()
        esper.add_component(ball, Position(x = 315, y = 175))
        esper.add_component(ball, RenderableRectangle(w = 10, h = 10))
        esper.add_component(ball, Color(r = 255, g = 255, b = 255))
        esper.add_component(ball, Velocity(value = 4))
        random_value_for_vertical_direction: Direction = random.choice([Direction.up, Direction.down])
        random_value_for_horizontal_direction: Direction = random.choice([Direction.left, Direction.right])
        esper.add_component(ball, CurrentDirection(horizontal_value = random_value_for_horizontal_direction, vertical_value = random_value_for_vertical_direction))

        # STATIC GEOMETRY

        central_line = esper.create_entity()
        esper.add_component(central_line, Position(x = 319, y = 0))
        esper.add_component(central_line, RenderableRectangle(w = 1, h = 360))
        esper.add_component(central_line, Color(r = 255, g = 255, b = 255))

        # GUI

        score_points_for_player = esper.create_entity()
        esper.add_component(score_points_for_player, Position(50, 10))
        esper.add_component(score_points_for_player, GuiElement(string_value = '0'))

        score_points_for_enemy = esper.create_entity()
        esper.add_component(score_points_for_enemy, Position(580, 10))
        esper.add_component(score_points_for_enemy, GuiElement(string_value = '0'))

        #countdown_timer = esper.create_entity()
        #esper.add_component(countdown_timer, Position(295, 10))
        #esper.add_component(countdown_timer, GuiElement(string_value = '0'))

        # TIMERS
        
        timer_score_point = esper.create_entity()
        esper.add_component(timer_score_point, Timer(total_duration = 4000))

        # PROCESSORS

        timers_processor = TimersProcessor(delta_time)
        input_processor = InputsProcessor(inputs_entity = inputs)

        ## UPDATES

        player_movement_processor = PlayerMovementProcessor(player_entity = player, inputs_entity = inputs)
    
        ball_x_movement_processor = BallXMovementProcessor(ball_entity = ball)
        ball_x_collision_processor = BallXCollisionProcessor(ball_entity = ball, player_entity = player, enemy_entity = enemy)
        ball_y_movement_processor = BallYMovementProcessor(ball_entity = ball)
        ball_y_collision_processor = BallYCollisionProcessor(ball_entity = ball, player_entity = player, enemy_entity = enemy)

        score_processor = ScoreProcessor(timer_score_point_entity = timer_score_point, 
                                         score_points_for_player_entity = score_points_for_player, 
                                         score_points_for_enemy_entity = score_points_for_enemy)
        
        ## DRAWS

        renderable_rectangle_processor = RenderableRectangleProcessor(screen = self._screen)
        gui_element_processor = GuiElementsProcessor(screen = self._screen, font = self._monogram_font)
        
        # EVENTS

        esper.set_handler(Event.ball_horizontal_collision, ball_x_movement_processor.invert_ball_horizontal_direction)
        esper.set_handler(Event.ball_vertical_collision, ball_y_movement_processor.invert_ball_vertical_direction)
        esper.set_handler(Event.score_point, score_processor.activate_score_timer_and_update_score)

        # GAME LOOP

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()

            # UPDATES
            input_processor.process()
            timers_processor.process()
            player_movement_processor.process()
            ball_x_movement_processor.process()
            ball_x_collision_processor.process()
            ball_y_movement_processor.process()
            ball_y_collision_processor.process()

            # DRAWS
            self._screen.fill((0, 0, 0))
            gui_element_processor.process()
            renderable_rectangle_processor.process()
            pygame.display.flip()

            # FINAL CHECKS FOR CURRENT FRAME
            delta_time_component = esper.try_component(delta_time, DeltaTime)
            assert(delta_time_component != None)
            delta_time_component.value = self._fps_clock.tick(self._fps)