# Shopping List & Hardware Connection Guide

## 🛒 Components to Buy

### 1. Main Controller
- **Raspberry Pi 4 Model B (4GB or 8GB RAM)**: The "brain" that runs the AI and the Web Server.
- **MicroSD Card (32GB+ Class 10)**: For the OS and project files.
- **Power Supply (5V 3A USB-C)**: For the Raspberry Pi.

### 2. Sensor Hub
- **Arduino Nano or Uno**: Used to read analog signals from the sensors and send them to the Pi.
- **USB Cable (Type B or Mini-USB)**: To connect the Arduino to the Pi.

### 3. Sensors
- **GPR Module (Ground Penetrating Radar)**: Entry-level modules like the *GPR-A series* or professional UWB (Ultra-Wideband) sensors.
- **Acoustic/Ultrasound Sensor**: *HC-SR04* (for basic distance/void detection) or specialized piezoelectric sensors for Partial Discharge detection.
- **GPS Module**: *u-blox NEO-6M* with antenna for location tracking.

### 4. Miscellaneous
- **Jumper Wires (Male-to-Male, Male-to-Female)**.
- **Breadboard** (for prototyping).
- **Weatherproof Enclosure**: To protect the electronics during field tests.

---

## 🔌 Wiring Guide

### Arduino to Sensors:
1. **GPR Module**:
   - VCC -> Arduino 5V
   - GND -> Arduino GND
   - Data Out -> Arduino Pin **A0**
2. **Acoustic Sensor**:
   - VCC -> Arduino 5V
   - GND -> Arduino GND
   - Signal -> Arduino Pin **A1**

### Raspberry Pi to Modules:
1. **Arduino Connection**:
   - Connect the Arduino USB port to any USB port on the Raspberry Pi. The system will automatically detect it at `/dev/ttyACM0`.
2. **GPS Module (via UART)**:
   - VCC -> Pi Pin 2 (5V)
   - GND -> Pi Pin 6 (GND)
   - TX -> Pi Pin 10 (RXD)
   - RX -> Pi Pin 8 (TXD)

---

## 🛠️ Assembly Steps
1. Flash the Arduino using `hardware/arduino_sensor_hub.ino`.
2. Connect the sensors to the Arduino as shown above.
3. Connect the Arduino and GPS to the Raspberry Pi.
4. Power up the Pi and run the software using `./run_demo.sh`. The system will prefer data from the Arduino if it is connected.
