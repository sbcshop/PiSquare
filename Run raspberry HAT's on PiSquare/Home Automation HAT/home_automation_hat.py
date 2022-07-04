from machine import Pin
import time

relay1 = machine.Pin(15, machine.Pin.OUT)
relay2 = machine.Pin(13, machine.Pin.OUT)


relay1.value(0)#initally relay3 at LOW
relay2.value(0)#initally relay4 at LOW


time.sleep(1)

while 1:
    relay1.value(1)#initally relay3 at HIGH
    relay2.value(1)#initally relay4 at HIGH

    time.sleep(1)

    relay1.value(0)#initally relay3 at LOW
    relay2.value(0)#initally relay4 at LOW

    time.sleep(1)

