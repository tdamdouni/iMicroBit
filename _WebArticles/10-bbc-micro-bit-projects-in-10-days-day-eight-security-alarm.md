# 10 BBC micro:bit Projects in 10 Days: Day Eight - Security Alarm

_Captured: 2017-09-14 at 11:54 from [www.element14.com](https://www.element14.com/community/community/stem-academy/microbit/blog/2016/06/15/10-bbc-microbit-projects-in-10-days-day-eight-security-alarm)_

**About this project**

This project demonstrates how the BBC micro:bit's functions can be enhanced with external devices, in this case a [3V buzzer](http://cpc.farnell.com/kingstate/kpeg-350/buzzer-piezo/dp/LS02970?COM=June) that can be programmed to act as a security alarm.

**What you'll need**

_1 x BBC micro:bit_

_1 x Micro USB_

_1 x Computer or tablet_

_2 x AAA Batteries & Battery Holder_

_2 x Crocodile Clips_

****Project ****walkthrough****

  * Go to the [BBC micro:bit website](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fwww.microbit.co.uk%2F), click 'create code' and begin a new Microsoft Block Editor project.
  * Start by dragging in a 'forever' loop from the basic commands menu.
  * To create a variable for tracking movement, drag in a 'set [item] to' tile and rename the variable to 'Zmovement' or similar. From the Input commands menu, attach a tile that reads 'acceleration (mg) [x]' and set it to 'acceleration (mg) [z]'.
![BBC micro:bit ](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-23300-287773/Alarm+1.png)

  * Now, drag in and attach an 'if/do' tile, to tell the device to react to changes in the Z value of the accelerometer.
  * For 'if', connect an 'or' tile from the Logic commands menu, to tell the device to react under one of two circumstances.
  * Using two [0] < [0]' tiles and your Zmovement variable, create a line of code that reads 'if [Zmovement] < [-1,100] or [Zmovement] > [-900]'
  * This tells your device to react if it is moved along the Z axis. If the device is stationary and facing LED-upwards from a flat surface, this means it should now react if anybody attempts to pick it up from above.
  * For 'do', attach a 'show string' tile from the basic commands menu, and enter an appropriate warning, such as 'Hands off my micro:bit!'
![BBC micro:bit ](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-23300-287991/Alarm+2.png)

  * Now, create two duplicates of your 'set [Zmovement] to accelleration (mg) [z]' string, and create two new variables for detecting movement along the X and Y axis'. Place these in your Forever loop, above the 'if/do' string, like so:
![BBC micro:bit ](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-23300-287992/Alarm+3.png)

  * Create two duplicates your 'if/do' string, and set these to Xmovement and Ymovement respectively. Set the numerical parameters to < [-100] and > [100], and recreate your 'show string' warning message under 'do' for each.
  * This means your device will now trigger the warning message if it is picked up, or if it is moved along the X and Y axis' on the accelerometer. Your full block of code should look something like this:
![BBC micro:bit ](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-23300-287993/Alarm+4.png)

  * Finally, we need to add the buzzer element. We'll be attaching the 3V buzzer to one of the BBC micro:bit's pins - for the purposes of this walkthrough, let's use pin 0.
  * Go to the Pins command menu and find the tile that reads 'digital write (0,1) [1] to pin [P0]'.
  * This tile tells the pin to either switch the pin on, or off. When the digital write is set to 0, the pin is switched off. When it is set to 1, the pin is switched on at 3V.
  * Set the digital write to [1], and keep the pin set to [P0].
  * We don't want the buzzer to go off constantly when activated, so now set a pause of 3000ms (3 seconds) underneath.
  * Now, add a second 'digital write...' tile, and this time set it to 0, meaning the pin will switch off three seconds after activating.
  * Create two identical duplicates of this set of tiles, and place one within each of your three 'if/do' tiles.
  * Your final block of code should look like this:
![BBC micro:bit ](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-23300-287995/Alarm+6.png)

  * Click compile to download your code, and transfer it to your BBC micro:bit device.
  * Attach one end of your first crocodile clip to the GND pad at the edge of the BBC micro:bit, and the other end to the black wire on your buzzer.
  * Attach one end of your second crocodile clip to the '0' pad on the BBC micro:bit, and the other end to the red wire on your buzzer.
  * Now either run your code or pick up your BBC micro:bit to test the functionality of your new security alarm!

_Once your students have mastered this project, what else can they learn how to do with the pin functionality? Experiment with attaching different devices, or by using the BBC micro:bit's other pins to program a wider range of responses to external stimuli. Let us know what you and your pupils come up with in the comments section below..._
