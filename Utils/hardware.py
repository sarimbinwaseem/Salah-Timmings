#!/opt/python/3.11.4/bin/python3.11

"""Hardware module"""

import time
from RPi import GPIO


class Hardware:
	"""docstring for Hardware"""

	def __init__(self, display_loop = None, stime = None, display = None):
		super().__init__()

		GPIO.setmode(GPIO.BCM)
		self._BUZZER = 25
		self._BUTTON = 24

		GPIO.setup(self._BUZZER, GPIO.OUT)
		GPIO.output(self._BUZZER, GPIO.LOW)
		GPIO.setup(self._BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

		GPIO.add_event_detect(
			self._BUTTON,
			GPIO.RISING,
			callback=lambda PIN: display_loop(PIN, stime, display),
		)

	def buzz(self, iterations: int) -> None:
		"""Buzz the buzzer one or more times."""

		if iterations == 1:
			GPIO.output(self._BUZZER, GPIO.HIGH)
			time.sleep(3)
			GPIO.output(self._BUZZER, GPIO.LOW)

		else:
			for _ in range(iterations):
				GPIO.output(self._BUZZER, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(self._BUZZER, GPIO.LOW)
				time.sleep(1)

if __name__ == "__main__":
	hard = Hardware()
	hard.buzz(3)