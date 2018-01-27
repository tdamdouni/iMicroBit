# Debugging micro:bit code using the serial port and USB

_Captured: 2017-12-28 at 11:32 from [bluetooth-mdw.blogspot.de](http://bluetooth-mdw.blogspot.de/2017/12/debugging-microbit-code-using-serial.html)_

Debugging micro:bit code can be tricky. It can only display one character at a time so the LED display is not a great option, though you'll be surprised how much you can still get done when you need to.

You can write full strings and variable values to the serial port however and so by connecting your micro:bit into a computer using a USB cable and firing up a terminal application like Putty, you can monitor serial output as your micro:bit code executes.

This is a great way to get to the bottom of weird code problems you just can't figure out!

Here's how you'd do this from C/C++
    
    
    uBit.serial.printf("P0:%d P1:%d P8:%d P12:%d\r\n", pin0, pin1, pin8, pin12); 

![](https://1.bp.blogspot.com/-bmDfB5dYOUk/Wj4dmdqzjGI/AAAAAAAAM_c/kcrEYJFPb4I5fm9XIbHHzFZAVrRgS7P5QCLcBGAs/s640/mb_putty.png)
