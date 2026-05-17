import time
from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor

def main():
    print("Initializing AI-Powered Universal Cable Diagnostic Device...")

    # Load model
    model = load_model('models/cable_model_v1.h5')

    # Initialize sensors
    sensors = [
        GPRSensor(),
        AcousticSensor()
    ]

    print("Starting diagnostic loop (Press Ctrl+C to stop)...")
    try:
        while True:
            sensor_data = {}
            for sensor in sensors:
                sensor_data[sensor.sensor_type] = sensor.read_data()

            # AI Diagnosis
            status = model.predict(sensor_data)

            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Readings: {sensor_data} -> Status: {status}")

            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopping device...")

if __name__ == "__main__":
    main()
