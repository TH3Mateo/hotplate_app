#include <Arduino.h>

float R1 = 10000;
float logR2, R2, T;
int out = 0;
#define c1 1.009249522e-03
#define c2 2.378405444e-04
#define c3 2.019202697e-07

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