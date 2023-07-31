# Salah-Timmings
#### In Progress.
[x] Make a logic to return Isha ending time.
## Display Salah Timmings on small display, running on Raspberry Pi.


### Pinouts and connections:
 I have a SSD1306 display with 4 pins:

 1. VCC
 2. GND
 3. SDA
 4. SCL

```
VCC -> 3V3

GND -> GND

SDA -> SDA

SCL -> SCL
```

Check Adafruit's webiste for other displays' connections.

## Setup:

1. Load Raspberry Pi OS on your RPi.
2. Enter command and enable I2C or SPI from Interface options as needed:

```bash 
sudo raspi-config
``` 

3. Change main.py file as needed for your display then run:

```bash
sudo python main.py
```

#### If you are getting shelve library error, try upgrading to newer Python version.

## Conclusion:

Unfortunately, My SSD1306 display is not working at the moment. i2cdetect is not detecting it so, I cannot work on this project further. 

But the code side of this project is almost complete and is giving correct timmings (except the ending of Isha time (Haven't checked yet but I can sense.). Ending time of Isha may be returned by method after 00:00 at night {see code}).