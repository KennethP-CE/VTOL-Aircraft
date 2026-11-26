#include <string>
#include <Servo.h>

void setup() {
  myServo.attach(servoPin);
  Serial.begin(115200);
  while (!Serial && millis() < 4000);
}

void loop() {
  if (Serial.available() > 0) {
    String incomingString = Serial.readStringUntil('\n');
    incomingString.trim();
    int num = std::stoi(incomingString);
    Serial.print("Teensy received: ");
    Serial.println(incomingString);
    myServo.write(num);
    delay(15)
  }
}