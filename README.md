# PiSQUARE

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img.png" />

### PiSquare is an RP2040 and ESP-12E-based board that allows you to use multiple Raspberry Pi HATs without stacking them on top of one other. PiSquare uses Socket programming to wirelessly communicate multiple Raspberry Pi HATs ("n" numbers of HATs).

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img2.png" />

### You can utilise PiSquare in a variety of ways, as we were previously limited to utilising a single HAT on the Raspberry Pi or a maximum of three Raspberry Pi HATs using PiStack, but you can't link the same HATs on it twice (Like more than two UART or SPI based Raspberry Pi HAT at the same time) PiSquare allows you to attach as many HATs as you like to your Raspberry Pi without stacking them, whether they're SPI, I2C, or SPI HATs, and you can control them all wirelessly.

## Parts

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img1.png" />

### With PiSquare you can make :-

* **Create the server from Raspberry Pi and PiSquare as client, run multiple HAT , vice-versa**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif1.gif" />
    
* **Make the PiSquare client and other all PiSquare as server, vice-versa**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif2.gif" />

* **Make Moble phone as server and other PiSquare as clients, vice-versa and Run any HAT on single PiSquare and control it via your phone**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif3.gif" />
    
* **Create Hotspot on Raspberry Pi and connect PiSquares to raspberry pi (without router)**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif4.gif" />

* **Create hotspot on PiSquare and connect PiSquare to other PiSquares (without router)**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif5.gif" />

## Setup PiSquare 
1. Download Thonny IDE 

   https://thonny.org/
   
   <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img.JPG" />
   
2. In PiSquare we use both MicroPython and CircuitPython, but we use micropython
   * Install **Micropython** in PiSquare
     first you need to press the boot button of PiSquare, then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new        device named "RPI-RP2". 
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />
        
     After this go to run->select interpreter,choose device,port and install micropython (install firmware)
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img2.png" />
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img3.png" />
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img4.png" />
        
   * Install **CircuitPython** in PiSquare
     Insert the circuit python to the PiSquare(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2"). for this first you need to        press the boot button then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new device named "RPI-RP2" drag this      file "adafruit-circuitpython- raspberry_pi_pico-en_US-7.1.1.uf2" to this device as shown in figure:
     this is the official website, or yoy can download from here https://circuitpython.org/board/raspberry_pi_pico/
     
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />  
     When you properly insert the circuitpython then you see a new device that looks like the below image:-
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />
     
      After this go to run->select interpreter,choose device and port
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img20.png" />
    
