#Receiver code

from machine import UART, Pin,SPI,I2C
import time
lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

while 1:
        data_Read = lora.readline()#read data comming from other lora
        if data_Read is not None:
                 print(data_Read)
        time.sleep(0.2)
