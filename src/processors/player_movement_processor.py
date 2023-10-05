import esper
from components.components import Position, Inputs, Velocity

class PlayerMovementProcessor(esper.Processor):

    def __init__(self, player_entity, inputs_entity):
        super().__init__()
        self._player_entity = player_entity
        self._inputs_entity = inputs_entity

    def process(self):
        player_position_component = esper.try_component(self._player_entity, Position)
        player_velocity_component = esper.try_component(self._player_entity, Velocity)
        inputs_component = esper.try_component(self._inputs_entity, Inputs)
        
        assert(player_position_component != None)
        assert(player_velocity_component != None)
        assert(inputs_component != None)

        if inputs_component.up and player_position_component.y > 10:
            player_position_component.y -= player_velocity_component.value
        if inputs_component.down and player_position_component.y < 320:
            player_position_component.y += player_velocity_component.value
        