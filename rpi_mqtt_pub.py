'''
Publish sound sensor information - RPi 1
'''

import paho.mqtt.client as mqtt
import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    # RPi does subscribe to something
    client.subscribe('computer-color')
    client.message_callback_add('computer-color', computer_color_callback)
    
#Default message callback.
def on_message(client, userdata, msg):
    pass

def computer_color_callback(client, userdata, msg):
    print(msg.payload)
    colr = msg.payload
    if colr == b'Red':
       lcd.setRGB(255,0,0) 
    elif colr == b'Purple':
       lcd.setRGB(128,0,128) 
    elif colr == b'Yellow':
        lcd.setRGB(255,255,0) 
    elif colr == b'Gray':
        lcd.setRGB(128,128,128) 
    elif colr == b'Blue':
        lcd.setRGB(0,0,255)
    elif colr == b'Green':
        lcd.setRGB(0,255,0)
    
    
    


if __name__ == '__main__':
    # connect to MQTT broker
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    '''
    
    CHANGE HOST, DOESN'T WORK!!!!!!
    
    '''
    # testsystem1.westus2.azurecontainer.io
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()

    # Connect the Grove Sound Sensor to analog port A0
    # SIG,NC,VCC,GND
    sound_sensor = 0
    grovepi.pinMode(sound_sensor,"INPUT")
    
    


    # constantly get data and publish it
    while True:
        try:
            ultrasonic_ranger = 4
            distance = grovepi.ultrasonicRead(ultrasonic_ranger)
            if distance <= 92:
                sound_data = grovepi.analogRead(sound_sensor)
                client.publish('rpi1-sound_sensor', sound_data)

            
            time.sleep(.1)

        except IOError:
            print ("Error")

        except KeyboardInterrupt:
            # Gracefully shutdown on Ctrl-C}
            lcd.setText('')
            lcd.setRGB(0, 0, 0)
            break