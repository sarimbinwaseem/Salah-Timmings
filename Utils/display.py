"""Display module"""

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Display:
	"""All display related stuff"""

	def __init__(self):
		super().__init__()
		self.RST = None

		# Note the following are only used with SPI:
		self.DC = 23
		self.SPI_PORT = 0
		self.SPI_DEVICE = 0
		self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
		self.X = 0

		try:
			self.font = ImageFont.truetype("Fonts/TheImpostor.ttf", 20)
		except FileNotFoundError:
			self.font = ImageFont.load_default()

	def get_disp_dimensions(self) -> tuple:
		return (self.disp.width, self.disp.height)

	def begin_display(self):
		"""Initializing the display object."""

		try:
			self.disp.begin()
		except OSError:
			# Display may not be connected.
			return -1

		# Clear display.
		self.disp.clear()
		self.disp.display()

		return 0

	def set_image_support(self):
		"""Getting the dimensions of the display and
		setting the margins."""

		_, height = self.get_disp_dimensions()

		# First define some constants to allow easy resizing of shapes.
		self.PADDING = 3
		self.TOP = self.PADDING
		self.BOTTOM = height - self.PADDING
		# Move left to right keeping track of the current x position for drawing shapes.
		self.X = 0

	def create_blank_image(self) -> Image.Image:
		"""Create blank image to draw the timings on."""

		width, height = self.get_disp_dimensions()
		# Create blank image for drawing.
		# Make sure to create image with mode '1' for 1-bit color.

		self.IMAGE = Image.new("1", (width, height))


	def create_draw(self) -> ImageDraw.ImageDraw:
		"""Create draw object to draw timings on image."""

		# rawing object to draw on image.
		self.DRAW = ImageDraw.Draw(self.IMAGE)


	def draw_rectangle(self):
		"""Drawing black i.e. 0 fill rectangle to get display started."""

		width, height = self.get_disp_dimensions()

		# Draw a black filled box to clear the image.
		self.DRAW.rectangle((0, 0, width, height), outline=0, fill=0)

	def create_image(self, current_time, next_salah_time) -> None:
		"""Creating image of timings to show."""


		self.DRAW.text((self.X, self.TOP), current_time, font=self.font, fill=255)

		self.DRAW.text((self.X, self.TOP + 28), next_salah_time, font=self.font, fill=255)

	def display_image(self) -> None:
		"""Display the created image."""


		self.disp.image(self.IMAGE)
		self.disp.display()

	def clear(self) -> None:
		"""Clear the display."""

		self.disp.clear()
		self.disp.display()
