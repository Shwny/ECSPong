import esper
from components.components import Timer

class TimersProcessor(esper.Processor):

    def __init__(self, delta_time):
        super().__init__()
        self._delta_time = delta_time

    def process(self):
        for ent, (timer) in esper.get_component(Timer):
            if timer.active:
                timer.current_value_millis += self._delta_time
                timer.current_value_integer = int(timer.current_value_millis / 1000)
                timer.current_value_integer_countdown = int(timer.total_duration - int(timer.current_value_millis))

                if timer.current_value_millis >= timer.total_duration:
                    timer.active = False
                    timer.current_value_integer = 0
                    timer.current_value_millis = 0.0
                    timer.current_value_integer_countdown = timer.total_duration