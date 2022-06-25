# Use thonny ide to program PiSquare
# This code is server, and mobile application is client
# Code made by sbcomponents
from machine import UART, Pin,SPI,I2C
import utime,time
from ssd1306 import SSD1306_I2C

WiFi_SSID='PiSquare'                 # PiSquare_SSID
WiFi_password = 'pisquare@#123'      # PiSquare Password
port = '8080'                        # TCP Server Port

uart = UART(1, 115200)              # Default Baud rate of ESP8266

r1 = machine.Pin(2, machine.Pin.OUT)
r2 = machine.Pin(3, machine.Pin.OUT)
r3 = machine.Pin(15, machine.Pin.OUT)
r4 = machine.Pin(13, machine.Pin.OUT)

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
sendCMD("AT+RST","OK")
time.sleep(1)
sendCMD("AT+CWMODE=2","OK")
sendCMD("AT+CIFSR","OK")
sendCMD("AT+CWSAP?","OK")
sendCMD("AT+CIPMUX=1","OK")
sendCMD("AT+CIPSERVER=1,"+port,"OK")
sendCMD("AT+CWSAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\",2,3,4,0","OK")#+CWSAP: "ssid", "pwd", "chl", "ecn", "maxconnection", "ssidhidden 0- non hide,1-for hidden"
sendCMD("AT+CWLIF","OK")

while True:
    Connection_ID,data=ReceiveData()
    if(Connection_ID != None):
        sendData(Connection_ID,data) #Send received data back to TCP Server
        oled.text(data,10,20)
        oled.show()
        print("data =",data)   # Print Received data
        print(list(data))
        if data == "Relay1_ON":
            r1.value(1)
            print("relay 1 on")
            oled.fill(0)
            oled.show()
        elif data == "Relay1_OFF":
            r1.value(0)
            print("relay 1 off")
            oled.fill(0)
            oled.show()
            
        elif data == "Relay2_ON":
            r2.value(1)
            print("relay 2 on")
            oled.fill(0)
            oled.show()
            
        elif data == "Relay2_OFF":
            r2.value(0)
            print("relay 2 off")
            oled.fill(0)
            oled.show()
            
        elif data == "Relay3_ON":
            r3.value(1)
            print("relay 3 on")
            oled.fill(0)
            oled.show()
            
        elif data == "Relay3_OFF":
            r3.value(0)
            print("relay 3 off")
            oled.fill(0)
            oled.show()
            
        elif data == "Relay4_ON":
            r4.value(1)
            print("relay 4 on")
            oled.fill(0)
            oled.show()
            
        elif data == "Relay4_OFF":
            r4.value(0)
            print("relay 5 off")
            oled.fill(0)
            oled.show()

            




            



