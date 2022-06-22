# import the socket library
import socket            
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

# Choose any port number,make sure same port number is also in PiSquare
port = 12420          
 
# Next bind to the portl
socket_obj.bind(('', port))        
print ("socket binded to %s" %(port))

socket_obj.listen(5) # put the socket into listening mode  
print ("socket is listening")

conn, addr = socket_obj.accept() # Establish connection with client.
print ('Server got connection from', addr )

conn.send(data.encode()) # data send to client

print (conn.recv(1024).decode()) # data receive from client

while True:
  n = input("enter data you need to send = ")
  conn.send(n.encode())

conn.close
   
