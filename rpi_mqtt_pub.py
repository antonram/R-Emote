'''
Publish sound sensor information - RPi 1
'''

import paho.mqtt.client as mqtt
import requests
import sys

import grovepi



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    # RPi doesn't subscribe to anything



if __name__ == '__main__':
    # connect to MQTT broker
    client = mqtt.Client()
    #client.on_message = on_message
    client.on_connect = on_connect
    '''
    
    CHANGE HOST, DOESN'T WORK!!!!!!
    
    '''
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    # Connect the Grove Sound Sensor to analog port A0
    # SIG,NC,VCC,GND
    sound_sensor = 0

    grovepi.pinMode(sound_sensor,"INPUT")


    # constantly get data and publish it
    while True:
        try:
            sound_data = grovepi.analogRead(sound_sensor)
            client.publish('rpi1/sound_sensor', sound_data)

            
            time.sleep(.1)

        except IOError:
            print ("Error")

        except KeyboardInterrupt:
            # Gracefully shutdown on Ctrl-C
            break