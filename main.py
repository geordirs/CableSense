import time
import os
from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor

def main():
    print("Initializing AI-Powered Universal Cable Diagnostic Device...")

    # Path to the trained model
    model_path = 'models/cable_model.joblib'

    if not os.path.exists(model_path):
        print(f"Warning: Model file {model_path} not found. Some functionality may be limited.")

    # Load model
    model = load_model(model_path)

    # Initialize sensors
    sensors = [
        GPRSensor(),
        AcousticSensor()
    ]

    print("Starting diagnostic loop (Press Ctrl+C to stop)...")
    try:
        # For demonstration purposes, we will run only 5 iterations in non-interactive environments
        # In a real device, this would be 'while True:'
        iterations = 0
        while iterations < 5:
            sensor_data = {}
            for sensor in sensors:
                sensor_data[sensor.sensor_type] = sensor.read_data()

            # AI Diagnosis
            status = model.predict(sensor_data)

            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Readings: {sensor_data} -> Status: {status}")

            time.sleep(1)
            iterations += 1

        print("Demo completed.")
    except KeyboardInterrupt:
        print("\nStopping device...")

if __name__ == "__main__":
    main()
