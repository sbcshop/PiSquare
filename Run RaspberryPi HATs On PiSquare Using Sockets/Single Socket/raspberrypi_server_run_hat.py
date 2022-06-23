# import the socket library
import socket
import config_protocol

# Choose any port number,make sure same port number is also in PiSquare
port = 12420    
BUFFER_SIZE = 1024

# next create a socket object
def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP
ip = extract_ip()

data = "S:"+ip

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
print ("Socket successfully created")
socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Next bind to the portl
socket_obj.bind(('', port))        
print ("socket binded to %s" %(port))

socket_obj.listen(5) # put the socket into listening mode  
print ("socket is listening")

conn, addr = socket_obj.accept() # Establish connection with client.
print ('Server got connection from', addr )


while True:

                  print("1 - GPIO")
                  print("2 - I2C")
                  print("3 - UART")
                  print("4 - SPI")
                  
                  n = int(input("Enter your choice = "))
                  
                  if n == 1:
                    print("press 1 for gpio write")
                    print("press 2 for gpio read")
                    a = int(input("Enter your choice = "))
                    
                    if a == 1:
                        x = input("Enter gpio pin  = ")
                        y = input("Enter state  = ")
                        gpio_w = config_protocol.GPIO_Socket.GPIO_Write(x,y)
                        print(gpio_w)
                        conn.send(gpio_w.encode()) #Send data to client
                        print('\n')
                        print (conn.recv(1024).decode())
                        print('\n')

                    if a ==2:
                        x = input("Enter gpio pin  = ")
                        gpio_r = config_protocol.GPIO_Socket.GPIO_Read(x)
                        print(gpio_r)
                        conn.send(gpio_r.encode()) #Send data to client
                        print('\n')
                        print (conn.recv(1024).decode())
                        print('\n')
                    

                  if n == 2:
                        print("press 1 for I2C write")
                        print("press 2 for I2C read")
                        b = int(input("Enter your choice = "))

                        if b == 1:
                            x = input("Enter frequency  = ")
                            y = int(input("Enter address  = "))
                            add = str(hex(y))
                            z = input("Enter data  = ")
                            
                            i2c_w = config_protocol.I2C_Socket.I2C_Write(x,add,z)
                            print(i2c_w)
                            conn.send(i2c_w.encode()) #Send data to client
                            print('\n')
                            print (conn.recv(1024).decode())
                            print('\n')

                        if b == 2:
                            w = input("Enter frequency  = ")
                            i2c_r = config_protocol.I2C_Socket.I2C_Read(w)
                            print(i2c_r)
                            conn.send(i2c_r.encode()) #Send data to client
                            print('\n')
                            print (conn.recv(1024).decode())
                            print('\n')                           
                    
                  if n == 3:
                    print("press 1 for uart write")
                    print("press 2 for uart read")
                    y = int(input("Enter your choice = "))
                    
                    if y == 1:
                        x = input("Enter baudrate  = ")
                        y = input("Enter data  = ")
                        uart_w = config_protocol.UART_Socket.UART_Write(x,y)
                        conn.send(uart_w.encode()) #Send data to client
                        print('\n')
                        print (conn.recv(1024).decode())
                        print('\n')
                        
                    if y == 2:
                        x = input("Enter device  = ")
                        uart_r = config_protocol.UART_Socket.UART_Read(x)
                        conn.send(uart_r.encode()) #Send data to client
                        print('\n')
                        print (conn.recv(1024).decode())
                        print('\n')
                        
                  if n == 4:
                    print("press 1 for SPI write")
                    print("press 2 for SPI read")
                    y = int(input("Enter your choice = "))
                    
                    if y == 1:
                        x = input("Enter device  = ")
                        y = input("Enter data  = ")
                        spi_w = config_protocol.SPI_Socket.SPI_Write(x,y)
                        #print(uart_w)
                        conn.send(spi_w.encode()) #Send data to client
                        print('\n')
                        print (conn.recv(1024).decode())
                        print('\n')
                        
                    if y == 2:
                        x = input("Enter device  = ")
                        spi_r = config_protocol.SPI_Socket.SPI_Read(x)
                        #print(uart_r)
                        conn.send(spi_r.encode()) #Send data to client
                        print('\n')
                        print (conn.recv(1024).decode())
                        print('\n')

conn.close
   
