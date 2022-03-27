#!/usr/bin/env python3
import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.reset_input_buffer()
    
    file = open("Frog.jpg","w")
    
    while True:
        if ser.in_waiting > 0:
            line = ser.readline()
            print(line) #Debugging/curious
            file.write(line)