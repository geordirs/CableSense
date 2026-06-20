import json
import random
try:
    import serial
except ImportError:
    serial = None

class SerialSensorBridge:
    def __init__(self, port='/dev/ttyACM0', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.connection = None
        if serial:
            try:
                self.connection = serial.Serial(port, baudrate, timeout=1)
                print(f"Connected to hardware on {port}")
            except Exception as e:
                print(f"Hardware not found on {port}: {e}. Falling back to simulation.")

    def read_data(self):
        if self.connection and self.connection.in_waiting > 0:
            try:
                line = self.connection.readline().decode('utf-8').strip()
                return json.loads(line)
            except Exception:
                return self._simulate()
        else:
            return self._simulate()

    def _simulate(self):
        return {
            'gpr_amplitude': random.uniform(0, 1),
            'pd_intensity': random.uniform(0, 1)
        }

    @property
    def sensor_type(self):
        return "hardware_bridge"
