import random
from .base_sensor import BaseSensor

class GPRSensor(BaseSensor):
    def read_data(self):
        """
        Simulates GPR data collection.
        Returns a dictionary of GPR-related features.
        """
        return {
            'gpr_amplitude': random.uniform(0, 1),
            'soil_resistivity': random.uniform(10, 1000),
            'burial_depth': random.uniform(0.5, 3.0)
        }

    @property
    def sensor_type(self):
        return "gpr"
