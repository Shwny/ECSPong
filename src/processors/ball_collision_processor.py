import logging
import esper
from components.components import Position, RenderableRectangle, Event
from engine.utils import util_rectangle_collide_check

class BallXCollisionProcessor(esper.Processor):

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

        if ball_position_component.x < 0 or ball_position_component.x > 630:
            esper.dispatch_event(Event.ball_horizontal_collision)

        ball_player_collision_check: bool = util_rectangle_collide_check(ball_position_component, ball_rectangle, player_position_component, player_rectangle)
        
        if ball_player_collision_check:
            # Left-side collision
            if ball_position_component.x < player_position_component.x:
                ball_position_component.x = player_position_component.x - ball_rectangle.w    
            # Right-side collision
            elif ball_position_component.x > player_position_component.x:
                ball_position_component.x = player_position_component.x + player_rectangle.w
            esper.dispatch_event(Event.ball_horizontal_collision)
            
class BallYCollisionProcessor(esper.Processor):

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

        if ball_position_component.y < 0 or ball_position_component.y > 350:
            esper.dispatch_event(Event.ball_vertical_collision)

        ball_player_collision_check: bool = util_rectangle_collide_check(ball_position_component, ball_rectangle, player_position_component, player_rectangle)
        
        if ball_player_collision_check:
            # Bottom-side collision
            if ball_position_component.y < player_position_component.y:
                ball_position_component.y = player_position_component.y - ball_rectangle.h
            # Top-side collision
            elif ball_position_component.y > player_position_component.y:
                ball_position_component.y = player_position_component.y + player_rectangle.h
            esper.dispatch_event(Event.ball_vertical_collision)