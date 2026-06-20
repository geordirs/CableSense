import random
from .base_sensor import BaseSensor

class AcousticSensor(BaseSensor):
    def read_data(self):
        """
        Simulates Acoustic data collection focusing on Partial Discharge.
        """
        return {
            'pd_intensity': random.uniform(0, 1)
        }

    @property
    def sensor_type(self):
        return "acoustic"
