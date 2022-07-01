from machine import Pin, I2C, UART
import utime
from ssd1306 import SSD1306_I2C # save this library in PiSquare

WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

i2c = I2C(1,freq=200000,sda=Pin(6),scl=Pin(7))
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

oled.fill(0)
oled.text("SB COMPONENTS",10,5)
oled.text("PiSquare",30,25)
oled.show()


