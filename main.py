import time
import os
from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor
from src.sensors.gps_sensor import GPSSensor

def main():
    print("Initializing GPS-Integrated Enhanced Cable Diagnostic Device...")

    # Path to the trained model
    model_path = 'models/cable_model.joblib'

    # Load model
    model = load_model(model_path)

    # Initialize sensors
    sensors = [
        GPRSensor(),
        AcousticSensor(),
        GPSSensor()
    ]

    print("Starting diagnostic loop (Press Ctrl+C to stop)...")
    try:
        iterations = 0
        while iterations < 5:
            combined_sensor_data = {}
            location = {}
            for sensor in sensors:
                data = sensor.read_data()
                if sensor.sensor_type == 'gps':
                    location = data
                elif isinstance(data, dict):
                    combined_sensor_data.update(data)
                else:
                    combined_sensor_data[sensor.sensor_type] = data

            # AI Diagnosis
            status = model.predict(combined_sensor_data)

            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] LOCATION: {location}")
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] STATUS: {status}")
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] DATA: {combined_sensor_data}")
            print("-" * 40)

            time.sleep(1)
            iterations += 1

        print("Demo completed.")
    except KeyboardInterrupt:
        print("\nStopping device...")

if __name__ == "__main__":
    main()
