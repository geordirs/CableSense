# Cable Diagnostic Device - User & Hardware Guide

## 🚀 Quick Start (Demo Mode)
If you want to see the project running immediately on your computer:
1. Ensure you have Python installed.
2. Run the automated demo script:
   ```bash
   ./run_demo.sh
   ```
3. Open your browser and go to: `http://localhost:5000`

---

## 1. Hardware Setup
To build the physical device, you will need:
- **Computing Unit**: Raspberry Pi 4 (4GB+ recommended).
- **GPR Sensor**: Ground Penetrating Radar module with serial/USB interface.
- **Acoustic Sensor**: High-sensitivity piezoelectric sensor for Partial Discharge detection.
- **GPS Module**: USB or GPIO-based GPS receiver.

### Connection Diagram:
- Connect the GPR module via USB.
- Connect the Acoustic sensor to the ADC pins (using an MCP3008 if using a Raspberry Pi).
- Connect the GPS module to the UART pins or USB.

## 2. Software Installation
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Re-train the AI model:
   ```bash
   python3 src/data_generator.py
   python3 src/train_model.py
   ```

## 3. Operation
### Running the Diagnostic Device
To start the real-time diagnostic loop and save data:
```bash
python3 main.py
```

### Starting the Web Dashboard
To view results in a browser:
1. Start the API:
   ```bash
   python3 src/api.py
   ```
2. Open `http://localhost:5000` in your browser.

## 4. GIS Integration
To export the collected diagnostic history for GIS software (QGIS, ArcGIS):
```bash
python3 src/utils/exporter.py
```
This will generate `data/diagnostics.geojson`.

## 5. AR Interface
The API provides an endpoint for Augmented Reality overlays at `/api/ar-overlay`. This can be consumed by a mobile app or AR glasses to project cable information onto the real-world view.
