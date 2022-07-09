# PiSquare Demo Code
* **Blink LEDs (led_blink.py)**
  * Control the onboard blue status LED on the PiSquare by running "led_blink.py"
  
* **PiSquare Internal Temperature (pisquare_internal_temp.py)**
  * See PiSquare internal temperature using "pisquare_internal_temp.py"
  
* **Light Dependant Resistor (ldr.py)** 
  * Measure the relative resistance of an LDR connected to the PiSquare, using the circuit shown below. The resistor is 10kOhms. The circuit is known as a 'voltage divider'
  <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img27.jpg" />
  <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img28.png" />
  
* **Onboard OLED Test (oled_test.py)**

  * Before running this script, you need to install the "micropython-ssd1306" MicroPython library. This should be done from Thonny.
  * With the PiSquare connected, select Tools->Manage Packages...
  * In the search bar, type "micropython-ssd1306", or "adafruit-circuitpython-ssd1306" if you are using Circuit Python.
  * Select the appropriate library from the list (it should be the top one) and click on 'Install' to install the latest version.
  * Inside the 'Onboard OLED Test' folder load "oled_test.py" in Thonny and run it.
  
  <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img24.jpg" />

* **Servo Motors (servo_motor.py)**
  * Connect up a servo motor as shown in the image below:

    <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img25.jpg" />
  
  * Run the server_motor.py code.

* **16x2 LCD Display (lcd_display_16x2_demo.py)**

  * As with the inbuilt OLED screen, you need to install a couple of libraries. These are not currently available from PyPi, so you are going to use the alternative method of installing libraries.
  * In Thonny, open both "pico_i2c_lcd.py" and "lcd_api.py", then use File->Save Copy...  This will present a dialog box allowing you to choose between saving to your local computer or "Raspberry Pi Pico". Choose the Pico.
  * Save the files into the "lib" folder with their current names.
  * Load and run "lcd_16x2_test.py"
  
  <img src = "https://github.com/sbcshop/PiSquare/blob/main/images/img26.jpg" />
  
* **Measuring the relative resistance of a potentiometer (potentiometer_test.py)**

  * Use the same circuit as the LDR, but replace the LDR with a potentiometer.
  * Run "potentiometer_test.py"
