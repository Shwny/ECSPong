import random
import esper
from components.components import Position, Velocity, CurrentDirection, Direction

class BallMovementProcessor(esper.Processor):

    def __init__(self, ball_entity):
        super().__init__()
        self._ball_entity = ball_entity

    def process(self):
        ball_position_component = esper.try_component(self._ball_entity, Position)
        ball_velocity_component = esper.try_component(self._ball_entity, Velocity)
        ball_direction_component = esper.try_component(self._ball_entity, CurrentDirection)

        assert(ball_position_component != None)
        assert(ball_velocity_component != None)
        assert(ball_direction_component != None) 

        if ball_direction_component.vertical_value == Direction.up:
            ball_position_component.y += ball_velocity_component.value
        elif ball_direction_component.vertical_value == Direction.down:
            ball_position_component.y -= ball_velocity_component.value

        if ball_direction_component.horizontal_value == Direction.right:
            ball_position_component.x += ball_velocity_component.value
        elif ball_direction_component.horizontal_value == Direction.left:
            ball_position_component.x -= ball_velocity_component.value

    def invert_ball_horizontal_direction(self) -> None:
        ball_direction_component = esper.try_component(self._ball_entity, CurrentDirection)

        assert(ball_direction_component != None) 

        if ball_direction_component.horizontal_value == Direction.right:
            ball_direction_component.horizontal_value = Direction.left
        elif ball_direction_component.horizontal_value == Direction.left:
            ball_direction_component.horizontal_value = Direction.right
    
    def invert_ball_vertical_direction(self) -> None:
        ball_direction_component = esper.try_component(self._ball_entity, CurrentDirection)

        assert(ball_direction_component != None) 

        if ball_direction_component.vertical_value == Direction.up:
            ball_direction_component.vertical_value = Direction.down
        elif ball_direction_component.vertical_value == Direction.down:
            ball_direction_component.vertical_value = Direction.up
            
