"""
Created by SB COMPONENTS
"""
from tkinter import*
try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter as tk 
from PIL import Image, ImageTk
from datetime import datetime
from time import sleep

import numpy as np
import ctypes
import os

import socket
from tkinter import font as tkFont

#from _thread import *
import threading

from threading import Thread

import threading
import time
from queue import Queue
import config_protocol
from tkinter import font as tkFont


NUMBER_OF_THREADS = 3
JOB_NUMBER = [1, 2,3]
queue = Queue()
all_connections = []
all_address = []

#ctypes.windll.shcore.SetProcessDpiAwareness(1) # it increase the window clearity
root = Tk()
photo = PhotoImage(file = "icon/icon.png")
root.iconphoto(False, photo) # set the icon to the window
root.title('PiSquare Controller')
#root.attributes('-fullscreen', True) # it turn screen in full mode

root.bind("<Escape>", exit) #press escape to exit window

root.geometry("1920x1080+-8+-8")
root['bg'] = 'light blue'

lbl=Label(root,text ="PISQUARE WIFI CONTROLLER",fg ='red2' , font =("times new roman", 70),bg='light blue')
lbl.place(x=300,y=10)

lbl1=Label(root,text ="Scan clients",fg ='dark green' , font =("times new roman", 40),bg='light blue')
lbl1.place(x=80,y= 220)

lst  = []

