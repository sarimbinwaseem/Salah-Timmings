import sys
# import Adafruit_GPIO.SPI as SPI
# import Adafruit_SSD1306

# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
   

currentDate = datetime.datetime.today().date()
currentDay = currentDate.day
# currentDay = currentDate.strftime("%d-%m")
currentTime = datetime.datetime.today().time().strftime("%H:%M")
# currentTime = timeParser2(currentTime)
print("Current Date:", currentDate)
print("Current Time:", currentTime)
print("Current Day:", currentDay)

currentMonth = str(currentDate)[5:7]
print("Month:", currentMonth)
# print("Current Day:", currentDay)




FajirTime = str(sheet[f'{Fajir}{currentDay}'].value)
TuluTime = str(sheet[f'{Tulu}{currentDay}'].value)
ZuhurTime = str(sheet[f'{Zuhur}{currentDay}'].value)
AsarTime = str(sheet[f'{Asar}{currentDay}'].value)
MaghribTime = str(sheet[f'{Maghrib}{currentDay}'].value)
IshaTime = str(sheet[f'{Isha}{currentDay}'].value)

TimeList = [FajirTime, TuluTime, ZuhurTime, AsarTime, MaghribTime, IshaTime]

def nextNamazTime(currentTime, TimeList):
    t = ""
    for nTime in TimeList:
        if nTime > currTime():
            t = str(timeParser2(nTime))
            return t

### Display Code Started ###
	
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
####
disp = Adafruit_SSD1306.SSD1306_128_64(rst = RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

#rawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 3
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php

try:
    font = ImageFont.truetype('TheImpostor.ttf', 20)
except:
    font = ImageFont.load_default()
while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((x, top), str(timeParser2(currTime())),  font=font, fill=255)
    draw.text((x, top+28), nextNamazTime(currentTime, TimeList), font=font, fill=255)

    # Display image.
    try:
        
        disp.image(image)
        disp.display()
        timelib.sleep(.1)
    except KeyboardInterrupt:
        print("Keyboard Interrupt... Exiting")
        disp.clear()
        disp.display()
        sys.exit()       
