#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)


for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    print("On")
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)
    print("Off")
    time.sleep(0.2)


GPIO.cleanup()