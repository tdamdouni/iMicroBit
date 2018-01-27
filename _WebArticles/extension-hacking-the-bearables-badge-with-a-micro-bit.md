# Extension: Hacking the Bearables badge with a micro:bit

_Captured: 2017-11-20 at 15:15 from [lorrainbow.wordpress.com](https://lorrainbow.wordpress.com/2017/11/19/extension-hacking-the-bearables-badge-with-a-microbit/)_

![](https://lorrainbow.files.wordpress.com/2017/11/20171119_220219.jpg?w=1640&h=624&crop=1)

After my husband successfully hacked the [Pimoroni](https://shop.pimoroni.com/) Bearables badge with a Raspberry Pi: <https://lorrainbow.wordpress.com/2017/11/18/guest-blogger-phil-underwood-hacking-the-bareables-badge/> I decided to have a go and try it with the micro:bit

I'm in no way an electronics whizz like him but the words i2c and CLK sounded familiar! Turns out the micro:bit does have an i2c bus!

## How to hack the badge with a micro:bit

  1. Follow the instructions on the previous post to solder 3 wires to the middle 3 pads on the back of the Bearable
  2. Using the Edge Connector for the micro:bit 
    1. Connect the 2nd pad (ICSPDAT) to Pin 20 on the micro:bit
    2. Connect the 3rd pad (ICSPCLK) to Pin 19 on the micro:bit
    3. Connect the 4th pad to 0V (Ground) on the micro:bit
  3. On my edge connector pins 19 and 20 are just holes in the board. So I connected the wires using the male end of a jumper wire. For more stability I'd recommend soldering pins onto Pins 19 and 20 and connecting a female header on.
  4. Put a battery in the badge and get it going
  5. Using the Mu editor check to see if the badge is connected. 
    1. In Mu press Repl to see the output
    2. I used this code from here: <https://microbit-playground.co.uk/howto/scan-i2c-bus> to scan for a new device
    3. If the badge is connected you should see 
      1. 0x0e - the magnetometer
      2. 0x1d - the accelerometer and
      3. 0x15 - the badge!
  6. To put the badge in hacking mode the code is: 
    * i2c.write(0x15, bytes([0,17]))
  7. Then to turn on a single pink light: 
    * i2c.write(0x15,bytes([1,7]))
  8. To go back to normal badge mode: 
    * i2c.write(0x15,bytes([0,16]))

More information on what these codes mean can be found in the previous post.

Happy Hacking!
