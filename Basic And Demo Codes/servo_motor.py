import time
from machine import Pin, PWM

pwm = PWM(Pin(8)) # servo motor data pin(orange wire or yellow wire) is connected to GP8 pin of PiSquare
pwm.freq(50)

while True:
    for position in range(1000,9000,50):
        pwm.duty_u16(position)
        time.sleep(0.01)
    for position in range(9000,1000,-50):
        pwm.duty_u16(position)
        time.sleep(0.01)
