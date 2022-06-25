from machine import UART, Pin,SPI,I2C
from ssd1306 import SSD1306_I2C
import utime,time
import random

import utime

WiFi_SSID='PiSquare'             # PiSquare Wifi_SSID
WiFi_password = 'pisquare@#123'  # PiSquare WiFi Password
port = '80'                      # PiSquare TCP Server Port(make sure server and client port are same)

uart = UART(1, 115200)           # Default Baud rate

WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

i2c = I2C(1,freq=200000,sda=Pin(6),scl=Pin(7))
print(i2c)
print("I2C Address  : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.fill(0)
oled.text("SERVER",50,0)
oled.show()

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
def sendData(ID,data):
    sendCMD('AT+CIPSEND='+str(ID)+','+str(len(data)),'>')
    uart.write(data)
    
    
########  Function to receive data  ######################
def ReceiveData():
    data=uart.read()
    if(data != None):
        data=data.decode()
        print(data)
        if(data.find('+IPD') >= 0):
            n1=data.find('+IPD,')
            n2=data.find(',',n1+5)
            ID=int(data[n1+5:n2])
            n3=data.find(':')
            data=data[n3+1:]
            return ID,data
    return None,None

uart.write('+++')
time.sleep(1)
if(uart.any()>0):uart.read()
sendCMD("AT+RST","OK")
time.sleep(1)
sendCMD("AT+CWMODE=2","OK")
sendCMD("AT+CIFSR","OK")
sendCMD("AT+CWSAP?","OK")
sendCMD("AT+CIPMUX=1","OK")
sendCMD("AT+CIPSERVER=1,"+port,"OK")
sendCMD("AT+CWSAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\",2,3,4,0","OK")#+CWSAP: "ssid", "pwd", "chl", "ecn", "maxconnection", "ssidhidden 0- non hide,1-for hidden"
sendCMD("AT+CWLIF","OK")
#uart.write('Connection Established')  # Send data to TCP server

data = "hello world"
while True:
    Connection_ID,data=ReceiveData()
    if(Connection_ID != None):
        sendData(Connection_ID,data) #Send received data back to TCP Server
        print(data)   # Print Received data
        oled.text(data,10,20)
        oled.show()
        time.sleep(2)
        oled.fill(0)
        oled.show()



