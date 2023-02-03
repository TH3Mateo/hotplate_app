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