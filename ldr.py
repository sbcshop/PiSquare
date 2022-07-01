from machine import ADC, Pin
from time import sleep

ldr = ADC(Pin(28)) # ldr is connect to GP28 (Analog pin)


while True:
    x = ldr.read_u16()
    x = round(x/65535*100,2)
    print("light: " + str(x) +"%")
    sleep(1) 