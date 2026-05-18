# Cable Diagnostic Device - User & Hardware Guide

## 🚀 Quick Start (Demo Mode)
1. Run the automated demo: `./run_demo.sh`
2. Open `http://localhost:5000`

---

## 1. Hardware Assembly (Arduino + Raspberry Pi)
For real-world testing, use an Arduino as a sensor hub:
1. **Arduino Firmware**: Flash `hardware/arduino_sensor_hub.ino` to an Arduino Uno/Nano.
2. **Wiring**:
   - GPR Sensor -> Arduino Pin A0
   - Acoustic Sensor -> Arduino Pin A1
3. **Connection**: Connect Arduino to Raspberry Pi via USB.
4. **Software Configuration**: The system automatically attempts to connect to `/dev/ttyACM0`.

## 2. Security & Auditing
- The API is protected by a token. Use the header `X-API-Token: cable-secure-token-2024` for authenticated requests.
- Audit logs are stored in `logs/audit.log`.
- Refer to `SECURITY.md` for full security guidelines.

## 3. Deployment (Docker)
To deploy the system in a production environment:
```bash
docker-compose up -d
```
This will start the API server and persist data/logs in the local directory.

## 4. AI Training Pipeline
If you need to update the model with new data:
```bash
python3 src/data_generator.py
python3 src/train_model.py
```

## 5. GIS & Reporting
Export collected diagnostics to GeoJSON:
```bash
python3 src/utils/exporter.py
```
Open `data/diagnostics.geojson` in QGIS or ArcGIS.
