from abc import ABC


class AbstractBattery(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        return True
