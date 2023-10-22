import esper
from components.components import Timer, EntityType, GuiElement, ActiveElement

class ScoreProcessor(esper.Processor):

    def __init__(self, timer_score_point_entity, score_points_for_player_entity, score_points_for_enemy_entity):
        super().__init__()
        self._timer_score_point_entity = timer_score_point_entity
        self._score_points_for_player_entity = score_points_for_player_entity
        self._score_points_for_enemy_entity = score_points_for_enemy_entity

    def process(self):
        pass
    
    # L'evento DEVE essere separato dal processor
    def activate_score_timer_and_update_score(self, scoring_entity: EntityType):
        score_timer_component: Timer = esper.try_component(self._timer_score_point_entity, Timer)
        score_gui_element_component: GuiElement = esper.try_component(self._timer_score_point_entity, GuiElement)
        score_active_element_component: ActiveElement = esper.try_component(self._timer_score_point_entity, ActiveElement)

        assert(score_timer_component != None)
        assert(score_gui_element_component != None)
        assert(score_active_element_component != None)
        
        score_timer_component.active = True
        score_active_element_component.value = True # || THIS EFFECTIVELY HIDES THE COUNTDOWN FOR THE APPLICATION TO RESTART
        score_gui_element_component.string_value = f"{int(score_timer_component.current_value_integer_countdown / 100)}"

        match scoring_entity:
            
            case EntityType.player:
                score_player_component: GuiElement = esper.try_component(self._score_points_for_player_entity, GuiElement)
                assert(score_player_component != None)
                score_player_component.string_value = str(int(score_player_component.string_value) + 1)
                
            case EntityType.enemy:
                score_enemy_component: GuiElement = esper.try_component(self._score_points_for_enemy_entity, GuiElement)
                assert(score_enemy_component != None)
                score_enemy_component.string_value = str(int(score_enemy_component.string_value) + 1)