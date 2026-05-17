import random
from .base_sensor import BaseSensor

class AcousticSensor(BaseSensor):
    def read_data(self):
        # Simulating acoustic data
        return random.uniform(0, 1)

    @property
    def sensor_type(self):
        return "acoustic"
