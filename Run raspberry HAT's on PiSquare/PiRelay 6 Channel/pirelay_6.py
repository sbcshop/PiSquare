from machine import Pin
import time

relay1 = machine.Pin(2, machine.Pin.OUT)
relay2 = machine.Pin(3, machine.Pin.OUT)
relay3 = machine.Pin(15, machine.Pin.OUT)
relay4 = machine.Pin(13, machine.Pin.OUT)
relay5 = machine.Pin(14, machine.Pin.OUT)
relay6 = machine.Pin(28, machine.Pin.OUT)

relay1.value(0)#relay1 at LOW
relay2.value(0)#relay2 at LOW
relay3.value(0)#relay3 at LOW
relay4.value(0)#relay4 at LOW
relay5.value(0)#relay5 at LOW
relay6.value(0)#relay6 at LOW

time.sleep(1)

while 1:
    relay1.value(1)#relay1 at HIGH
    relay2.value(1)#relay2 at HIGH
    relay3.value(1)#relay3 at HIGH
    relay4.value(1)#relay4 at HIGH
    relay5.value(1)#relay5 at HIGH
    relay6.value(1)#relay6 at HIGH
    
    time.sleep(1)
    
    relay1.value(0)#relay1 at LOW
    relay2.value(0)#relay2 at LOW
    relay3.value(0)#relay3 at LOW
    relay4.value(0)#relay4 at LOW
    relay5.value(0)#relay5 at LOW
    relay6.value(0)#relay6 at LOW
    
    time.sleep(1)
