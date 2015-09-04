/* Eric Salina
 * 9/4/2015
 * 
 * Reads a number corresponding to an LED from Serial, as well as
 * the corresponing RGB values. It then writes those values to an
 * RGB LED. For use in the ceiling GBRLED party light project.
 */


void setup() {
           //R  G  B  pins
  LEDs = [  [0, 1, 2]
            [3, 4, 5]
            [6, 7, 8]
            [9, 10, 11]
            [12, 13, 15]
            [16, 17, 18]
            [19, 20, 21]
            [22, 23, 24]
            [25, 26, 27]
            [28, 29, 30]
            [31, 32, 33]
            [34, 35, 36]
            [37, 38, 39]
            [40, 41, 42]
            [43, 44, 45]
            [46, 47, 48]
            [49, 50, 51]
            [52, 53, 54]
          ]
  Serial.begin(9600)
}

void loop() {
  while(Serial.available() > 0){
    int LED = Serial.parseInt();
    int r = Serial.parseInt();
    int g = Serial.parseInt();
    int b = Serial.parseInt();

    analogWrite(LEDs[LED][0], r);
    analogWrite(LEDs[LED][1], g);
    analogWrite(LEDs[LED][2], b);
  }

}
