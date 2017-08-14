# LED Dimming and RGB LED with BBC Micro:bit in C++

_Captured: 2017-08-09 at 17:53 from [toriilab.blogspot.de](https://toriilab.blogspot.de/2017/03/led-dimming-and-rgb-led-with-bbc.html?m=1)_

![](https://4.bp.blogspot.com/-9HapVc32m1c/WM7WKo0aDGI/AAAAAAAAB88/Ti9kCDStTJ8ItcqJ2bUCoC6eKk-Zs5F9QCLcB/s280/rgb2.png)

PWM is used in LED dimming; as the duty cycle of a PWM signal increases, the average voltage and power provided by the PWM increases. The intensity of an LED can be varied by pulse-width modulating the voltage across the LED. Adjustments to the intensity of the LED are made by simply varying the duty cycle of the PWM signal driving the LED.  
The BBC Micro:bit has the following pins. The pin name do not correspond to the pin names in software on the mbed C++ platform and are mapped by the following:

Pin GPIO  
MICROBIT_PIN_P0 P0_3  
MICROBIT_PIN_P1 P0_2  
MICROBIT_PIN_P2 P0_1  
MICROBIT_PIN_P3 P0_4  
MICROBIT_PIN_P4 P0_5   
MICROBIT_PIN_P5 P0_17  
MICROBIT_PIN_P6 P0_12  
MICROBIT_PIN_P7 P0_11  
MICROBIT_PIN_P8 P0_18  
MICROBIT_PIN_P9 P0_10  
MICROBIT_PIN_P10 P0_6  
MICROBIT_PIN_P11 P0_26  
MICROBIT_PIN_P12 P0_20  
MICROBIT_PIN_P13 P0_23  
MICROBIT_PIN_P14 P0_22  
MICROBIT_PIN_P15 P0_21  
MICROBIT_PIN_P16 P0_16  
MICROBIT_PIN_P19 P0_0  
MICROBIT_PIN_P20 P0_30

For this project, I am using the micro:bit, zbit:toolbelt board, an LED and a potentiometer. For LED dimming, any of the following pins can be used both for the potentiometer and LED.

Analog GPOIO Pins  
MICROBIT_PIN_P0  
MICROBIT_PIN_P1  
MICROBIT_PIN_P2  
MICROBIT_PIN_P3  
MICROBIT_PIN_P4  
MICROBIT_PIN_P10

I connected MICROBIT_PIN_P10 which is in analog input mode to the potentiometer. The value returned as a result is then written as the duty cycle to the LED. The LED is connected to MICROBIT_PIN_P4 in PWM mode. The micro:bit is programmed with C++ on the mbed platform with the following code:

![](https://2.bp.blogspot.com/-pEwLepbwpq0/WM7WhfiJ3iI/AAAAAAAAB9A/LwtHgF3tru4Us5JsrA3HSeUXUnRSjp--wCLcB/s280/rgb1.png)

Since I'm using a RGB LED, the micro:bit can also be programmed to change the colour of the LED with a key press. A video demonstration is shown below.
