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
        self.X = 0

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
            self.disp.clear()
            self.disp.display()

    def set_image_support(self):
        width, height = self.get_disp_dimensions()

        # First define some constants to allow easy resizing of shapes.
        self.PADDING = 3
        self.TOP = self.PADDING
        self.BOTTOM = height - self.PADDING
        # Move left to right keeping track of the current x position for drawing shapes.
        self.X = 0

    def create_blank_image(self) -> Image.Image:
        width, height = self.get_disp_dimensions()
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.

        image = Image.new("1", (width, height))

        return image

    def get_draw(self, image: Image.Image) -> ImageDraw.ImageDraw:
        # rawing object to draw on image.
        draw = ImageDraw.Draw(image)

        width, height = self.get_disp_dimensions()

        return draw

    def draw_rectangle(self, draw: ImageDraw.ImageDraw):
        width, height = self.get_disp_dimensions()

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

    def create_image(self, draw: ImageDraw.ImageDraw, current_time, next_salah_time):
        draw.text((self.X, self.TOP), current_time, font=font, fill=255)

        draw.text((self.X, self.TOP + 28), next_salah_time, font=font, fill=255)

    def display_image(self, image: Image.Image):
        self.disp.image(image)
        self.disp.display()

    def clear(self):
    	self.disp.clear()
    	self.disp.display()