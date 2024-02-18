"""Display module"""

# import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json


class Display:
	"""All display related stuff"""

	def __init__(self):
		super().__init__()

		# self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
		
		self.X: int = 0
		self.PADDING: int = 0
		self.TOP: int = 0
		self.BOTTOM: int = 0
		self.IMAGE = None
		self.DRAW = None

		self.WIDTH: int = 0
		self.HEIGHT: int = 0

		try:
			self.FONT = self.get_font("TheImpostor")
		except FileNotFoundError:
			self.FONT = ImageFont.load_default()

	def get_font(self, name: str) -> ImageFont.FreeTypeFont:
		"""returns font object for display."""

		name = name.replace(".ttf", "")

		with open("../Fonts/fontsandsizes.json", 'r') as file:
			fonts = json.loads(file.read())

		font_size = fonts[f"{name}.ttf"]
		font = ImageFont.truetype(f"../Fonts/{name}.ttf", font_size)

		return font


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


	def get_disp_dimensions(self) -> tuple:
		"""Returns connected display's dimension"""

		return (self.disp.width, self.disp.height)


	def set_image_support(self):
		"""Getting the dimensions of the display and
		setting the margins."""

		self.WIDTH, self.HEIGHT = self.get_disp_dimensions()

		# First define some constants to allow easy resizing of shapes.
		self.PADDING = 3
		self.TOP = self.PADDING
		self.BOTTOM = self.HEIGHT - self.PADDING
		# Move left to right keeping track of the current x position
		# for drawing shapes.
		self.X = 0

	def create_blank_image(self) -> Image.Image:
		"""Create blank image to draw the timings on."""

		# Create blank image for drawing.
		# Make sure to create image with mode '1' for 1-bit color.

		self.IMAGE = Image.new("1", (self.WIDTH, self.HEIGHT))


	def create_draw(self) -> ImageDraw.ImageDraw:
		"""Create draw object to draw timings on image."""

		# Draw object to draw on image.
		self.DRAW = ImageDraw.Draw(self.IMAGE)


	def draw_rectangle(self):
		"""Drawing black i.e. 0 fill rectangle to get display started."""

		width, height = self.get_disp_dimensions()

		# Draw a black filled box to clear the image.
		self.DRAW.rectangle((0, 0, width, height), outline=0, fill=0)

	def draw_time_image(self, current_time, next_salah_time) -> None:
		"""Creating image of timings to show."""


		self.DRAW.text((self.X, self.TOP), current_time, font=self.FONT, fill=255)

		self.DRAW.text((self.X, self.TOP + 28), next_salah_time, font=self.FONT, fill=255)

	def create_image(self, image_path: str) -> None:
		"""Create displayable image from actual image."""

		self.IMAGE = Image.open(image_path).resize((self.WIDTH, self.HEIGHT), Image.Resampling.LANCZOS).convert('1')

	def display_image(self) -> None:
		"""Display the created image."""


		self.disp.image(self.IMAGE)
		self.disp.display()

	def clear(self) -> None:
		"""Clear the display."""

		self.disp.clear()
		self.disp.display()

if __name__ == '__main__':
	dis = Display()
	print(dis.FONT.font.family)