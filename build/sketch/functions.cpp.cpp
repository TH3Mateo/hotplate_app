#line 1 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\functions.cpp"
#include <Arduino.h>

float R1 = 10000;
float logR2, R2, T;
int out = 0;
#define c1 1.009249522e-03
#define c2 2.378405444e-04
#define c3 2.019202697e-07

#line 10 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\functions.cpp"
int map_f(double x, long in_min, long in_max, int out_min, int out_max);
#line 15 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\functions.cpp"
int calc_temp(float V);
#line 23 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\functions.cpp"
void heat(double temp, int target, uint8_t writepin);
#line 14 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\main.ino"
void setup();
#line 21 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\main.ino"
void loop();
#line 10 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\functions.cpp"
int map_f(double x, long in_min, long in_max, int out_min, int out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

int calc_temp(float V)
{
  R2 = R1 * (1023.0 / (float)V - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2 * logR2 + c3 * logR2 * logR2 * logR2)) - 273.15;
  return T;
}

void heat(double temp, int target, uint8_t writepin)
{

  out = (map_f(temp, 0, target, 1024, 0) * pow((target / temp), 2)) / 5;
  if (out < 0)
  {
    out = 0;
  }
  analogWrite(writepin, out);
  // Serial.print("output: ");
  // Serial.println(out);
}
#line 1 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\main.ino"
#include <Arduino.h>
#include "functions.h"


uint8_t ThermistorPin = A0;
uint8_t heaterPin = 4;
int target;

int sum = 0;
double avg = 0;
uint8_t cnt = 0;
uint8_t del = 20;

void setup()
{
    Serial.begin(115200);
    pinMode(heaterPin, OUTPUT);
    pinMode(ThermistorPin, INPUT);
}

void loop()
{
    if (Serial.available() != 0)
    {
        target = Serial.readString().toInt();
        delay(300);
    }

    cnt++;
    sum = sum + analogRead(ThermistorPin);

    if (cnt == 20)
    {

        avg = sum / 20;
        sum = 0;
        cnt = 0;
        Serial.print("rd ");
        Serial.println(calc_temp(avg));
        // Serial.println(target);
        heat(calc_temp(avg), target, heaterPin);
    }
    delay(del);
}
