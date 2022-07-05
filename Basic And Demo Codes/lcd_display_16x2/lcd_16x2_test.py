from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=400000) # sda of lcd i2c is connect to GP20 pin of PiSquare and scl is connected to GP21 pin of PiSquare

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
    lcd.move_to(2,0)
    lcd.putstr("SB COMPONENTS")
    lcd.move_to(4,1)
    lcd.putstr("PISQUARE")
    
  
