
from engine.engine import AbstractEngine


class SternmanEngine(AbstractEngine):
    def __init__(self, warning_light_is_on):
        super().__init__(warning_light_is_on)

    def engine_should_be_serviced(self):
        return self.warning_light_is_on
