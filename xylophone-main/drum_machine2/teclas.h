#include <Adafruit_PWMServoDriver.h>

#define NTECLAS 12

#ifndef teclas_h
#define teclas_h
#include "Arduino.h" 
class Teclas {
public:
  Teclas();
  void initialize();
  void play_key(int key, int vel);
  void play_loop();
  void key_up(int key);
private:
  void key_startup();
  int angle2PWM(double x, int i);
  int delay1 = 50;
  int delay2 = 500;
  Adafruit_PWMServoDriver pca1;
  unsigned long delay_down[NTECLAS] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  int MIN_IMP[NTECLAS] = { 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500 };
  int MAX_IMP[NTECLAS] = { 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500 };
  int MIN_ANG[NTECLAS] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  int MAX_ANG[NTECLAS] = { 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180 };
//                                  1    2    3    4    5    6    7    8    9   10   11   12
  float CORECTOR[NTECLAS] =      {  0,  10,   2,  -1,   0,  -8,   5,   0,   5,   2,   1,  -4 };
  float low_note_soft[NTECLAS] = { 80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80 };
  float low_note_hard[NTECLAS] = { 85,  85,  85,  85,  85,  85,  85,  85,  85,  85,  85,  85 };
  float high_note[NTECLAS] =     { 70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70 };
};
#endif
