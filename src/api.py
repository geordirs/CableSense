import sys
import os
import json

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from src.ai_model import load_model
from src.sensors.gpr_sensor import GPRSensor
from src.sensors.acoustic_sensor import AcousticSensor
from src.sensors.gps_sensor import GPSSensor

app = Flask(__name__, static_folder='../static')
CORS(app)

model = load_model('models/cable_model.joblib')
sensors = [
    GPRSensor(),
    AcousticSensor(),
    GPSSensor()
]

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/status')
def get_status():
    combined_sensor_data = {}
    location = {}
    for sensor in sensors:
        data = sensor.read_data()
        if sensor.sensor_type == 'gps':
            location = data
        else:
            combined_sensor_data.update(data)

    status = model.predict(combined_sensor_data)
    return jsonify({
        'status': status,
        'sensor_data': combined_sensor_data,
        'location': location
    })

@app.route('/api/history')
def get_history():
    history_file = 'data/history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return jsonify(json.load(f))
    return jsonify([])

@app.route('/api/ar-overlay')
def get_ar_overlay():
    # Simulate AR metadata for visualization
    combined_sensor_data = {}
    for sensor in sensors:
        if sensor.sensor_type != 'gps':
            combined_sensor_data.update(sensor.read_data())

    depth = combined_sensor_data.get('burial_depth', 1.0)
    status = model.predict(combined_sensor_data)

    return jsonify({
        'overlay_elements': [
            {
                'type': 'cable_projection',
                'depth_m': depth,
                'label': f'Cable: {status}',
                'color': 'red' if 'Failure' in status or 'Break' in status else 'green'
            },
            {
                'type': 'soil_info',
                'resistivity': combined_sensor_data.get('soil_resistivity', 500),
                'label': 'Soil Condition: Normal'
            }
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
