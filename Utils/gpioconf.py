#!/opt/python/3.11.4/bin/python3.11

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

BUZZER = 25
BUTTON = 24
FLAG = True

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


