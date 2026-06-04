import sys
import os
import json
from functools import wraps
from flask import Flask, jsonify, send_from_directory, request

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor
from src.sensors.gps_sensor import GPSSensor
from src.sensors.serial_sensor import SerialSensorBridge
from src.database import get_history
from src.logger import system_log, audit_log

app = Flask(__name__, static_folder='../static')

# Basic Security: Token-based authentication
API_TOKEN = os.environ.get('CABLE_API_TOKEN', 'cable-secure-token-2024')

def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('X-API-Token')
        if token != API_TOKEN:
            audit_log.warning(f"Unauthorized access attempt from {request.remote_addr}")
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

model = load_model('models/cable_model.joblib')
hardware = SerialSensorBridge()
sensors = [GPRSensor(), AcousticSensor(), GPSSensor()]

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/status')
def get_status():
    combined_sensor_data = {}
    location = {}

    # Try hardware first
    hw_data = hardware.read_data()
    if hw_data:
        combined_sensor_data.update(hw_data)

    for sensor in sensors:
        data = sensor.read_data()
        if sensor.sensor_type == 'gps':
            location = data
        elif isinstance(data, dict):
            for key, val in data.items():
                if key not in combined_sensor_data:
                    combined_sensor_data[key] = val

    status = model.predict(combined_sensor_data)
    return jsonify({
        'status': status,
        'sensor_data': combined_sensor_data,
        'location': location
    })

@app.route('/api/history')
@require_token
def api_history():
    audit_log.info(f"History accessed by {request.remote_addr}")
    return jsonify(get_history())

@app.route('/api/ar-overlay')
@require_token
def get_ar_overlay():
    combined_sensor_data = hardware.read_data() or {}
    for sensor in sensors:
        if sensor.sensor_type != 'gps':
            data = sensor.read_data()
            for key, val in data.items():
                if key not in combined_sensor_data:
                    combined_sensor_data[key] = val

    depth = combined_sensor_data.get('burial_depth', 1.0)
    status = model.predict(combined_sensor_data)

    return jsonify({
        'overlay_elements': [
            {
                'type': 'cable_projection',
                'depth_m': depth,
                'label': f'Cable: {status}',
                'color': 'red' if 'Failure' in status or 'Break' in status else 'green'
            }
        ]
    })

if __name__ == '__main__':
    system_log.info("Starting API Server...")
    app.run(host='0.0.0.0', port=5000, debug=False)
