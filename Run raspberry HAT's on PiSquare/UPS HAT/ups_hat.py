from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from ina219 import INA219
from logging import INFO
import time

SHUNT_OHMS = 0.1


WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height
i2c = I2C(0,freq=200000,sda=Pin(20),scl=Pin(21))
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

oled.fill(0)
oled.text("SB COMPONENTS",10,5)
oled.text("PiSquare UPS HAT",0,25)
oled.show()

########################################################
sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)


ina = INA219(SHUNT_OHMS, i2c,0x42,log_level=INFO)
ina.configure()

time.sleep(2)
oled.fill(0)
oled.show()

while 1:
    bus_voltage = ina.voltage()
    p = (bus_voltage - 6)/2.4*100
    if(p > 100):p = 100
    if(p < 0):p = 0

    print("Bus Voltage: %.3f V" % ina.voltage())
    print("Current: %.3f mA" % ina.current())
    print("Power: %.3f mW" % ina.power())
    print("Percent: %.3f " % p)
    time.sleep(0.2)

    oled.text("Bus Voltage: %.3f V" % ina.voltage(),0,0)
    oled.text("Current: %.3f mA" % ina.current(),0,8)
    oled.text("Power: %.3f mW" % ina.power(),0,16)
    oled.text("Percent: %.3f " % p,0,24)
    oled.show()
    oled.fill(0)
    
