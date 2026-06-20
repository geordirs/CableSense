import unittest
import os
from src.ai_model import CableDiagnosticModel, load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor
from src.sensors.gps_sensor import GPSSensor

class TestCableDiagnosticDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model_path = 'models/cable_model.joblib'

    def test_model_predictions_trained(self):
        if os.path.exists(self.model_path):
            model = CableDiagnosticModel(model_path=self.model_path)
            status = model.predict({
                'gpr_amplitude': 0.1,
                'pd_intensity': 0.1,
                'soil_resistivity': 500,
                'burial_depth': 1.5
            })
            self.assertEqual(status, 'Healthy')
        else:
            self.skipTest("Trained model not found")

    def test_sensors(self):
        gpr = GPRSensor()
        gps = GPSSensor()

        gpr_data = gpr.read_data()
        self.assertIn('gpr_amplitude', gpr_data)

        gps_data = gps.read_data()
        self.assertIn('latitude', gps_data)
        self.assertIn('longitude', gps_data)

if __name__ == '__main__':
    unittest.main()
