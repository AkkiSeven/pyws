import serial
import time


arduino = serial.Serial('COM5',9600)
time.sleep(2)
print(" Enter 1 to tuern on 0 to turn off")

while 1:
  dataFromUser=input()
  if dataFromUser=='1':
      arduino.write(b'1')
      print("LED ON")
  elif dataFromUser=='0':
      arduino.write(b'0')
      print("LED OFF")

