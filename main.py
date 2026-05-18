import time
import os
from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor
from src.sensors.gps_sensor import GPSSensor
from src.database import init_db, add_entry

def log_alert(status, location):
    os.makedirs('data', exist_ok=True)
    with open('data/alerts.log', 'a') as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] CRITICAL ALERT: {status} at Lat:{location['latitude']}, Lon:{location['longitude']}\n")

def main():
    print("Initializing Enhanced Cable Diagnostic Device with Database and Alerting...")
    init_db()

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
        while iterations < 10:
            combined_sensor_data = {}
            location = {}
            for sensor in sensors:
                data = sensor.read_data()
                if sensor.sensor_type == 'gps':
                    location = data
                elif isinstance(data, dict):
                    combined_sensor_data.update(data)

            status = model.predict(combined_sensor_data)
            timestamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

            # Save to Database
            add_entry(timestamp, location['latitude'], location['longitude'], status, combined_sensor_data)

            # Alerting for critical faults
            if any(fault in status for fault in ['Failure', 'Break', 'Intrusion']):
                log_alert(status, location)
                print(f"!!! CRITICAL ALERT: {status} detected !!!")

            print(f"[{timestamp}] STATUS: {status} at {location}")

            time.sleep(1)
            iterations += 1

        print("Cycle completed. Data saved to SQLite database and alerts logged to data/alerts.log.")
    except KeyboardInterrupt:
        print("\nStopping device...")

if __name__ == "__main__":
    main()
