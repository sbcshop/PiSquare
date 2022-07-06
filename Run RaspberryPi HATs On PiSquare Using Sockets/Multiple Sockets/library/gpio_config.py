from machine import UART, Pin,SPI,I2C
from pico_i2c_lcd import I2cLcd
import pmsa003
import machine
import utime,time
import gc9a01
import sdcard
import utime
import os
import st7789
import vga1_bold_16x32 as font
from ina219 import INA219
from logging import INFO
from ssd1306 import SSD1306_I2C

def Digital_Pin_Read(gp_pin):
    if gp_pin =='GPIO17':
            GPIO17 = machine.Pin(7, machine.Pin.IN)
            return GPIO17.value()
            
    if gp_pin =='GPIO4':
            GPIO4 = machine.Pin(6, machine.Pin.IN)
            return GPIO4.value()
            
    if gp_pin =='GPIO21':
            GPIO21 = machine.Pin(12, machine.Pin.IN)
            return GPIO21.value()
            
    if gp_pin =='GPIO8':
            GPIO8 = machine.Pin(9, machine.Pin.IN)
            return GPIO8.value()
            
    if gp_pin =='GPIO14':
            GPIO14 = machine.Pin(0, machine.Pin.IN)
            return GPIO14.value()
                    
    elif gp_pin =='GPIO15':
            GPIO15 = machine.Pin(1, machine.Pin.IN)
            return GPIO15.value()        
               
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
            GPIO17 = machine.Pin(7, machine.Pin.OUT)
            GPIO17.value(int(state))
            
    if gp_pin =='GPIO4':
            GPIO4 = machine.Pin(6, machine.Pin.OUT)
            GPIO4.value(int(state))
            
    if gp_pin =='GPIO21':
            GPIO21 = machine.Pin(12, machine.Pin.OUT)
            GPIO21.value(int(state))
            
    if gp_pin =='GPIO8':
            GPIO8 = machine.Pin(9, machine.Pin.OUT)
            GPIO8.value(int(state))
            
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
    
    elif device == "rfid_hat":
         rfid = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
         WIDTH  = 128                                            # oled display width
         HEIGHT = 32                                             # oled display height

            #i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
         i2c = I2C(0,freq=200000,sda=Pin(20),scl=Pin(21))
         print(i2c)
         print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
         print("I2C Configuration: "+str(i2c))                   # Display I2C config

         oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

         oled.fill(0)
         oled.text("RFID HAT",30,5)
         oled.show()
         time.sleep(2)
         oled.fill(0)
         oled.show()
         for i in range(2):
            data_Read = rfid.readline(12)#read data comming from other pico lora expansion
            if data_Read is not None:
                data=data_Read.decode("utf-8")
                oled.text(data,5,5)
                oled.show()
                print(data)
                time.sleep(2)
                oled.fill(0)
                oled.show()
                return data
            time.sleep(2)
            
    elif device == "barcode_hat":
            barcode = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
            
            spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
            tft = st7789.ST7789(spi,135,240,reset=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)#SPI interface for tft screen
            def info():
                tft.init()
                time.sleep(0.5)#time delay
               
                tft.text(font,"RASPBERRY-PI", 10,10,st7789.YELLOW)# print on tft screen
                tft.fill_rect(0, 50, 240,10, st7789.RED)#display red line on tft screen
                
                tft.text(font,"BARCODE-HAT", 10,70 ,st7789.GREEN)
                tft.fill_rect(0, 105, 240,10, st7789.RED)

            info()
            time.sleep(4)
            tft.fill(0)
            data_Read = barcode.readline()#read data comming from other pico lora expansion
            for i in range(2): 
                if data_Read:
                      if '\r' in data_Read:
                        data=data_Read.decode("utf-8")
                        tft.text(font,data, 0,50 ,st7789.GREEN)
                        tft.fill_rect(0, 95, 240,10, st7789.RED)
                        return data[:-1]
            
                time.sleep(2)

    elif device == 'gps_hat':
                gps = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
                def convert_to_degrees(raw_value):
                    decimal_value = raw_value/100.00
                    degrees = int(decimal_value)
                    mm_mmmm = (decimal_value - int(decimal_value))/0.6
                    position = degrees + mm_mmmm
                    position = "%.4f" %(position)
                    return position

                def RMC_Read():
                            data = "$GNRMC,"
                            info = data
                            received_data = (str)(gps.read()) #read NMEA string received
                            data_available = received_data.find(info)
                            if (data_available>0):
                                buffer = received_data.split(data,1)[1]  #store data coming 
                                buff = (buffer.split(','))
                                nmea_time = []
                                nmea_latitude = []
                                nmea_longitude = []
                                date = []
                                speed_over_ground = []
                                nmea_time = buff[0]
                                speed_over_ground = buff[6]#extract time from GPGGA string
                                nmea_latitude = buff[2]              
                                nmea_longitude = buff[4]
                                date = buff[8]
                                lat = (float)(nmea_latitude)
                                lat = convert_to_degrees(lat)
                                longi = (float)(nmea_longitude)
                                longi = convert_to_degrees(longi)                
                                return lat,longi,nmea_time,speed_over_ground,date
                            
                for _ in range(1000):
                  x = RMC_Read() #Recommended minimum specific GNSS data
                  if x is not None:
                                a = list(x)
                                print("Latitude = ",a[0] + "    Longitude = ",a[1])
                                print("UTC Time = ",a[2])
                                print("Date = ",a[4])
                                print("speed over ground = ",a[3])
                                print("\n")
                                return "Latitude = "+str(a[0]) + "    Longitude = "+str(a[1]) + "  UTC Time = "+str(a[2])+ "  Date = "+str(a[4])
                                time.sleep(0.2)
                                break
    
    else:
        return 'wrong device'
    
