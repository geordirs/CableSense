# Cable Monitoring Device

## Description

This project aims to develop a compact and advanced device for detecting and monitoring high-voltage cables, internet cables, fiber optics, and other services on utility poles in Latin America. The device will provide detailed information about cable type, voltage, and operational status.

## Features

- **Cable Detection:** Identifies high-voltage cables, internet cables, fiber optics, and others.
- **Voltage Measurement:** Real-time monitoring of cable voltage.
- **Operational Status:** Determines the operational status of the cables.
- **Detailed Data:** Specific information about cable type and condition.
- **User-Friendly Interface:** Easy to use for field engineers.

## Technologies Used

- **Hardware:** Raspberry Pi, specific sensors for cable detection and voltage measurement.
- **Software:** Python for device programming, libraries for sensor communication.
- **Artificial Intelligence:** AI models for predictive analysis of cable status and anomaly detection.

## Installation and Configuration

1. **Hardware:**
   - Connect sensors to the Raspberry Pi following the provided connection diagram.
   - Ensure all cables are securely connected and undamaged.

2. **Software:**
   - Clone the project repository:
     ```bash
     git clone https://github.com/yourusername/cable-monitoring.git
     ```
   - Install dependencies:
     ```bash
     cd cable-monitoring
     pip install -r requirements.txt
     ```

3. **AI Integration:**
   - Train the AI model with historical data on cable failures and status (see AI Training section).
   - Configure the model on the device:
     ```python
     from ai_model import load_model
     model = load_model('path/to/your/model')
     ```

## AI Training

1. **Data Collection:**
   - Collect historical data on cable status and failures.

2. **Model Training:**
   - Use an AI framework such as TensorFlow or PyTorch to train the model with the collected data.
   - Save the trained model in a compatible format.

3. **Model Integration:**
   - Load the model onto the device for real-time analysis.

## Agile Methodology

1. **Planning:**
   - Define requirements and establish a development timeline.

2. **Iterative Development:**
   - Implement features in short iterations.
   - Test and adjust the device in each iteration.

3. **Review and Adaptation:**
   - Review progress and adjust the plan as necessary.

## Contributions

Contributions to the project are welcome. Please submit a pull request or open an issue for suggestions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

