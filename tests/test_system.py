import unittest
import os
from src.ai_model import CableDiagnosticModel, load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor

class TestCableDiagnosticDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model_path = 'models/cable_model.joblib'

    def test_model_predictions_fallback(self):
        # Test without model file (fallback logic)
        model = CableDiagnosticModel(model_path='non_existent.joblib')

        # Test healthy
        self.assertEqual(model.predict({'acoustic': 0.1, 'gpr': 0.1}), 'Healthy')

        # Test fault
        self.assertEqual(model.predict({'acoustic': 0.1, 'gpr': 0.9}), 'Fault Detected')

    def test_model_predictions_trained(self):
        if os.path.exists(self.model_path):
            model = CableDiagnosticModel(model_path=self.model_path)

            # The trained model should behave similarly to our generation logic
            self.assertEqual(model.predict({'acoustic': 0.1, 'gpr': 0.1}), 'Healthy')
            self.assertEqual(model.predict({'acoustic': 0.9, 'gpr': 0.1}), 'Fault Detected')
        else:
            self.skipTest("Trained model not found for testing")

    def test_sensors(self):
        gpr = GPRSensor()
        acoustic = AcousticSensor()

        self.assertEqual(gpr.sensor_type, 'gpr')
        self.assertEqual(acoustic.sensor_type, 'acoustic')

        val = gpr.read_data()
        self.assertTrue(0 <= val <= 1)

        val = acoustic.read_data()
        self.assertTrue(0 <= val <= 1)

if __name__ == '__main__':
    unittest.main()
