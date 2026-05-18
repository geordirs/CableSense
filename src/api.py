import sys
import os

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

# Initialize system components
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
