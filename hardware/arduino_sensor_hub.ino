/*
  Arduino Sensor Hub for Cable Diagnostics
  Reads analog values from GPR and Acoustic sensors and sends them to Raspberry Pi via Serial.
*/

const int GPR_PIN = A0;
const int ACOUSTIC_PIN = A1;

void setup() {
  Serial.begin(9600);
  pinMode(GPR_PIN, INPUT);
  pinMode(ACOUSTIC_PIN, INPUT);
}

void loop() {
  // Read sensors (0-1023)
  int gprValue = analogRead(GPR_PIN);
  int acousticValue = analogRead(ACOUSTIC_PIN);

  // Convert to 0.0 - 1.0 range
  float gprNorm = gprValue / 1023.0;
  float acousticNorm = acousticValue / 1023.0;

  // Send as JSON-like string
  Serial.print("{\"gpr_amplitude\":");
  Serial.print(gprNorm);
  Serial.print(",\"pd_intensity\":");
  Serial.print(acousticNorm);
  Serial.println("}");

  delay(1000); // Send data every second
}
