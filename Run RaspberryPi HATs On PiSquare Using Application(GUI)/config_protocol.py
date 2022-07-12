class I2C_Socket():
    def I2C_Read(device):
        ir = 'I2C'+ ','  + 'R' + ',' + device
        return ir        
        

    def I2C_Write(device,data):
        wr = 'I2C' + ','  + 'W' + ',' + device + ',' + data
        return wr
    

class UART_Socket():
    def UART_Read(device):
        ur = 'UART'+','+ 'R' + ',' + device
        return ur
        
    def UART_Write(device,data):
        uw = 'UART'+ ','+'W' + ',' + + device + ',' + data
        return uw


class GPIO_Socket():
    def GPIO_Read(gpio):
        gr = 'GPIO'+ ',' + gpio + ',' + 'R' 
        return gr
      

    def GPIO_Write(gpio,state):
        gw = 'GPIO'+ ',' + gpio + ',' + 'W' + ',' + state
        return gw
        
class SPI_Socket():
 
    def SPI_Read(device):
        sr = 'SPI'+','  + 'R' + ',' + device
        return sr
        
    def SPI_Write(device,data):
        sw = 'SPI'+ ',' + 'W' + ',' + device + ','  + data
        return sw   
