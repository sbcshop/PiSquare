import socket
import sys
import threading
import time
from queue import Queue

port = 12420

JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []

num = 0

# Create a Socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    except socket.error as msg:
        print("Socket error: " + str(msg))


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

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]
    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout
            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0]+"  client")
            

        except:
            print("Error accepting connections")



def start():
    while True:
        n = input('Enter client name : ')
        if'c' in n:
            conn = get_target(n)
            if conn is not None:
                send_target_commands(conn)

        else:
            print("Command not recognized")


# Selecting the target
def get_target(n):
    try:
        target = n.replace('c ', '')  # target = id
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
                  n = input("Enter data you need to send = ")
                  conn.send(n.encode()) 
        

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
