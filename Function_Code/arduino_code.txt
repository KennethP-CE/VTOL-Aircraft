#include <Servo.h>

int pinFL = 9;
int pinFR = 10;
int pinBL = 11;
int pinBR = 12;
float ti1 = 0.5;
float ti2 = 0.5;
float ti3 = 0.5;
float ti4 = 0.5;

class Motor
{
private:
  Servo esc;
  int pin;
  int minPulse = 1000;
  int maxPulse = 2000;

public:
  Motor(int p)
  {
    pin = p;
  }
  void Begin()
  {
    esc.attach(pin);
    esc.writeMicroseconds(minPulse);
    Serial.println("ESC initialized");
  }
  void setThrottle(int pulse)
  {
    if minPulse < pulse < maxPulse:
      esc.writeMicroseconds(pulse);
      Serial.println("On");
    else:
      Serial.println("PWM out of bounds")
  }
  void Off()
  {
    esc.writeMicroseconds(minPulse);
    Serial.println("Off");
  }
};

class Throttle
{
private:
  int dw;
  float strength
  public:
  Throttle(int dw, float str)
  {
    direction = dw;
    strength = str;
  }
  void ChangeThrottle(float amt)
  {
    strength = strength + amt;
  }
}

Throttle M1(1, ti1);
Throttle M2(2, ti2);
Throttle M3(3, ti3);
Throttle M4(4, ti4);
Motor FrontL(pinFL);
Motor FrontR(pinFR);
Motor BackL(pinBL);
Motor BackR(pinBR);

void setup()
{
  Serial.begin(9600)
  FrontL.Begin();
  FrontR.Begin();
  BackL.Begin();
  BackR.Begin();
  delay(5000);
  //FrontL.setThrottle(1200);
  //FrontR.setThrottle(1200);
  //BackL.setThrottle(1200);
  //BackR.setThrottle(1200);
  delay(1000);
  //FrontL.Off();
  //FrontR.Off();
  //BackL.Off();
  //BackR.Off();
}

void loop() {

}