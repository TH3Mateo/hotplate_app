#line 1 "c:\\Users\\M\\Desktop\\Arduino_code\\smd_iron\\functions.h"


int calc_temp(float V);
int map_f(double x, long in_min, long in_max, int out_min, int out_max);
void heat(double temp, int target, uint8_t writepin);
