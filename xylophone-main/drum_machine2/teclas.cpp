#include "teclas.h"


Teclas::Teclas() {
  
}

void Teclas::initialize(){
  pca1 = Adafruit_PWMServoDriver(0x40);
  pca1.begin();
  pca1.setPWMFreq(50);  // Analog servos run at ~50 Hz updates

  key_startup();
}

void Teclas::play_key(int key, int vel){
  key = key - 1;
  if (delay_down[key] == 0){
    float angle =  map(vel, 0, 127, low_note_soft[key], low_note_hard[key]);
    pca1.writeMicroseconds(key, angle2PWM(angle, key));
//    pca1.writeMicroseconds(key, angle2PWM(85 + low_note[key], key));
    delay_down[key] = millis() + delay1;
  }
  
}

void Teclas::key_up(int key){
  delay_down[key] = 0;
  pca1.writeMicroseconds(key, angle2PWM(high_note[key], key));
//  pca1.writeMicroseconds(key, angle2PWM(70, key));
}

void Teclas::key_startup(){
    for(int key = 0; key< NTECLAS; key++){
        delay(1000);
        pca1.writeMicroseconds(key, angle2PWM(high_note[key], key));
    }
}


void Teclas::play_loop(){
  for(int i = 0; i<NTECLAS; i++){
      if ((delay_down[i] != 0) and (millis() > delay_down[i])){
        key_up(i);
      }
    }
}

int Teclas::angle2PWM(double x, int i) { /* function angle2PWM */
                                 ////Convert joint angle into pwm command value
  x += CORECTOR[i];
  
  int imp = (x - MIN_ANG[i]) * (MAX_IMP[i] - MIN_IMP[i]) / (MAX_ANG[i] - MIN_ANG[i]) + MIN_IMP[i];
  imp = max(imp, MIN_IMP[i]);
  imp = min(imp, MAX_IMP[i]);

  return imp;
}
