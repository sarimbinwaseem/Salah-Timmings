#!/opt/python/3.11.4/bin/python3.11

"""Hardware module"""

import time
from RPi import GPIO


class Hardware:
	"""docstring for Hardware"""

	def __init__(self, display_loop, stime, display, draw):
		super().__init__()

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
			callback=lambda PIN: display_loop(PIN, stime, display, draw),
		)

	def buzz(self, iterations: int) -> None:
		if iterations == 1:
			GPIO.output(self._BUZZER, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(self._BUZZER, GPIO.LOW)

		for _ in range(iterations):
			GPIO.output(self._BUZZER, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(self._BUZZER, GPIO.LOW)
			time.sleep(1)
