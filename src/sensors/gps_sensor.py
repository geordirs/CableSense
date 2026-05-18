import random
from .base_sensor import BaseSensor

class GPSSensor(BaseSensor):
    def read_data(self):
        """
        Simulates GPS coordinates.
        Returns a dictionary with latitude and longitude.
        """
        # Simulating a small movement around a central point
        lat = 4.7110 + random.uniform(-0.001, 0.001)
        lon = -74.0721 + random.uniform(-0.001, 0.001)
        return {
            'latitude': lat,
            'longitude': lon
        }

    @property
    def sensor_type(self):
        return "gps"
