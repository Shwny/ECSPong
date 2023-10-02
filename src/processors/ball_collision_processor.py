import random
import esper
from engine.utils import util_rectangle_collide_check
from engine.utils import Event
from components.components import Position, RenderableRectangle

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

        check_ball_player_collision: bool = util_rectangle_collide_check(ball_position_component, 
                                                                         ball_rectangle, 
                                                                         player_position_component, 
                                                                         player_rectangle)
        
        check_ball_enemy_collision: bool = util_rectangle_collide_check(ball_position_component, 
                                                                         ball_rectangle, 
                                                                         enemy_position_component, 
                                                                         enemy_rectangle)
        
        if check_ball_enemy_collision or check_ball_player_collision:
            esper.dispatch_event(Event.BALL_COLLISION, )
        
        
