# PiSQUARE
## In this repository we control raspberry Pi hats, through (wifi) TCP Protocol.Raspberry pi Hats are fix(connect) to PiSqure.
### Let's talk about how whole thing work, Connect PiSquare(having pi Hat's) to Raspberry pi using wifi.Then we control raspberry pi HAT(client)'s using raspberry pi (server), here we use socket programming.Make sure all the HAT'S which has library,need to save inside the PiSquare.You can add as many library.

* **Create the server from Raspberry Pi and PiSquare as client, run multiple HAT , vice-versa (with router)**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif1.gif" />
    
* **Create Hotspot on Raspberry Pi and connect PiSquares to raspberry pi (without router)**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif4.gif" />
    
    
## Install necessary libraries in Raspberry Pi :
```pip install sockets```

**or**

```sudo apt-get install socket```

## There are two folders in this repository:  
#### In Single socket, you can connect one client to the server(Raspberri pi), and send ,receive data
### 1. Single socket
   * **config_protocol.py - This is the library used in raspberry pi, it configure protocol**
   * **raspberrypi_server_run_hat.py - Run this file in Raspberry pi(server),Connect the raspberry pi to the router, make sure both PiSquare and raspberry pi connect        to same network**
   * **pisquare_client_run_hat.py - Run the file to PiSquare to make client, connect client to the router, copy and paste the raspberry pi IP this code** 
   * **(Folder)Libraries - Inside this folder there are some libraries, you need to save these libraries inside PiSquare.one exapmle(OLED library) show below steps, same as save all      the libraries**
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img7.png" />
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img10.png" />
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img9.png" />
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img8.png" />


### 2. Multiple Sockets
#### In multiple sockets, you can connect many client to the server(Raspberri pi), and send ,receive data simultaneously
   * **config_protocol.py - This is the library used in raspberry pi, it configure protocol**
   * **raspberrypi_multiple_socket_hats.py - Run this file in Raspberry pi(server),Connect the raspberry pi to the router, make sure both PiSquare and raspberry pi          connect to same network**
   * **pisquare_multiple_client_run_hats.py - Run the file to PiSquare to make client, connect client to the router,copy and paste the raspberry pi IP this code** 
   * **(Folder)Libraries - Inside this folder there are some libraries, you need to save these libraries inside PiSquare.one exapmle(OLED library) show below steps, same as save all      the libraries**
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img7.png" />
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img10.png" />
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img9.png" />
   <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img8.png" />

## Working
<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img19.png" />
<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img20.png" />
<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img21.png" />
<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img22.png" />
