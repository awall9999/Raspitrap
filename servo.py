#!/usr/bin/python

import time
import RPi.GPIO as GPIO

print (GPIO.VERSION)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)
p.start(7.5)


p.ChangeDutyCycle(1)
time.sleep(0.3)

#p.ChangeDutyCycle(3.5)
#time.sleep(0.3)

p.stop()
GPIO.cleanup()





