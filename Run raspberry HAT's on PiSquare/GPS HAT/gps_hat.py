from machine import UART, Pin,SPI,I2C
import utime,time

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
            
while 1:
  x = RMC_Read() #Recommended minimum specific GNSS data
  if x is not None:
                a = list(x)
                print("Latitude = ",a[0] + "    Longitude = ",a[1])
                print("UTC Time = ",a[2])
                print("Date = ",a[4])
                print("speed over ground = ",a[3])
                print("\n")
                time.sleep(0.2)
                
        


