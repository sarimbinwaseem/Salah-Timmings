#!/opt/python/3.11.4/bin/python3.11

import sys
import time
import RPi.GPIO as GPIO


class Hardware:
    """docstring for Hardware"""

    def __init__(self, display_loop, stime, display):
        super(Hardware, self).__init__()

        GPIO.setmode(GPIO.BCM)
        self._BUZZER = 25
        self._BUTTON = 24
        self._FLAG = True

        GPIO.setup(self._BUZZER, GPIO.OUT)
        GPIO.output(self._BUZZER, GPIO.LOW)
        GPIO.setup(self._BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(
            self._BUTTON,
            GPIO.RISING,
            callback=lambda PIN: display_loop(
                PIN, stime, display
            )
        )

    def buzz(self, iterations: int):
        if iterations == 1:
            GPIO.output(self._BUZZER, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self._BUZZER, GPIO.LOW)

        for _ in range(iterations):
            GPIO.output(self._BUZZER, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self._BUZZER, GPIO.LOW)
            time.sleep(1)

    def my_callback(self, function):
        function()
