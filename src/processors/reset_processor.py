import esper
from components.components import ActiveElement, Position

class ResetProcessor(esper.Processor):

    def __init__(self, timer_score_point_entity, player_entity, enemy_entity, ball_entity):
        super().__init__()
        self._timer_score_point_entity = timer_score_point_entity
        self._player_entity = player_entity
        self._enemy_entity = enemy_entity
        self._ball_entity = ball_entity

    def process(self):
        score_active_element_component: ActiveElement = esper.try_component(self._timer_score_point_entity, ActiveElement)
        player_position_component = esper.try_component(self._player_entity, Position)
        enemy_position_component = esper.try_component(self._enemy_entity, Position)
        ball_position_component = esper.try_component(self._ball_entity, Position)

        assert(score_active_element_component != None)

        if(score_active_element_component.value == True):
            player_position_component.x = 10
            player_position_component.y = 10
            enemy_position_component.x = 620
            enemy_position_component.y = 10
            ball_position_component.x = 315
            ball_position_component.y = 175

        