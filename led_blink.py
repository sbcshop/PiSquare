from machine import Pin
import time

led = Pin(24, Pin.OUT) # GP24 Pin 

while True:
    led.value(1)
    time.sleep(1) # change time delay from here 
    led.value(0)
    time.sleep(1)
