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
  LEDBuffer = [18][3]


  char colorSep = ','
  char LEDsep = ';'
  char fullStop = '.'
          
  Serial.begin(9600)
}

void loop() {
  if(Serial.available()){
    char c = Serial.read()
    if(c == LEDsep){
      updateBuffer(data)
      data = ""
    }else if(c == fullStop){
      writeLEDs()
      data = ""
    }else{
      data += c
    }
  }
}



void updateBuffer(string data){
  rest = data
  int LED = rest.substring(0, rest.indexOf(colorSep))
  String rest = rest.substring(rest.indexOf(colorSep))
  int R = rest.substring(0, rest.indexOf(colorSep))
  String rest = rest.substring(rest.indexOf(colorSep))
  int G = rest.substring(0, rest.indexOf(colorSep))
  String rest = rest.substring(rest.indexOf(colorSep))
  int B = rest

  LEDBuffer[LED] = [R, G, B]
}

  
void writeLEDs(){
  for(int i=0; i<sizeof(LEDBuffer); i++){
    analogWrite(i, LEDBuffer[i][0])
    analogWrite(i, LEDBuffer[i][1])
    analogWrite(i, LEDBuffer[i][2])
  }
}








