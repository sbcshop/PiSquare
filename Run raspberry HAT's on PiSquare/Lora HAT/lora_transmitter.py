#Transmiter code
from machine import UART,SPI,Pin
import time

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
    
while True:
    n = input("Enter data = ")
    lora.write(n)#send data
    time.sleep(0.2)#wait 200ms

