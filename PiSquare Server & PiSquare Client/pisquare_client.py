from machine import UART, Pin,SPI,I2C
from ssd1306 import SSD1306_I2C
import utime,time



lst = []
#import vga1_8x16 as font
WiFi_SSID='PiSquare'  # Wifi_SSID
WiFi_password = 'pisquare@#123'      # WiFi Password
TCP_ServerIP = '192.168.4.1'   # IP of Computer on which TCP server is running or any server
Port = '80'                    # TCP Server Port
                    # TCP Server Port

uart = UART(1, 115200)           # Default Baud rate



WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

i2c = I2C(1,freq=200000,sda=Pin(6),scl=Pin(7))
print(i2c)
print("I2C Address  : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.fill(0)
oled.text("Client",50,0)
oled.show()

######## Function to send or receive commands and data
lst = []
def sendCMD(cmd,ack,timeout=2000):
    uart.write(cmd+'\r\n')
    t = utime.ticks_ms()
    while (utime.ticks_ms() - t) < timeout:
        s=uart.read()
        if(s != None):
            s=s.decode()
            if cmd == "AT+CIFSR":
                 lst.append(s)
            print(s)
            if(s.find(ack) >= 0):
                return True
    return False
#####################################################

uart.write('+++')
sendCMD("AT+RST","OK")
time.sleep(1)
if(uart.any()>0):uart.read()
sendCMD("AT","OK")
sendCMD("AT+CWMODE=3","OK")
sendCMD("AT+CWJAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\"","OK",20000)
sendCMD("AT+CIFSR","OK")
sendCMD("AT+CIPSTART=\"TCP\",\""+TCP_ServerIP+"\","+Port,"OK",10000)
#sendCMD("AT+CIPMODE=1","OK")
#sendCMD("AT+CIPSEND",">")
#uart.write('Client')  # Send data to TCP server
print(lst)
'''
res = str(lst)[1:-1]
x = res.split(",")
x = x[3].replace('"',"")
x = x.split("+")
r = x[0][:-4]
print(r)
'''
while True:
    sendCMD("AT+CIPSTART=\"TCP\",\""+TCP_ServerIP+"\","+Port,"OK",10000)
    sendCMD("AT+CIPMODE=1","OK")
    a = sendCMD("AT+CIPSEND",">")
    uart.write('client is connected from pisquare')  # Send data to TCP server
    if a == True:
        break
    
while True:
    s=uart.read()   # receive data from server
    if(s != None):
        s=s.decode()
        oled.text(s,10,20)
        oled.show()
        time.sleep(2)
        oled.fill(0)
        oled.show()
        print(s)    # Print received data

