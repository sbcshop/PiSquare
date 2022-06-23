from machine import UART, Pin,SPI,I2C
from pico_i2c_lcd import I2cLcd
import pmsa003
import machine
import utime,time
import gc9a01

import utime
import italicc

import vga1_bold_16x32 as font
#gp23 reserved

def Digital_Pin_Read(gp_pin):
    if gp_pin =='GPIO17':
            GPIO14 = machine.Pin(7, machine.Pin.IN)
            GPIO14.value()
            
    if gp_pin =='GPIO4':
            GPIO14 = machine.Pin(6, machine.Pin.IN)
            GPIO14.value()
            
    if gp_pin =='GPIO21':
            GPIO14 = machine.Pin(12, machine.Pin.IN)
            GPIO14.value()
            
    if gp_pin =='GPIO8':
            GPIO14 = machine.Pin(9, machine.Pin.IN)
            GPIO14.value()
            
    if gp_pin =='GPIO14':
            GPIO14 = machine.Pin(0, machine.Pin.IN)
            return GPIO14.value()
                    
    elif gp_pin =='GPIO15':
            GPIO10 = machine.Pin(1, machine.Pin.IN)
            return GPIO10.value()        
               
    elif gp_pin =='GPIO11':
            GPIO11 = machine.Pin(10, machine.Pin.IN)
            return GPIO11.value()        
          
    elif gp_pin =='GPIO10':
            GPIO10 = machine.Pin(11, machine.Pin.IN)
            return GPIO10.value()        
            
    elif gp_pin =='GPIO27':
            GPIO27 = machine.Pin(8, machine.Pin.IN)
            return GPIO27.value()
                
    elif gp_pin =='GPIO22':
            GPIO22 = machine.Pin(18, machine.Pin.IN)
            return GPIO22.value()        
                
    elif gp_pin =='GPIO5':
            GPIO5 = machine.Pin(2, machine.Pin.IN)
            return GPIO5.value()
                
    elif gp_pin =='GPIO6':
            GPIO6 = machine.Pin(3, machine.Pin.IN)
            return GPIO6.value()        
                
    elif gp_pin =='GPIO13':
            GPIO13 = machine.Pin(15, machine.Pin.IN)
            return GPIO13.value()
                
    elif gp_pin =='GPIO19':
            GPIO19 = machine.Pin(13, machine.Pin.IN)
            return GPIO19.value()
                
    elif gp_pin =='GPIO26':
            GPIO26 = machine.Pin(14, machine.Pin.IN)
            return GPIO26.value()        
                
    elif gp_pin =='GPIO21':
            GPIO21 = machine.Pin(28, machine.Pin.IN)
            return GPIO21.value()        
        
    elif gp_pin =='GPIO20':
            GPIO20 = machine.Pin(27, machine.Pin.IN)
            return GPIO20.value()
                
    elif gp_pin =='GPIO16':
            GPIO16 = machine.Pin(17, machine.Pin.IN)
            return GPIO16.value()        
        
    elif gp_pin =='GPIO12':
            GPIO12 = machine.Pin(18, machine.Pin.IN)
            return GPIO12.value()        
        
    elif gp_pin =='GPIO7':
            GPIO7 = machine.Pin(19, machine.Pin.IN)
            return GPIO7.value()
                
    elif gp_pin =='GPIO2':
            GPIO2 = machine.Pin(20, machine.Pin.IN)
            return GPIO2.value()
        
    elif gp_pin =='GPIO3':
            GPIO3 = machine.Pin(21, machine.Pin.IN)
            return GPIO3.value()        
                
    elif gp_pin =='GPIO25':
            GPIO25 = machine.Pin(22, machine.Pin.IN)
            return GPIO25.value()

    elif gp_pin =='GPIO24':
            GPIO24 = machine.Pin(26, machine.Pin.IN)
            return GPIO24.value()
    
    elif gp_pin =='GPIO18':
            GPIO18 = machine.Pin(23, machine.Pin.IN)
            return GPIO18.value()
        

