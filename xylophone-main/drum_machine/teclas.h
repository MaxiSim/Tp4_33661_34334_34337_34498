#include <Adafruit_PWMServoDriver.h>

#define NTECLAS 18

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
  void calib(int key, float angle);
private:
  void key_startup();
  int angle2PWM(double x, int i);
  int delay1 = 50;
  int delay2 = 500;
  Adafruit_PWMServoDriver pca1;
  Adafruit_PWMServoDriver pca2;
  unsigned long delay_down[NTECLAS] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  int MIN_IMP[NTECLAS] = { 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500 };
  int MAX_IMP[NTECLAS] = { 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500 };
  int MIN_ANG[NTECLAS] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
  int MAX_ANG[NTECLAS] = { 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180 };
//                                    1     2     3     4    5    6     7     8     9    10    11     12    13    14    15    16    17    18
  float CORECTOR[NTECLAS] =      {    0,   -7,   -1,  -14, -10, -15,    1,   -3,  -14, -6.8, -4.5, -12.5,   -4, -5.3,    7,   -7,   -6,    3 };
  float low_note_soft[NTECLAS] = { 44.5,   46, 40.9, 46.3,  44,  48, 44.6, 45.4, 41.9, 44.5, 44.7,    43, 41.6, 41.3, 40.7, 43.7, 44.5, 46.5 };
  float low_note_hard[NTECLAS] = {   39,   41,   36,   40,  40,  45, 38.6, 40.4, 38.9, 40.5, 41.7,    40, 38.7, 38.3, 37.7, 39.7, 40.5, 43.5 };
  float high_note[NTECLAS]=      {   57,   57,   57,   57,  57,  57,   57,   57,   57,   57,   57,    57,   57,   57,   57,   57,   57,   57 };
};
#endif
