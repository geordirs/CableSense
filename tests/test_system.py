import unittest
from src.ai_model import CableDiagnosticModel, load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor

class TestCableDiagnosticDevice(unittest.TestCase):
    def test_model_predictions(self):
        model = CableDiagnosticModel()

        # Test healthy
        self.assertEqual(model.predict({'acoustic': 0.1, 'gpr': 0.1}), 'Healthy')

        # Test degraded
        self.assertEqual(model.predict({'acoustic': 0.6, 'gpr': 0.1}), 'Degraded')

        # Test fault
        self.assertEqual(model.predict({'acoustic': 0.1, 'gpr': 0.9}), 'Fault Detected')

    def test_sensors(self):
        gpr = GPRSensor()
        acoustic = AcousticSensor()

        self.assertEqual(gpr.sensor_type, 'gpr')
        self.assertEqual(acoustic.sensor_type, 'acoustic')

        val = gpr.read_data()
        self.assertTrue(0 <= val <= 1)

        val = acoustic.read_data()
        self.assertTrue(0 <= val <= 1)

    def test_load_model(self):
        model = load_model('dummy_path')
        self.assertIsInstance(model, CableDiagnosticModel)

if __name__ == '__main__':
    unittest.main()
