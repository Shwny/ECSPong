import esper
from components.components import Position, Inputs, Velocity, DeltaTime

class EnemyMovementProcessor(esper.Processor):

    def __init__(self, enemy_entity, ball_entity, inputs_entity, delta_time_entity):
        super().__init__()
        self._enemy_entity = enemy_entity
        self._ball_entity = ball_entity
        self._inputs_entity = inputs_entity
        self._delta_time_entity = delta_time_entity

    def process(self):
        enemy_position_component = esper.try_component(self._enemy_entity, Position)
        enemy_velocity_component = esper.try_component(self._enemy_entity, Velocity)
        ball_position_component = esper.try_component(self._ball_entity, Position)
        inputs_component = esper.try_component(self._inputs_entity, Inputs)
        delta_time = esper.try_component(self._delta_time_entity, DeltaTime)
        
        assert(enemy_position_component != None)
        assert(enemy_velocity_component != None)
        assert(inputs_component != None)
        assert(delta_time != None)

        if ball_position_component.y < enemy_position_component.y:
            enemy_position_component.y -= enemy_velocity_component.value * delta_time.value
        if ball_position_component.y > enemy_position_component.y:
            enemy_position_component.y += enemy_velocity_component.value * delta_time.value
        