#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess
import time
import picamera


GPIO.setmode(GPIO.BOARD)

irin = 12
flash =13

GPIO.setwarnings(False)

GPIO.setup(irin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(flash,GPIO.OUT)

for x in range(0, 9):
         GPIO.output(flash,1)
         time.sleep(0.2)
         GPIO.output(flash,0)
         time.sleep(0.2)

while True:
     if GPIO.input(irin):
          print('Detect')
          
          subprocess.call(["python", "/root/servo.py"])

          time.sleep(2)
          
          GPIO.output(flash,1)		  
          subprocess.call(["python", "/root/cam.py"])
          GPIO.output(flash,0)
          subprocess.call(["python", "/root/sendpic.py"])
		  
          GPIO.cleanup()
          break

     pass
GPIO.cleanup()


