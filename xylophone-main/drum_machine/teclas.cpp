#include "teclas.h"


Teclas::Teclas() {
  
}

void Teclas::initialize(){
  pca1 = Adafruit_PWMServoDriver(0x41);
  pca2 = Adafruit_PWMServoDriver(0x40);
  pca1.begin();
  pca1.setPWMFreq(50);  // Analog servos run at ~50 Hz updates
  pca2.begin();
  pca2.setPWMFreq(50);  // Analog servos run at ~50 Hz updates

  key_startup();
  
//  
  
}

void Teclas::play_key(int key, int vel){
  key = key - 1;
  if (delay_down[key] == 0){
    float angle =  map(vel, 0, 127, low_note_soft[key], low_note_hard[key]);
    if (key < 9){
      pca1.writeMicroseconds(key, angle2PWM(angle, key));
    } else {
      pca2.writeMicroseconds(key - 9, angle2PWM(angle, key));
    }
    delay_down[key] = millis() + delay1;
  }
  
}

void Teclas::calib(int key, float angle){
  key = key - 1;
  if (delay_down[key] == 0){
    float angle2 =  low_note_hard[key] + angle/10;
    Serial.println(angle2);
    if (key < 9){
      pca1.writeMicroseconds(key, angle2PWM(angle2, key));
    } else {
      pca2.writeMicroseconds(key - 9, angle2PWM(angle2, key));
    }
    delay_down[key] = millis() + delay1;
  }
  
}

void Teclas::key_up(int key){
  delay_down[key] = 0;
  if (key < 9){
    pca1.writeMicroseconds(key, angle2PWM(high_note[key], key));
  } else {
    pca2.writeMicroseconds(key - 9, angle2PWM(high_note[key], key));
  }
}

void Teclas::key_startup(){
    for(int key = 0; key< NTECLAS; key++){
        delay(100);
        if (key < 9){
            pca1.writeMicroseconds(key, angle2PWM(high_note[key], key));
        } else {
            pca2.writeMicroseconds(key - 9, angle2PWM(high_note[key], key));
        }
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
