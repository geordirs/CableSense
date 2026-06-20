from abc import ABC, abstractmethod

class BaseSensor(ABC):
    @abstractmethod
    def read_data(self):
        """
        Reads data from the sensor.
        :return: A numerical value representing the sensor reading.
        """
        pass

    @property
    @abstractmethod
    def sensor_type(self):
        """
        Returns the type of the sensor.
        """
        pass
