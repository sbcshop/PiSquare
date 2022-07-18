# PiSQUARE

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img.png" />

#### PiSquare is an RP2040 and ESP-12E-based board that allows you to use multiple Raspberry Pi HATs without stacking them on top of one other. PiSquare uses Socket programming to wirelessly communicate with multiple Raspberry Pi HATs ("n" numbers of HATs).

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img2.png" />

#### You can use the PiSquare in a variety of ways. Previously you were limited to using a single HAT on the Raspberry Pi, or a maximum of three HATs using PiStack or equivalent, but you can't use two of the same HATs on it at once (e.g. two UART or SPI based HATs.). PiSquare allows you to attach as many HATs as you like to your Raspberry Pi without stacking them, whether they're SPI, I2C, or SPI HATs, and you can control them all wirelessly.

## The PiSquare pin configuration matches the Raspberry Pi pin configuration (like UART, I2C and SPI).

<img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img3.png" />

## In PiSquare Pin 16 is Not Connected(NC), it Means Those Hat which Uses GPIO23 Pin In Raspberry Pi will not work(only GPIO23 pin not work rest Pin work like SPI,UART and I2C)

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

## Operating Conditions
 * Operating Temp Max 85°C (including self-heating)
 * Operating Temp Min -20°C
 * VBUS 5V ± 10%.
 * VSYS Min 1.8V
 * VSYS Max 5.5V
 
## Parts specification
1. **ESP-12E(ESP8266MOD)**
    * Wi-Fi 2.4 GHz, support for WPA/WPA2
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

### Example PiSquare scenarios:

* **Create a server on the Raspberry Pi with one or more PiSquares as clients with multiple HATs**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif1.gif" />
    
* **Create a server on a PiSquare with one or more PiSquare clients**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif2.gif" />

* **Use a Moble phone as the server with one or more PiSquare clients**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif3.gif" />
    
* **Create a hotspot on a Raspberry Pi and connect one or more PiSquares to the Raspberry Pi (without using a router)**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif4.gif" />

* **Create a hotspot on a PiSquare and connect one or more PiSquares (without using a router)**
    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/gif5.gif" />

## Setting up the PiSquare 
### The PiSquare support C/C++, MicroPython and CircuitPython

For MicroPython/CircuitPython

1. Download the Thonny IDE 

   https://thonny.org/
   
   <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img.JPG" />
   
2. The PiSquare we can use both MicroPython and CircuitPython, but in these instructions we use MicroPython

   * Installing **MicroPython** on the PiSquare

     Before connecting the PiSquare to your PC, press and hold the Boot button, then connect the USB.  Don't release the button until you connect the USB your PC. Release the Boot button once you see a new 'drive' named "RPI-RP2".
     
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />
        
     In Thonny, select Run->Select Interpreter.  Choose the 'MicroPython (Raspberry Pi Pico)' interpreter, the port the PiSquare is attached to, and click on 'Install or update firmware'.
     
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img2.png" />
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img3.png" />
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img4.png" />
        
   * Installing **CircuitPython** on the PiSquare
   
      Download the AdaFruit CircuitPython firmware from here: https://circuitpython.org/board/raspberry_pi_pico/
   
      Before connecting the PiSquare to your PC, press and hold the Boot button, then connect the USB.  Don't release the button until you connect the USB your PC. Release the Boot button once you see a new 'drive' named "RPI-RP2".

     Drag the UF2 file (e.g. "adafruit-circuitpython- raspberry_pi_pico-en_US-7.1.1.uf2") to this drive as shown below:
          
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />

     The PiSquare will restart and a new 'drive' connected:
     
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />
     
     In Thonny, select Run->Select Interpreter.  Choose the 'CircuitPython (generic)' interpreter and the port the PiSquare is attached to.
     
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
     
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
     
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img20.png" />
    
