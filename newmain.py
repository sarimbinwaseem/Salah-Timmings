import sys
import threading
import time as timelib
# import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from Utils.salahtime import SalahTime

print("Salah Timmings imported...")
stime = SalahTime()

thread = threading.Thread(target = stime.check_changes)
thread.start()

class Display():
	"""docstring for Display"""
	def __init__(self):
		super(Display, self).__init__()
		self.RST = None

		# Note the following are only used with SPI:
		self.DC = 23
		self.SPI_PORT = 0
		self.SPI_DEVICE = 0
		self.disp = Adafruit_SSD1306.SSD1306_128_64(rst = RST)
	try:
		disp.begin()
	except OSError:
		print("Display module may be not be connected!. Exiting...")
		stime.check_changes_flag = False
		thread.join()
		sys.exit(1)

	# Clear display.
	disp.clear()
	disp.display()