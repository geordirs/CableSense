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
        :param sensor_data: Dictionary containing flattened data from all sensors.
        :return: A string indicating the status.
        """
        if self.model:
            # Prepare input data for the model
            df = pd.DataFrame([sensor_data])
            # Features must match the order during training
            features = ['gpr_amplitude', 'pd_intensity', 'soil_resistivity', 'burial_depth']
            # Fill missing features with default values if necessary
            for f in features:
                if f not in df.columns:
                    df[f] = 0.0

            X = df[features]
            prediction = self.model.predict(X)
            return prediction[0]
        else:
            # Fallback logic
            pd_intensity = sensor_data.get('pd_intensity', 0)
            gpr_amplitude = sensor_data.get('gpr_amplitude', 0)

            if pd_intensity > 0.75:
                return 'Insulation Failure'
            elif gpr_amplitude > 0.8:
                return 'Moisture Intrusion/Physical Break'
            elif pd_intensity > 0.4 or gpr_amplitude > 0.5:
                return 'Degraded'
            else:
                return 'Healthy'

def load_model(model_path):
    """
    Loads the AI model from the specified path.
    """
    return CableDiagnosticModel(model_path)