def Digital_Pin_Write(gp_pin,state):
    if gp_pin =='GPIO17':
            GPIO14 = machine.Pin(7, machine.Pin.OUT)
            GPIO14.value(int(state))
            
    if gp_pin =='GPIO4':
            GPIO14 = machine.Pin(6, machine.Pin.OUT)
            GPIO14.value(int(state))
            
    if gp_pin =='GPIO21':
            GPIO14 = machine.Pin(12, machine.Pin.OUT)
            GPIO14.value(int(state))
            
    if gp_pin =='GPIO8':
            GPIO14 = machine.Pin(9, machine.Pin.OUT)
            GPIO14.value(int(state))
            
    if gp_pin =='GPIO14':
            GPIO14 = machine.Pin(0, machine.Pin.OUT)
            GPIO14.value(int(state))
                    
    elif gp_pin =='GPIO15':
            GPIO15 = machine.Pin(1, machine.Pin.OUT)
            GPIO15.value(int(state))
            
    elif gp_pin =='GPIO11':
            GPIO11 = machine.Pin(10, machine.Pin.OUT)
            GPIO11.value(int(state))
          
    elif gp_pin =='GPIO10':
            GPIO10 = machine.Pin(11, machine.Pin.OUT)
            GPIO10.value(int(state))
       
    elif gp_pin =='GPIO27':
            GPIO27 = machine.Pin(8, machine.Pin.OUT)
            GPIO27.value(int(state))
                
    elif gp_pin =='GPIO22':
            GPIO22 = machine.Pin(16, machine.Pin.OUT)
            GPIO22.value(int(state))
                
    elif gp_pin =='GPIO5':
            GPIO5 = machine.Pin(2, machine.Pin.OUT)
            GPIO5.value(int(state))
                
    elif gp_pin =='GPIO6':
            GPIO6 = machine.Pin(3, machine.Pin.OUT)
            GPIO6.value(int(state))
                
    elif gp_pin =='GPIO13':
            GPIO13 = machine.Pin(15, machine.Pin.OUT)
            GPIO13.value(int(state))
              
    elif gp_pin =='GPIO19':
            GPIO19 = machine.Pin(13, machine.Pin.OUT)
            GPIO19.value(int(state))
               
    elif gp_pin =='GPIO26':
            GPIO26 = machine.Pin(14, machine.Pin.OUT)
            GPIO26.value(int(state))
                
    elif gp_pin =='GPIO21':
            GPIO21 = machine.Pin(28, machine.Pin.OUT)
            GPIO21.value(int(state))
        
    elif gp_pin =='GPIO20':
            GPIO20 = machine.Pin(27, machine.Pin.OUT)
            GPIO20.value(int(state))
                
    elif gp_pin =='GPIO16':
            GPIO16 = machine.Pin(17, machine.Pin.OUT)
            GPIO16.value(int(state))
        
    elif gp_pin =='GPIO12':
            GPIO12 = machine.Pin(18, machine.Pin.OUT)
            GPIO12.value(int(state))
        
    elif gp_pin =='GPIO7':
            GPIO7 = machine.Pin(19, machine.Pin.OUT)
            GPIO7.value(int(state))
                
    elif gp_pin =='GPIO2':
            GPIO2 = machine.Pin(20, machine.Pin.OUT)
            GPIO2.value(int(state))
        
    elif gp_pin =='GPIO3':
            GPIO3 = machine.Pin(21, machine.Pin.OUT)
            GPIO3.value(int(state))
                
    elif gp_pin =='GPIO25':
            GPIO25 = machine.Pin(22, machine.Pin.OUT)
            GPIO25.value(int(state))


    elif gp_pin =='GPIO24':
            GPIO24 = machine.Pin(26, machine.Pin.OUT)
            GPIO24.value(int(state))
        
    elif gp_pin =='GPIO18':
            GPIO18 = machine.Pin(23, machine.Pin.OUT)
            GPIO18.value(int(state))

        

        
def UART_Pin_Read(device):
    if device == 'lora_hat':
        lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
        for i in range(2):
            data_Read = lora.readline()#read data comming from other pico lora expansion
            if data_Read is not None:
                return data_Read
            time.sleep(2)
                            
    elif device == 'air_monitoring':
        sensor = pmsa003.Sensor("0")    
        utime.sleep(1)    
        reading = sensor.read()    
        return " pm10: {:d} pm25: {:d} pm100: {:d}" .format(reading.pm10_cf1, reading.pm25_cf1, reading.pm100_cf1)
    else:
        return 'wrong device'

             
def UART_Pin_Write(Baudrate,data):
    uart1 = UART(0,baudrate = Baudrate,tx = Pin(0),rx = Pin(1))
    val = uart1.write(data)#send data
    return val
 

def I2C_Pin_Read(Freq):
    i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=Freq)#I2C
    #print("I2C Address      : "+hex(i2c.scan()[0]).upper())
    i2c_1 = i2c.scan()
    return i2c_1

def I2C_Pin_Write(Freq,Address,Data):
    if Address == 0x27:
        i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=Freq)#I2C
        lcd = I2cLcd(i2c, Address, 2, 16)
        lcd.move_to(0,0)
        lcd.putstr(Data)
        return 'done'
    else:
        return 'wrong address'

    
def SPI_Pin_Write(lcd,data):
    spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
    if lcd == 'lcd1.3':
        tft = st7789.ST7789(spi,240,240,reset=Pin(8, Pin.OUT),cs=Pin(5, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)#SPI interface for tft screen
        tft.init()
        time.sleep(0.5)#time delay
        tft.text(font,data, 10,40,st7789.YELLOW)# print on tft screen
        tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen
        return 'done'

        
    if lcd == 'lcd1.28':
        tft = gc9a01.GC9A01(spi,240,240,reset=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=2)
        tft.init()
        tft.rotation(3)
        tft.fill(gc9a01.BLACK)
        utime.sleep(0.5)
        tft.text(font, data, 20, 50, gc9a01.RED)
        return 'done'
    else:
        return 'wrong device'






