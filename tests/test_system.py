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
        self.assertEqual(model.predict({'pd_intensity': 0.1, 'gpr_amplitude': 0.1}), 'Healthy')

        # Test Insulation Failure
        self.assertEqual(model.predict({'pd_intensity': 0.9, 'gpr_amplitude': 0.1}), 'Insulation Failure')

    def test_model_predictions_trained(self):
        if os.path.exists(self.model_path):
            model = CableDiagnosticModel(model_path=self.model_path)

            # Test healthy
            status = model.predict({
                'gpr_amplitude': 0.1,
                'pd_intensity': 0.1,
                'soil_resistivity': 500,
                'burial_depth': 1.5
            })
            self.assertEqual(status, 'Healthy')

            # Test Insulation Failure
            status = model.predict({
                'gpr_amplitude': 0.1,
                'pd_intensity': 0.9,
                'soil_resistivity': 500,
                'burial_depth': 1.5
            })
            self.assertEqual(status, 'Insulation Failure')
        else:
            self.skipTest("Trained model not found for testing")

    def test_sensors(self):
        gpr = GPRSensor()
        acoustic = AcousticSensor()

        gpr_data = gpr.read_data()
        self.assertIn('gpr_amplitude', gpr_data)
        self.assertIn('soil_resistivity', gpr_data)

        acoustic_data = acoustic.read_data()
        self.assertIn('pd_intensity', acoustic_data)

if __name__ == '__main__':
    unittest.main()
