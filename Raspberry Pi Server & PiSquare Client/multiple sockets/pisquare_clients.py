from machine import UART, Pin,SPI,I2C
import utime,time
from ssd1306 import SSD1306_I2C

WiFi_SSID='Tech SB_2G'          # Wifi_SSID
WiFi_password = 'jc643111h@'    # WiFi Password
TCP_ServerIP = '192.168.29.73'  # Raspberry pi IP Address
Port = '12420'                  # TCP Server Port (you can change)

uart = UART(1,115200)           # Default Baud rate

WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

i2c = I2C(1,freq=200000,sda=Pin(6),scl=Pin(7))
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.fill(0)
oled.text("Client",50,5)
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
def sendData(ID,data):
    sendCMD('AT+CIPSEND='+str(ID)+','+str(len(data)),'>')
    uart.write(data)
    

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
sendCMD("AT+CIFSR","OK")

res = str(lst)[1:-1]
x = res.split(",")
x = x[3].replace('"',"")
x = x.split("+")
r = x[0][:-4]
print(r)

oled.fill(0)
oled.text(r,10,0)
oled.show()
time.sleep(2)
while True:
    sendCMD("AT+CIPSTART=\"TCP\",\""+TCP_ServerIP+"\","+Port,"OK",10000)
    sendCMD("AT+CIPMODE=1","OK")
    a = sendCMD("AT+CIPSEND",">")
    uart.write('client is connected to raspberry pi')  # Send data to TCP server
    if a == True:
        break
    
while True:
    s=uart.read()   # receive data from server
    if(s != None):
        s=s.decode()
        print(s)    # Print received data
        oled.text(s,0,20)
        oled.show()
        time.sleep(2)
    oled.fill(0)
    oled.show() 
