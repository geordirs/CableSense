import time
import os
from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor

def main():
    print("Initializing Enhanced AI-Powered Universal Cable Diagnostic Device...")

    # Path to the trained model
    model_path = 'models/cable_model.joblib'

    # Load model
    model = load_model(model_path)

    # Initialize sensors
    sensors = [
        GPRSensor(),
        AcousticSensor()
    ]

    print("Starting diagnostic loop (Press Ctrl+C to stop)...")
    try:
        # For demonstration purposes, we will run only 5 iterations
        iterations = 0
        while iterations < 5:
            # Collect data from all sensors into a single flattened dictionary
            combined_sensor_data = {}
            for sensor in sensors:
                data = sensor.read_data()
                if isinstance(data, dict):
                    combined_sensor_data.update(data)
                else:
                    combined_sensor_data[sensor.sensor_type] = data

            # AI Diagnosis
            status = model.predict(combined_sensor_data)

            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Sensor Data: {combined_sensor_data}")
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] STATUS: {status}")
            print("-" * 40)

            time.sleep(1)
            iterations += 1

        print("Demo completed.")
    except KeyboardInterrupt:
        print("\nStopping device...")

if __name__ == "__main__":
    main()
