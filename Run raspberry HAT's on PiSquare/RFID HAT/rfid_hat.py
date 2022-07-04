from machine import UART, Pin,SPI,I2C
import utime,time
from ssd1306 import SSD1306_I2C


lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

buzzer = machine.Pin(7, machine.Pin.OUT)
buzzer.value(0)

WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

#i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
i2c = I2C(0,freq=200000,sda=Pin(20),scl=Pin(21))
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

oled.fill(0)
oled.text("RFID HAT",30,5)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()

while 1:
    data_Read = lora.readline(12)#read data comming from other pico lora expansion
    if data_Read is not None:
        buzzer.value(1)
        data=data_Read.decode("utf-8")
        oled.text(data,5,5)
        oled.show()
        print(data)
        time.sleep(2)
        oled.fill(0)
        oled.show()
    time.sleep(0.5)
    buzzer.value(0)