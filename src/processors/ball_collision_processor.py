import random
import esper
from engine.utils import util_rectangle_collide_check
from components.components import Position, RenderableRectangle, Event

class BallCollisionProcessor(esper.Processor):

    def __init__(self, ball_entity, player_entity, enemy_entity):
        super().__init__()
        self._ball_entity = ball_entity
        self._player_entity = player_entity
        self._enemy_entity = enemy_entity

    def process(self):
        ball_position_component: Position = esper.try_component(self._ball_entity, Position)
        player_position_component: Position = esper.try_component(self._player_entity, Position)
        enemy_position_component: Position = esper.try_component(self._enemy_entity, Position)
        
        ball_rectangle: RenderableRectangle = esper.try_component(self._ball_entity, RenderableRectangle)
        player_rectangle: RenderableRectangle = esper.try_component(self._player_entity, RenderableRectangle)
        enemy_rectangle: RenderableRectangle = esper.try_component(self._enemy_entity, RenderableRectangle)

        assert(ball_position_component != None)
        assert(player_position_component != None)
        assert(enemy_position_component != None)

        assert(ball_rectangle != None)
        assert(player_rectangle != None)
        assert(enemy_rectangle != None)

        # Check for borders collision
        if ball_position_component.y < 0 or ball_position_component.y > 350:
            esper.dispatch_event(Event.ball_vertical_collision)

        if ball_position_component.x < 0 or ball_position_component.x > 630:
            esper.dispatch_event(Event.ball_horizontal_collision)

        # TODO: implement the ball collision behaviour, properly
        # 1 - check for collisions between entities
        ball_player_collision_check: bool = util_rectangle_collide_check(ball_position_component, ball_rectangle, player_position_component, player_rectangle)
        # 2 - adjust position for ball when collision is detected
        # 3 - check for new position relative to the considered entity and modify ball movement accordingly
        if ball_player_collision_check:
            if ball_position_component.x < player_position_component.x:
                ball_position_component.x = player_position_component.x - ball_rectangle.w
                esper.dispatch_event(Event.ball_horizontal_collision)
            elif ball_position_component.x > player_position_component.x:
                ball_position_component.x = player_position_component.x + player_rectangle.w
                esper.dispatch_event(Event.ball_horizontal_collision)

            if ball_position_component.y < player_position_component.y:
                ball_position_component.y = player_position_component.y - player_rectangle.y
                esper.dispatch_event(Event.ball_vertical_collision)
            elif ball_position_component.y > player_position_component.y:
                ball_position_component.y = player_position_component.y + ball_rectangle.y
                esper.dispatch_event(Event.ball_vertical_collision)
        