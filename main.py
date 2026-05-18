import time
import os
import json
from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor
from src.sensors.gps_sensor import GPSSensor

def save_to_history(entry):
    history_file = 'data/history.json'
    history = []
    if os.path.exists(history_file):
        try:
            with open(history_file, 'r') as f:
                history = json.load(f)
        except json.JSONDecodeError:
            history = []

    history.append(entry)
    # Keep only last 100 entries for the prototype
    history = history[-100:]

    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)

def main():
    print("Initializing GPS-Integrated Enhanced Cable Diagnostic Device...")

    model_path = 'models/cable_model.joblib'
    model = load_model(model_path)

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

            status = model.predict(combined_sensor_data)

            entry = {
                'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                'location': location,
                'status': status,
                'sensor_data': combined_sensor_data
            }

            save_to_history(entry)

            print(f"[{entry['timestamp']}] STATUS: {status} at {location}")

            time.sleep(1)
            iterations += 1

        print("Demo completed. History saved to data/history.json")
    except KeyboardInterrupt:
        print("\nStopping device...")

if __name__ == "__main__":
    main()
