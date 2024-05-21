#include <ArduinoJson.h>

class Servo {
  int pin;
  int position;

  public:
  Servo(int);
  void move(int);
};

Servo::Servo(int pin) {
  this->pin = pin;
  this->position = position;
}

void Servo::move(int position){
  this->position = position;
  int del = (7 * position) + 300;
  for (int pulseCounter = 0; pulseCounter <= 5; pulseCounter++){
      digitalWrite(pin, HIGH);
      delayMicroseconds(del);
      digitalWrite(pin, LOW);
      delay(5);
  }
}


void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}

Servo servoX(8);
Servo servoY(9);



void loop() {
  if (Serial.available()) {
    String jsonStr = Serial.readStringUntil('\n');
    StaticJsonDocument<256> doc;
    DeserializationError error = deserializeJson(doc, jsonStr);

    if (!error) {
      int x = int(doc["x"]);
      int y = int(doc["y"]);
      if (x <= 110 || x >= 0)
        servoX.move(x);
      if (y <= 110 || y >= 0)
        servoY.move(y);
    } else {
      Serial.println("Ошибка при разборе JSON");
    }
  }
}
