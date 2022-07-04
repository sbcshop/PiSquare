from machine import Pin, SPI,UART
import time
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font
#import vga1_8x16 as font1
#import vga1_16x16 as font2

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)#SPI interface for tft screen

barcode = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def info():
    tft.init()
    time.sleep(0.5)#time delay
   
    tft.text(font,"RASPBERRY-PI", 10,10,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 50, 240,10, st7789.RED)#display red line on tft screen
    
    tft.text(font,"BARCODE-HAT", 10,70 ,st7789.GREEN)
    tft.fill_rect(0, 105, 240,10, st7789.RED)

info()
time.sleep(1)
tft.fill(0)
tft.text(font,"SCAN", 80,5,st7789.YELLOW)# print on tft screen
while 1:
        data_Read = barcode.readline()#read data comming from other pico lora expansion
        if data_Read:
                    if '\r' in data_Read:
                        data=data_Read.decode("utf-8")
                        print(data)
                        tft.text(font,data, 0,50 ,st7789.GREEN)
                        tft.fill_rect(0, 95, 240,10, st7789.RED)
                
        time.sleep(2)

