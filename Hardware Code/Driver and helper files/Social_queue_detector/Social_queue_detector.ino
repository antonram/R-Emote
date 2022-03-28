#include <SPI.h>
#include <SD.h>
File myFile;  //Creating file object


///Ultrasonic rangefinder///
#define echoPin 31 // attach pin D Arduino to pin Echo of HC-SR04
#define trigPin 33 //attach pin D3 Arduino to pin Trig of HC-SR04
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

///Sound sensor///
int sound_sensor_pin = A14;


void setup() {
  ///Serial start up///
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Sound sensor Test"); // print some text in Serial Monitor
  Serial.println("with Arduino Mega");
  
  ///Ultrasonic sensor///
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT 
  #define ULTRASONIC_RANGEFINDER_THRES 100 

  ///Sound Sensor///
  pinMode(sound_sensor_pin, INPUT);
  #define SOUND_SENSOR_THRES 108
}
void loop() {

  ///Sound level detection
  digitalWrite(sound_sensor_pin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(sound_sensor_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sound_sensor_pin, LOW);
  int noise_level = analogRead(sound_sensor_pin);
 
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  //Serial.println(distance);
  //Serial.println(noise_level);

  if( abs(noise_level-SOUND_SENSOR_THRES) > 6 && distance < ULTRASONIC_RANGEFINDER_THRES){
    Serial.println("I'm talking to someone.");
    //start recording audio and save it to SD card
    //take picture and save it to SD card
    //Send files to SW side (server, MQTT, etc)
  }  
  
  
}
