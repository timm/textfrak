import time
import serial

ser = serial.Serial('/dev/cu.usbserial-DN01AAWR', 9600)


while True:
    message = ser.readline()
    print(message)