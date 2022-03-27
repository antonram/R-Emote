#include <SPI.h>
#include <SD.h>
File myFile;  //Creating file object

void setup() {
  Serial.begin(9600);

  // openvthe file
  myFile = SD.open("happy_frog.jpg");
  
  // if the file opened okay, write to it:
  if (myFile) {  
    
    while (myFile.available()) {
      Serial.print(myFile.read());
    }

    // close the file:
    myFile.close();

  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening happy_frog.jpg");
  }
  
}
void loop() {
  
}