def UART_Pin_Write(data):
    uart1 = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
    val = uart1.write(data)#send data
    return val
 

def I2C_Pin_Read(device):
    sda=machine.Pin(20)
    scl=machine.Pin(21)
    i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
   
    if device == "power_hat":
        SHUNT_OHMS = 0.1
        addr1=0x40
        addr2=0x41
        addr3=0x42
        
        lst = []
        
        ina1 = INA219(SHUNT_OHMS, i2c,addr1,log_level=INFO)
        ina2 = INA219(SHUNT_OHMS, i2c,addr2,log_level=INFO)
        ina3 = INA219(SHUNT_OHMS, i2c,addr3,log_level=INFO)

        ina1.configure()
        ina2.configure()
        ina3.configure()
        
        print("Bus Voltage 1: %.3f V" % ina1.voltage(),"Current 1: %.3f mA" % ina1.current(),"Power 1: %.3f mW" % ina1.power())

        print("Bus Voltage 2: %.3f V" % ina2.voltage(),"Current 2: %.3f mA" % ina2.current(),"Power 2: %.3f mW" % ina2.power())

        print("Bus Voltage 3: %.3f V" % ina3.voltage(),"Current 3: %.3f mA" % ina3.current(),"Power 3: %.3f mW" % ina3.power())
        
        f1 = "Bus Voltage 1: %.3f V" % ina1.voltage(),"Current 1: %.3f mA" % ina1.current(),"Power 1: %.3f mW" % ina1.power()
        f2 = "Bus Voltage 2: %.3f V" % ina2.voltage(),"Current 2: %.3f mA" % ina2.current(),"Power 2: %.3f mW" % ina2.power()
        f3 = "Bus Voltage 3: %.3f V" % ina3.voltage(),"Current 3: %.3f mA" % ina3.current(),"Power 3: %.3f mW" % ina3.power()
        
        lst.append(f1)
        lst.append(f2)
        lst.append(f3)
        
        return lst
    else:
       return 'wrong device'
               
def I2C_Pin_Write(device,Data):
    if device == "16x2_lcd":
        i2c = I2C(0,scl=Pin(21), sda=Pin(20))#I2C
        lcd = I2cLcd(i2c, 0x27, 2, 16)
        lcd.move_to(0,0)
        lcd.putstr(Data)
        return 'done'
    else:
        return 'wrong address'

    
def SPI_Pin_Write(device,data):
    spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
    if device == 'lcd1.3':
        tft = st7789.ST7789(spi,240,240,reset=Pin(8, Pin.OUT),cs=Pin(5, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)#SPI interface for tft screen
        tft.init()
        time.sleep(0.5)#time delay
        tft.text(font,data, 10,40,st7789.YELLOW)# print on tft screen
        tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen
        return 'done'

        
    if device == 'lcd1.28':
        tft = gc9a01.GC9A01(spi,reset=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=0)
        tft.fill(gc9a01.BLACK)
        utime.sleep(0.5)
        tft.text(font, data, 20, 50, gc9a01.RED)
        return 'done'
    
    if device == 'sdcard':
        def sdtest(data):
            spi=SPI(1,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
            sd=sdcard.SDCard(spi,Pin(9))
            vfs = os.VfsFat(sd)
            os.mount(vfs, "/fc")
            print("Filesystem check")
            
            print(os.listdir("/fc"))

            fn = "/fc/File.txt"
            print()
            print("Single block write")
            with open(fn, "a") as f:
                n = f.write(data)
                print(n, "bytes written")
                da = str(n)+' bytes written'
                print("da = ",da)
                return da
            os.umount("/fc")
    
        sd=sdtest(data+'\n')
        return sd
        
    else:
        return 'wrong device'

def SPI_Pin_Read(device):
        if device == 'sdcard':
            def sdtest():
                spi=SPI(1,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
                sd=sdcard.SDCard(spi,Pin(9))
                vfs = os.VfsFat(sd)
                os.mount(vfs, "/fc")
                print("Filesystem check")
                
                print(os.listdir("/fc"))

                fn = "/fc/File.txt"
                print()
                print("Single block read")
                with open(fn, "r") as f:
                    result2 = f.read()
                    print(len(result2), "bytes read")
                    return result2

                os.umount("/fc")
            d = sdtest()
            return d
                
        else:
            return 'wrong device'
