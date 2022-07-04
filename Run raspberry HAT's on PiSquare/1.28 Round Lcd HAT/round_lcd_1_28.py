from machine import Pin, SPI
import gc9a01
import time
import utime

import vga1_bold_16x32 as font

#------joystck pin declaration----- 
joystick_up = machine.Pin(14,Pin.IN, Pin.PULL_UP)
joystick_down = machine.Pin(3,Pin.IN, Pin.PULL_UP)
joystick_left = machine.Pin(15,Pin.IN, Pin.PULL_UP)
joystick_right = machine.Pin(2,Pin.IN, Pin.PULL_UP)
joystick_centre = machine.Pin(13,Pin.IN, Pin.PULL_UP)


def main(): 
    spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
    tft = gc9a01.GC9A01(spi,reset=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=0)
    tft.fill(gc9a01.BLACK)
    utime.sleep(0.5)
    tft.text(font, "Round lcd hat", 20, 50, gc9a01.RED)
    tft.text(font, "1.28(240x240)", 20, 90, gc9a01.YELLOW)
    tft.text(font, "PiSquare", 30, 130, gc9a01.GREEN)
    
main() 
time.sleep(2)
while 1:
    val1 = joystick_up.value()
    val2 = joystick_down.value()
    val3 = joystick_left.value()
    val4 = joystick_right.value()
    val5 = joystick_centre.value()
       
    print("val1 = ",val1)
    print("val2 = ",val2)
    print("val3 = ",val3)
    print("val4 = ",val4)
    print("val5 = ",val5)
    
    time.sleep(0.2)
