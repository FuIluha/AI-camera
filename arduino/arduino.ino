#include <Servo.h>

Servo servoH;
Servo servoV;

void setup() {
  servoH.attach(9);
  servoV.attach(8);
}

void loop() {
  servoH.write(0);
  servoV.write(180);
  delay(1000);

  servoH.write(180);
  servoV.write(0);
  delay(1000);
}
