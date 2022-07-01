import socket
import sys
import threading
import time
from queue import Queue
import config_protocol


JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 12420
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Handling connection from multiple clients and saving to a list
# Closing previous connections when server.py file is restarted

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout
            print("1010")
            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])

        except:
            print("Error accepting connections")

def start():
    while True:
        n = input('Enter client name : ')

        if 'c' in n:
            conn = get_target(n)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")


# Selecting the target
def get_target(n):
    try:
        target = n.replace('c ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        return conn

    except:
        print("Selection not valid")
        return None


def send_target_commands(conn):
    while True:
            n = input("Enter quit for another client = ")
            if n == 'quit':
                break
            if len(str.encode(n)) > 0:
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
                        conn.send(gpio_w.encode()) # Send data to clients
                        print('\n')
                        print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                        print('\n')

                    if a ==2:
                        x = input("Enter gpio pin  = ")
                        gpio_r = config_protocol.GPIO_Socket.GPIO_Read(x)
                        print(gpio_r)
                        conn.send(gpio_r.encode()) # Send data to clients
                        print('\n')
                        print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                        print('\n')
                    

                  if n == 2:
                        print("press 1 for I2C write")
                        print("press 2 for I2C read")
                        b = int(input("Enter your choice = "))

                        if b == 1:
                            x = input("Enter Device ")
                            y = int(input("Enter Data  = "))                            
                            i2c_w = config_protocol.I2C_Socket.I2C_Write(x,y)
                            print(i2c_w)
                            conn.send(i2c_w.encode()) # Send data to clients
                            print('\n')
                            print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                            print('\n')

                        if b == 2:
                            r = input("Enter Device  = ")
                            i2c_r = config_protocol.I2C_Socket.I2C_Read(r)
                            print(i2c_r)
                            conn.send(i2c_r.encode()) # Send data to clients
                            print('\n')
                            print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                            print('\n')
                    
                  if n == 3:
                    print("press 1 for uart write")
                    print("press 2 for uart read")
                    y = int(input("Enter your choice = "))
                    
                    if y == 1:
                        x = input("Enter Device = ")
                        y = input("Enter data  = ")
                        uart_w = config_protocol.UART_Socket.UART_Write(x,y)
                        conn.send(uart_w.encode()) # Send data to clients
                        print('\n')
                        print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                        print('\n')
                        
                    if y == 2:
                        x = input("Enter device  = ")
                        uart_r = config_protocol.UART_Socket.UART_Read(x)
                        conn.send(uart_r.encode()) # Send data to clients
                        print('\n')
                        print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                        print('\n')

                  if n == 4:
                    print("press 1 for SPI write")
                    print("press 2 for SPI read")
                    y = int(input("Enter your choice = "))
                    
                    if y == 1:
                        x = input("Enter device  = ")
                        y = input("Enter data  = ")
                        spi_w = config_protocol.SPI_Socket.SPI_Write(x,y)
                        conn.send(spi_w.encode()) # Send data to clients
                        print('\n')
                        print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                        print('\n')
                        
                    if y == 2:
                        x = input("Enter device  = ")
                        spi_r = config_protocol.SPI_Socket.SPI_Read(x)
                        conn.send(spi_r.encode()) # Send data to clients
                        print('\n')
                        print (conn.recv(1024).decode()) # Data receive from client (PiSquare) 
                        print('\n')

                        
             
# Create worker threads
def generate_workers():
    for _ in range(2):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
            
        if x == 2:
            start()
            
        queue.task_done()


def jobs_creation():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


generate_workers()
jobs_creation()
