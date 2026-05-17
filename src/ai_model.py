import os
import joblib
import pandas as pd

class CableDiagnosticModel:
    def __init__(self, model_path=None):
        self.model_path = model_path
        self.model = None
        if model_path and os.path.exists(model_path):
            self.model = joblib.load(model_path)
            print(f"Model loaded from {model_path}")
        else:
            print("Warning: No model found or loaded. Using fallback logic.")

    def predict(self, sensor_data):
        """
        Predicts the status of the cable based on sensor data.
        :param sensor_data: Dictionary containing data from various sensors.
        :return: A string indicating the status.
        """
        if self.model:
            # Prepare input data for the model
            df = pd.DataFrame([sensor_data])
            # Ensure columns are in the correct order
            X = df[['gpr', 'acoustic']]
            prediction = self.model.predict(X)
            return prediction[0]
        else:
            # Fallback logic
            acoustic_value = sensor_data.get('acoustic', 0)
            gpr_value = sensor_data.get('gpr', 0)

            if acoustic_value > 0.8 or gpr_value > 0.8:
                return 'Fault Detected'
            elif acoustic_value > 0.5 or gpr_value > 0.5:
                return 'Degraded'
            else:
                return 'Healthy'

def load_model(model_path):
    """
    Loads the AI model from the specified path.
    """
    return CableDiagnosticModel(model_path)
