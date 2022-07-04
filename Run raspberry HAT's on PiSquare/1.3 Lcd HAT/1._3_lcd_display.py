# attendence system using raspberry pi pico and pico barcode hat and security system using barcode
from machine import Pin, UART,SPI
import time
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font

joystick_up = machine.Pin(14,Pin.IN, Pin.PULL_UP)
joystick_down = machine.Pin(3,Pin.IN, Pin.PULL_UP)
joystick_left = machine.Pin(15,Pin.IN, Pin.PULL_UP)
joystick_right = machine.Pin(2,Pin.IN, Pin.PULL_UP)
joystick_centre = machine.Pin(13,Pin.IN, Pin.PULL_UP)

key1 = machine.Pin(28,Pin.IN, Pin.PULL_UP)
key2 = machine.Pin(27,Pin.IN, Pin.PULL_UP)
key3 = machine.Pin(17,Pin.IN, Pin.PULL_UP)
key4 = machine.Pin(18,Pin.IN, Pin.PULL_UP)

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)#SPI interface for tft screen

def main():
    tft.init()
    tft.fill(st7789.BLACK)
    time.sleep(0.5)#time delay
   
    tft.text(font,"PISQUARE", 10,40,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen
    
    tft.text(font,"LCD 1.3 HAT", 10,120,st7789.GREEN)
    tft.fill_rect(0, 152, 240,10, st7789.RED)
    
time.sleep(1)
main()

while 1:
    val1 = joystick_up.value()
    val2 = joystick_down.value()
    val3 = joystick_left.value()
    val4 = joystick_right.value()
    val5 = joystick_centre.value()
    
    key_val1 = key1.value()
    key_val2 = key2.value()
    key_val3 = key3.value()
    key_val4 = key4.value()
    
    
    print("val1 = ",val1)
    print("val2 = ",val2)
    print("val3 = ",val3)
    print("val4 = ",val4)
    print("val5 = ",val5)
    
    print("key_val1 = ",key_val1)
    print("key_val2 = ",key_val2)
    print("key_val3 = ",key_val3)
    print("key_val4 = ",key_val4)
    time.sleep(0.2)

    