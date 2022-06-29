# PiSQUARE

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img.png" />

#### PiSquare is an RP2040 and ESP-12E-based board that allows you to use multiple Raspberry Pi HATs without stacking them on top of one other. PiSquare uses Socket programming to wirelessly communicate multiple Raspberry Pi HATs ("n" numbers of HATs).

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img2.png" />

#### You can utilise PiSquare in a variety of ways, as we were previously limited to utilising a single HAT on the Raspberry Pi or a maximum of three Raspberry Pi HATs using PiStack, but you can't link the same HATs on it twice (Like more than two UART or SPI based Raspberry Pi HAT at the same time) PiSquare allows you to attach as many HATs as you like to your Raspberry Pi without stacking them, whether they're SPI, I2C, or SPI HATs, and you can control them all wirelessly.

## PiSquare pins configuration is same as Raspberry pi pins configuration (like UART, I2C and SPI are in same place, so we can raspberry pi HAT'S in PiSquare)

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img3.png" />

## PiSquare Pins

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img4.JPG" />

## PiSquare Pins Function
<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img23.JPG" />

## Parts

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img1.png" />

## About PiSquare
  * RP2040 microcontroller with 2MB Flash
  * USB Type C port for power and data (and for reprogramming the Flash)
  * Exposes 25 multi-function 3.3V General Purpose I/O (GPIO)
  * 21 GPIO are digital-only and 3 are ADC capable

## Operating Condition
 * Operating Temp Max 85°C (including self-heating)
 * Operating Temp Min -20°C
 * VBUS 5V ± 10%.
 * VSYS Min 1.8V
 * VSYS Max 5.5V
 
## Parts specification
1. **ESP-12E(ESP8266MOD)**
    * Wi-Fi 2.4 GHz, support WPA/WPA2
    * Integrated low power 32-bit MCU
    * Operating Current: 80mA
    * 802.11 b/g/n
    * Operating Voltage: 3.0-3.6V
    * Operating temperature range -40C ~ 125C
   
2. **RP2040 Microcontroller IC**
   * Dual ARM Cortex-M0+ @ 133MHz
   * Support for up to 16MB of off-chip Flash memory via dedicated QSPI bus (External flash W25Q16JVSNIQ)
   * 264kB on-chip SRAM in six independent banks
   * On-chip programmable LDO to generate the core voltage
   * 2 on-chip PLLs to generate USB and core clocks
  
3. **Status Led**
   * Status led is connected to **GP24** Pin of PiSquare
   
4. **0.91 OLED Display**
   * Driving IC: SSD1306
   * Operating Voltage: 3.3-5V
   * Resolution Ratio: 128 x 32
   * Text Color: White
   * Background Color: Black
   
5. **Three push buttons**
   * Reset button     (Reset pisquare)
   * Boot button      (Boot button of RP2040)
   * ESP Reset button (Reset button of ESP-12E module)

### With PiSquare you can do these things :-

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
   
2. In PiSquare we can use both MicroPython and CircuitPython, but we use micropython ( **use micropython** * )
   * Install **Micropython** in PiSquare
     first you need to press the boot button of PiSquare, then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new        device named "RPI-RP2". 
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />
        
     After this go to run->select interpreter,choose device,port and install micropython (install firmware)
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img2.png" />
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img3.png" />
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img4.png" />
        
   * Install **CircuitPython** in PiSquare
     Insert the circuit python to the PiSquare(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2"). for this first you need to        press the boot button then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new device named "RPI-RP2" drag this      file "adafruit-circuitpython- raspberry_pi_pico-en_US-7.1.1.uf2" to this device as shown in figure:
     this is the official website, or you can download from here https://circuitpython.org/board/raspberry_pi_pico/
     
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />  
     When you properly insert the circuitpython then you see a new device that looks like the below image:-
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />
     
      After this go to run->select interpreter,choose device and port
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img20.png" />
    
## Demo Codes
* **Led Blink code(led_blink.py)**
  * Control on board status led of PiSquare ( blue color led) 
  
* **pisquare_internal_temp.py**
  * Run this code to see PiSquare internal temperature