def Client_Socket():
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

        lst = []

        def accepting_connections():
            #print()
            for c in all_connections:
                c.close()

            del all_connections[:]
            del all_address[:]
            lst2 = []
            while True:
                try:
                    conn, address = s.accept()
                    s.setblocking(1)  # prevents timeout

                    all_connections.append(conn)
                    all_address.append(address)
                    #print("asd",address)
                    #global ad
                    print("##### = ",all_connections)
                    print(len(all_connections))
                    global ad
                    ad = str(all_address)#[1:-1]
                    print("ad  ==",ad)
                    
                    rx_label = Label(root,text = ad, justify="left", anchor="nw",
                                 wraplength=300,font =("times new roman", 18),
                                 bg="white", fg="black",
                                 bd=2, height=18, width=22, padx=10, pady=10)
                    rx_label.place(x=80, y=385)
                    '''
                    #print("asd = ", asd)
                    res = list(eval(ad))
                    resq = list(ad)
                    print("res= ",res)
                    print("resq = ",resq)
                    for i in range(len(res)):
                        res1 = str(res[i])[1:-1]
                        print("res1 = ",res1)
                        x = res1.split(",")
                        x = x[0].replace("'", "")
                        print(x)
                        lst.append(x)
                    print("lst1",lst)
                    '''
                    '''
                    helv25 = tkFont.Font(family='Helvetica', size=25)
                    global comm_Option5
                    comm_Variable5 = tk.StringVar()
                    
                    comm_Variable5.set("Choose Client")
                    comm_Option5 = tk.OptionMenu(root, comm_Variable5,*lst)
                    comm_Option5.config(font=helv25)
                    comm_Option5.config(bg='violet')

                    helv16 = tkFont.Font(family='Helvetica', size=16)
                    menu = root.nametowidget(comm_Option5.menuname)
                    menu.config(font=helv16)  # Set the dropdown menu's font
                    comm_Option5.place(x=420,y=300,width=270,height=40)

                    print("Connection has been established :" + address[0])
                    '''


                    return ad
                except:
                    print("Error accepting connections")

                print("####### = ",all_address)
        def start_control():
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            asd = accepting_connections()
            
            print("asd = ", asd)
            res = list(eval(asd))
            resq = list(asd)
            print("res= ",res)
            print("resq = ",resq)
            for i in range(len(res)):
                res1 = str(res[i])[1:-1]
                print("res1 = ",res1)
                x = res1.split(",")
                x = x[0].replace("'", "")
                print(x)
                lst.append(x)
                
            rx_label = Label(root,text = ad, justify="left", anchor="nw",
                                 wraplength=300,font =("times new roman", 18),
                                 bg="white", fg="black",
                                 bd=2, height=18, width=22, padx=10, pady=10)
            rx_label.place(x=80, y=385)
            
            print("lst1***",set(lst))
            helv25 = tkFont.Font(family='Helvetica', size=25)
            comm_Variable5 = tk.StringVar()

            comm_Variable5.set("Choose Client")
            comm_Option5 = tk.OptionMenu(root, comm_Variable5,*set(lst))
            comm_Option5.config(font=helv25)
            comm_Option5.config(bg='violet')

            helv16 = tkFont.Font(family='Helvetica', size=16)
            menu = root.nametowidget(comm_Option5.menuname)
            menu.config(font=helv16)  # Set the dropdown menu's font
            comm_Option5.place(x=420,y=300,width=270,height=40)
            
            
            def set_text():
                            n = comm_Variable5.get()
                            print("***n******* = ",n)
                            conn = get_target(n)
                            if conn is not None:
                                        send_target_commands(conn)
                                        

            lbl1=Label(root,text ="Select Client",fg ='black' , font =("times new roman", 40),bg='light blue')
            lbl1.place(x=420,y= 220)
            btn3 = Button(root, text = 'enter',bg='yellow', bd = '5',command=set_text,activebackground='#00ff00') # this create submit button of entry box, it submit the mail
            btn3.place(x=700, y=300)
        
        def get_target(n):
            try:
                x = lst.index(n)
                conn = all_connections[x]
                print("You are now connected to :" + str(all_address[x][0]))
                return conn
       
            except:
                print("Selection not valid")
                return None
        


        def send_target_commands(conn): 
                  lbl2=Label(root,text ="Select Communication",fg ='black' , font =("times new roman", 40),bg='light blue')
                  lbl2.place(x=900,y= 220)
                  
                  lbl2=Label(root,text ="GPIO Devices",fg ='dark green' , font =("times new roman", 30),bg='light blue')
                  lbl2.place(x=820,y= 300)

                  lbl2=Label(root,text ="UART Devices",fg ='dark green' , font =("times new roman", 30),bg='light blue')
                  lbl2.place(x=1370,y= 300)

                  lbl2=Label(root,text ="I2C Devices",fg ='dark green' , font =("times new roman", 30),bg='light blue')
                  lbl2.place(x=820,y= 650)
                  
                  lbl2=Label(root,text ="SPI Devices",fg ='dark green' , font =("times new roman", 30),bg='light blue')
                  lbl2.place(x=1370,y= 650)

                  lbl2=Label(root,text ="Write",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=820,y= 380)

                  lbl2=Label(root,text ="Read",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=820,y= 440)

                  lbl2=Label(root,text ="Write",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=820,y= 720)

                  lbl2=Label(root,text ="Read",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=820,y= 785)

                  lbl2=Label(root,text ="Write",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=1370,y= 380)

                  lbl2=Label(root,text ="Read",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=1375,y= 440)
                  
                  lbl2=Label(root,text ="Write",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=1370,y= 720)

                  lbl2=Label(root,text ="Read",fg ='red' , font =("times new roman", 25),bg='light blue')
                  lbl2.place(x=1375,y= 785)


                  
                  def config():
                                
                          def gpio_control():
                                            
                                            gp = ['GPIO0','GPIO1','GPIO2','GPIO3','GPIO6',
                                                 'GPIO7','GPIO8','GPIO9','GPIO10','GPIO11',
                                                 'GPIO12','GPIO13','GPIO14','GPIO15','GPIO16',
                                                 'GPIO17','GPIO18','GPIO19','GPIO20','GPIO21',
                                                 'GPIO22','GPIO23','GPIO24','GPIO25','GPIO26',
                                                 'GPIO27','GPIO28']
                                            global comm_Option2
                                            global comm_Option3

                                            comm_Variable2 = tk.StringVar()                                                                              
                                            comm_Variable2.set("GPIO26")
                                            comm_Option2 = tk.OptionMenu(root, comm_Variable2,*gp)
                                            comm_Option2.place(x=900,y=380,width=100,height=40)

                                            comm_Variable3 = tk.StringVar()                                                                              
                                            comm_Variable3.set("1")
                                            comm_Option3 = tk.OptionMenu(root, comm_Variable3,'0','1')
                                            comm_Option3.place(x=1010,y=380,width=100,height=40)
                                        
                                            def write_pin():
                                                x = comm_Variable2.get()
                                                y = comm_Variable3.get()
                                                gpio_w = config_protocol.GPIO_Socket.GPIO_Write(x,y)
                                                print(gpio_w)
                                                conn.send(gpio_w.encode()) # send a thank you message to the client. encoding to send byte type.
                                                print (conn.recv(1024).decode())
                                                                                           
                                            global btn6
                                            btn6 = Button(root, text = 'Click11',bg='yellow', bd = '5',command=write_pin,activebackground='#00ff00') 
                                            btn6.place(x=1120, y=380)

                                            gp_r = ['GPIO0','GPIO1','GPIO2','GPIO3','GPIO6',
                                                 'GPIO7','GPIO8','GPIO9','GPIO10','GPIO11',
                                                 'GPIO12','GPIO13','GPIO14','GPIO15','GPIO16',
                                                 'GPIO17','GPIO18','GPIO19','GPIO20','GPIO21',
                                                 'GPIO22','GPIO23','GPIO24','GPIO25','GPIO26',
                                                 'GPIO27','GPIO28']
                                            
                                            
                                            comm_Variable4 = tk.StringVar()                                                                              
                                            comm_Variable4.set("GPIO25")
                                            comm_Option4 = tk.OptionMenu(root, comm_Variable4,*gp_r)
                                            comm_Option4.place(x=900,y=445,width=100,height=40)
                                            
                                            gpio_label = Label(root,text = "", justify="left", anchor="nw",
                                                             wraplength=300,font =("times new roman", 15),
                                                             bg="white", fg="black",
                                                             bd=2, height=5, width=40, padx=10, pady=10)
                                            gpio_label.place(x=820, y=500)                                           

                                            def read_pin():
                                                x1 = comm_Variable4.get()
                                                gpio_r = config_protocol.GPIO_Socket.GPIO_Read(x1)
                                                print(gpio_r)
                                                conn.send(gpio_r.encode()) # send a thank you message to the client. encoding to send byte type.
                                                dat = conn.recv(1024).decode()
                                                gpio_label = Label(root,text = dat, justify="left", anchor="nw",
                                                                 wraplength=300,font =("times new roman", 15),
                                                                 bg="white", fg="black",
                                                                 bd=2, height=5, width=40, padx=10, pady=10)
                                                gpio_label.place(x=820, y=500)
                                            global but_1
                                            btn_1 = Button(root, text = 'Click',bg='yellow', bd = '5',command=read_pin,activebackground='#00ff00') 
                                            btn_1.place(x=1010, y=445)
                          gpio_control()

                                
                          ###################################UART#######
                          def Uart():
                                def uart_control():
                                        
                                            #br1 = ['9600','115200']

                                            large_font=('Verdana',20)
                                            name8=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                            name8.place(x=1635,y=380)
                                            name8.focus_set()
                                            
                                            name=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                            name.place(x=1450,y=380)
                                            name.focus_set()
 
                                            def write_pin():
                                                x = nmae8.get()
                                                y = name.get()
                                                
                                                uart_w = config_protocol.UART_Socket.UART_Write(y,x)
                                                conn.send(uart_w.encode()) # send a thank you message to the client. encoding to send byte type.
                                                print (conn.recv(1024).decode())
                                            btn9 = Button(root, text = 'Click',bg='yellow', bd = '5',command=write_pin,activebackground='#00ff00') 
                                            btn9.place(x=1820, y=380)
                                            ################################# UART READ #####################
                                            
                                            br2 = ['9600','115200']
  
                                            large_font=('Verdana',20)
                                            name1=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                            name1.place(x=1450,y=450)
                                            name1.focus_set()
                                            uart_label = Label(root,text = " ", justify="left", anchor="nw",
                                                                 wraplength=300,font =("times new roman", 15),
                                                                 bg="white", fg="black",
                                                                 bd=2, height=5, width=40, padx=10, pady=10)
                                            uart_label.place(x=1370, y=500)

                                            def read_pin():
                                                y1 = name1.get()
                                                uart_r = config_protocol.UART_Socket.UART_Read(y1)
                                                conn.send(uart_r.encode()) # send a thank you message to the client. encoding to send byte type.
                                                udat = conn.recv(1024).decode()
                                                uart_label = Label(root,text = udat, justify="left", anchor="nw",
                                                                     wraplength=300,font =("times new roman", 15),
                                                                     bg="white", fg="black",
                                                                     bd=2, height=5, width=40, padx=10, pady=10)
                                                uart_label.place(x=1370, y=500)
                                                
                                            btn10 = Button(root, text = 'Click',bg='yellow', bd = '5',command=read_pin,activebackground='#00ff00') 
                                            btn10.place(x=1635, y=450)

                                uart_control()


                          Uart()  
                          def I2c():
                                large_font=('Verdana',20)
                                name3=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                name3.place(x=900,y=720)
                                name3.focus_set()

                                name4=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                name4.place(x=1085,y=720)
                                name4.focus_set()

                                def write_i2c():
                                    x = name3.get()
                                    y = name4.get()
                                    
                                    i2c_w = config_protocol.I2C_Socket.I2C_Write(x,y)
                                    print(i2c_w)
                                    conn.send(i2c_w.encode()) # send a thank you message to the client. encoding to send byte type.
                                    print (conn.recv(1024).decode())
                                btn11 = Button(root, text = 'Click',bg='yellow', bd = '5',command=write_i2c,activebackground='#00ff00') 
                                btn11.place(x=1270, y=720)

                                name5=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                name5.place(x=900,y=790)
                                name5.focus_set()
                                i2c_label = Label(root,text = " ", justify="left", anchor="nw",
                                                        wraplength=300,font =("times new roman", 15),
                                                        bg="white", fg="black",
                                                        bd=2, height=7, width=40, padx=10, pady=10)
                                i2c_label.place(x=820, y=850)
                                
                                def i2c_read():
                                    r = name5.get()
                                    i2c_r = config_protocol.I2C_Socket.I2C_Read(r)
                                    print(i2c_r)
                                    conn.send(i2c_r.encode()) # send a thank you message to the client. encoding to send byte type.
                                    de = conn.recv(1024).decode()
                                    i2c_label = Label(root,text = de, justify="left", anchor="nw",
                                                        wraplength=300,font =("times new roman", 15),
                                                        bg="white", fg="black",
                                                        bd=2, height=7, width=40, padx=10, pady=10)
                                    i2c_label.place(x=820, y=850)

                                btn12 = Button(root, text = 'Click',bg='yellow', bd = '5',command=i2c_read,activebackground='#00ff00') 
                                btn12.place(x=1085, y=790)
                          I2c() 


                          def Spi():
                                large_font=('Verdana',20)
                                name5=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                name5.place(x=1450,y=720)
                                name5.focus_set()

                                name6=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                name6.place(x=1635,y=720)

                                def Spi_write():
                                    x = name5.get()
                                    y = name6.get()
                                    spi_w = config_protocol.SPI_Socket.SPI_Write(x,y)
                                    conn.send(spi_w.encode()) # send a thank you message to the client. encoding to send byte type.
                                    print (conn.recv(1024).decode())
                                btn12 = Button(root, text = 'Click',bg='yellow', bd = '5',command=Spi_write,activebackground='#00ff00') 
                                btn12.place(x=1820, y=720)
                                
                                name7=Entry(root,width=10,font=large_font,fg = 'DarkOrange3') # this create entry box to write name     
                                name7.place(x=1450,y=790)
                                name7.focus_set()
                                spi_label = Label(root,text = " ", justify="left", anchor="nw",
                                                        wraplength=300,font =("times new roman", 15),
                                                        bg="white", fg="black",
                                                        bd=2, height=7, width=40, padx=10, pady=10)
                                spi_label.place(x=1370, y=850)
                                
                                def Spi_read():
                                    x = name7.get()
                                    spi_r = config_protocol.SPI_Socket.SPI_Read(x)
                                    conn.send(spi_r.encode()) # send a thank you message to the client. encoding to send byte type.
                                    dr = conn.recv(1024).decode()
                                    spi_label = Label(root,text = dr, justify="left", anchor="nw",
                                                            wraplength=300,font =("times new roman", 15),
                                                            bg="white", fg="black",
                                                            bd=2, height=7, width=40, padx=10, pady=10)
                                    spi_label.place(x=1370, y=850)
                                    
                                btn12 = Button(root, text = 'Click',bg='yellow', bd = '5',command=Spi_read,activebackground='#00ff00') 
                                btn12.place(x=1638, y=790)
                          Spi()
                          
                  config()
                            
           
        # Create worker threads
        def create_workers(): 
            for _ in range(NUMBER_OF_THREADS):
                t = Thread(target=work)
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
                    #accepting_connections()
                    
                    
                if x == 2:
                    start_control()
                #accepting_connections()
                queue.task_done()
                #accepting_connections()
                


        def create_jobs():
            for x in JOB_NUMBER:
                queue.put(x)

            queue.join()


        create_workers()
        create_jobs()

          
def threading():
    t1=Thread(target=Client_Socket)
    t1.daemon = True
    t1.start()
    #t1.join()

rx_label = Label(root,text = " ", justify="left", anchor="nw",
                    wraplength=300,font =("times new roman", 18),
                    bg="white", fg="black",
                    bd=2, height=18, width=22, padx=10, pady=10)
rx_label.place(x=80, y=385)

btn1 = Button(root, text = 'Scan Clients',bg='yellow', bd = '5',command=threading,activebackground='#00ff00') # this create submit button of entry box, it submit the mail
btn1.place(x=80, y=300)


root.mainloop()
