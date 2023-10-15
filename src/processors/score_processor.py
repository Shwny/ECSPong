import esper
import pygame
from components.components import Timer, EntityType, GuiElement

class ScoreProcessor(esper.Processor):

    def __init__(self, timer_score_point_entity, score_points_for_player_entity, score_points_for_enemy_entity):
        super().__init__()
        self._timer_score_point_entity = timer_score_point_entity
        self._score_points_for_player_entity = score_points_for_player_entity
        self._score_points_for_enemy_entity = score_points_for_enemy_entity

    def process(self):
        pass
        
    def activate_score_timer_and_update_score(self, scoring_entity: EntityType):
        score_timer_component: Timer = esper.try_component(self._timer_score_point_entity, Timer)
        assert(score_timer_component != None)
        score_timer_component.active = True

        match scoring_entity:
            
            case EntityType.player:
                score_player_component: GuiElement = esper.try_component(self._score_points_for_player_entity, GuiElement)
                assert(score_player_component != None)
                score_player_component.string_value = str(int(score_player_component.string_value) + 1)
                
            case EntityType.enemy:
                score_enemy_component: GuiElement = esper.try_component(self._score_points_for_enemy_entity, GuiElement)
                assert(score_enemy_component != None)
                score_enemy_component.string_value = str(int(score_enemy_component.string_value) + 1)
                
