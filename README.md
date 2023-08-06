# Salah-Timmings
## Display Salah Timmings on small display, running on Raspberry Pi.
#### In Progress.

- [x] Make a logic to return Isha ending time (i.e. Fajir start time of next day).
- [ ] Confirm and correct the timmings.
- [x] Simulate a month ending and observe behaviour. I reckon some errors may occur at the end of the month. (Solved)
- [ ] 3rd info to show: Remaining time to next Salah. Maybe after getting new SSD1306 display.

### Pinouts and connections:
 I have a SSD1306 display with 4 pins:

 1. VCC
 2. GND
 3. SDA
 4. SCL


>VCC -> 3V3

>GND -> GND

>SDA -> SDA

>SCL -> SCL


Check Adafruit's [webiste](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/wiring) for other displays' connections.

## Setup:

1. Load [Raspberry Pi OS](https://www.raspberrypi.com/software/) on your RPi.
2. Enter command and enable I2C or SPI from Interface options as needed:

```bash 
sudo raspi-config
``` 

3. Change main.py file as needed for your display then run:

```bash
sudo python main.py
```

#### If you are getting shelve library error, try upgrading to newer Python version. I have tried on 3.11.3 & 3.11.4.

## Conclusion:

Unfortunately, My SSD1306 display is broken. i2cdetect is not detecting it so, I cannot work on this project further. 

But the code side of this project is almost complete and is giving correct timmings.
