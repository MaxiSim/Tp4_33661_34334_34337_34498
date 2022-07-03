/*
simple drum machine for the pca9685 servos on channels 14 and 15
*/

#include "teclas.h"

//Parameters
int note = 0;
int vel = 0;
int data1 = 0;
int data2 = 0;
int data3 = 0;
int data4 = 0;
int data5 = 0;

Teclas keyboard = Teclas();

void setup() {
  //Init Serial USB
  keyboard.initialize();
  Serial.begin(115200);
  Serial.println("Initialize System");
  
}


void loop() {
  if (Serial.available()>4){
    data1 = Serial.read() - 48;
    data2 = Serial.read() - 48;
    data3 = Serial.read() - 48;
    data4 = Serial.read() - 48;
    data5 = Serial.read() - 48;
    note = data1*10 + data2;
    vel = data3*100 + data4*10 + data5;
//    Serial.print(note);
//    Serial.print("     ");
//    Serial.println(vel);
    keyboard.play_key(note, vel);
  }

//   for (int i = 0; i < 18; i++){
//      keyboard.play_key(i);
//      delay(50);
//      keyboard.key_up(i);
//      delay(100);
//   }

  keyboard.play_loop();
}
