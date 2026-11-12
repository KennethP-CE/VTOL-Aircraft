void setup() {
  Serial.begin(115200); // Initialize USB Serial communication
  while (!Serial && millis() < 4000); // Wait for serial port to open
}

void loop() {
  // Check if data has been sent from the Raspberry Pi
  if (Serial.available() > 0) {
    String incomingString = Serial.readStringUntil('\n');
    incomingString.trim(); // Remove trailing newline/spaces
    
    // Echo back to the Pi
    Serial.print("Teensy received: ");
    Serial.println(incomingString);
  }
}