import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Display:
	"""docstring for Display"""

	def __init__(self):
		super(Display, self).__init__()
		self.RST = None

		# Note the following are only used with SPI:
		self.DC = 23
		self.SPI_PORT = 0
		self.SPI_DEVICE = 0
		self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

		try:
			self.font = ImageFont.truetype("Fonts/TheImpostor.ttf", 20)
		except:
			self.font = ImageFont.load_default()


	def get_disp_dimensions(self) -> tuple:

		return (self.disp.width, self.disp.height)


	def begin_display(self):
		try:
			self.disp.begin()
		except OSError:
			# Display may not be connected.
			return -1

		else:
			# Clear display.
			disp.clear()
			disp.display()

	def create_blank_image(self) -> PIL.Image.Image:

		width, height = self.get_disp_dimensions()
		# Create blank image for drawing.
		# Make sure to create image with mode '1' for 1-bit color.

		image = Image.new("1", (width, height))

		return image

	def get_draw(self) -> PIL.ImageDraw.ImageDraw:
		#rawing object to draw on image.
		draw = ImageDraw.Draw(image)

		width, height = self.get_disp_dimensions()

		return draw

	def draw_rectangle(self, draw: PIL.ImageDraw.ImageDraw):
		# Draw a black filled box to clear the image.
		draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

	def draw_image(self, draw: PIL.ImageDraw.ImageDraw):
		