# Use thonny ide to program pico
# Use Hercules SETUP utility for TCP server and client https://www.hw-group.com/software/hercules-setup-utility
# Make sure both WiFi HAT and TCP Server are connected on same network

from machine import UART, Pin,SPI,I2C
import utime,time
from ssd1306 import SSD1306_I2C

WiFi_SSID='Tech SB_2G'               # Enter Wifi SSID here
WiFi_password = 'jc643111'     # Enter WiFi Password here
Port = '8080'                       # TCP Server Port

uart = UART(1, 115200)              # Default Baud rate of ESP8266

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
time.sleep(1)

########  Function to send command  ###############

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

########  Function to send data  ###############

def sendData(ID,data):
    sendCMD('AT+CIPSEND='+str(ID)+','+str(len(data)),'>')
    uart.write(data)

########  Function to receive data  ###############

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
sendCMD("AT","OK")
sendCMD("AT+CWMODE=3","OK")
sendCMD("AT+CWJAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\"","OK",20000)
sendCMD("AT+CIPMUX=1","OK")
sendCMD("AT+CIPSERVER=1,"+Port,"OK")
sendCMD("AT+CIFSR","OK")

res = str(lst)[1:-1]
x = res.split(",")
x = x[3].replace('"',"")
x = x.split("+")
r = x[0][:-4]
print(r)
oled.text(r,10,20)
oled.show()
time.sleep(2)
oled.fill(0)
while True:
    Connection_ID,data=ReceiveData()
    if(Connection_ID != None):
        sendData(Connection_ID,data) #Send received data back to TCP Server
        oled.text(data,10,20)
        oled.show()
        time.sleep(2)
        oled.fill(0)
        oled.show()
        print(data)   # Print Received data


