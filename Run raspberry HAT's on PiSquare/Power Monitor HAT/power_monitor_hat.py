from machine import Pin, I2C
from ina219 import INA219
from logging import INFO

SHUNT_OHMS = 0.1

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

addr1=0x40
addr2=0x41
addr3=0x42

ina1 = INA219(SHUNT_OHMS, i2c,addr1,log_level=INFO)
ina2 = INA219(SHUNT_OHMS, i2c,addr2,log_level=INFO)
ina3 = INA219(SHUNT_OHMS, i2c,addr3,log_level=INFO)

ina1.configure()
ina2.configure()
ina3.configure()

print("Bus Voltage1: %.3f V" % ina1.voltage(),"Current1: %.3f mA" % ina1.current(),"Power1: %.3f mW" % ina1.power())

print("Bus Voltage2: %.3f V" % ina2.voltage(),"Current2: %.3f mA" % ina2.current(),"Power2: %.3f mW" % ina2.power())

print("Bus Voltage3: %.3f V" % ina3.voltage(),"Current3: %.3f mA" % ina3.current(),"Power3: %.3f mW" % ina3.power())
