from machine import ADC, Pin
import time

pot = ADC(Pin(26)) # potentiometer is connect to GP26 (Analog pin)

while True:
   value = pot.read_u16() * (3.3 / (65535)) #Convert the sampled data to voltage value
   print(value)
   time.sleep(1)