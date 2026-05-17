import random
from .base_sensor import BaseSensor

class GPRSensor(BaseSensor):
    def read_data(self):
        # Simulating GPR data (Ground Penetrating Radar)
        return random.uniform(0, 1)

    @property
    def sensor_type(self):
        return "gpr"
