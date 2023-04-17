from abc import ABC


class AbstractEngine(ABC):
    def __init__(self, current_mileage, last_service_mileage, warning_light_is_on):
        if current_mileage is not None and last_service_mileage is not None:
            self.current_mileage = current_mileage
            self.last_service_mileage = last_service_mileage
        if warning_light_is_on is not None:
            self.warning_light_is_on = warning_light_is_on

