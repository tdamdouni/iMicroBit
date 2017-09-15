# Bit:Bot – The Integrated Robot for BBC Micro:Bit

_Captured: 2017-09-04 at 19:20 from [4tronix.co.uk](http://4tronix.co.uk/blog/?p=1490)_

![bb01](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/bb01-300x225.jpg)

A great way to engage young and old kids alike with the BBC micro:bit and all the languages available. Both block-based and text-based languages can support the Bit:Bot

You can also use the Radio or Bluetooth functionality of the Micro:Bit to send and receive commands and date. See a [Bluetooth tutorial here](https://ukbaz.github.io/howto/bitbotRemoteControl.html)

***NEW*** There is now a Microsoft PXT package for Bit:Bot (thanks to Sten Roger Sandvik, @stenrs on Twitter). Go to the Advanced tab or the Tools gear icon and select Add Package, then search for BitBot.

**Warning**: The line follower sensors share the same pins as the buttons. Depending what language you are using, when the Micro:Bit is started or reset it will check the 2 buttons and start pairing if they are both pressed. With the Bit:Bot, this translates to both line follower sensors getting reflections. You can stop it happening by lifting it off the surface before switching on.

## Features

The Bit:Bot gives you all these features:

  * 2 micro-metal gear motors. Both fully controllable in software, for both speed (0 to 100%) and direction (forward or reverse)
  * Wheels with rubber tyres for maximum grip
  * Really smooth metal ball front caster
  * 12 mini neopixels in 2 sets of 6 along the arms either side. Select any colour for any pixel, produce stunning lighting effects as your Bit:Bot moves around
  * 2 digital line following sensors. Code your own line-following robots and race them to see whose code produces the fastest lap time!
  * 2 analog light sensors (front left and front right) so your Bit:Bot can be programmed to follow a light source such as a torch, or you could code it to go and hide in the darkest place it can find
  * Buzzer, so you can make beeping sounds whenever you want
  * Powered from integrated 3xAA battery holder with on/off switch and blue indicator LED
  * Easily plug your BBC micro:bit in and out using the edge connector
  * Extension port for additional neopixels (such as [McRoboFace](http://4tronix.co.uk/store/index.php?rt=product/product&product_id=563))
  * Expansion connections at the front for additional sensors (in development)

## Assembling

### Step 0 - Check you have all the correct parts:

  * 1 caster assembly (either metal ball or plastic ball)
  * 2 x 6mm M2 pan head screws
  * 2 x M2 nuts
  * 2 x 12mm brass pillars
  * 4 x 8mm M2.5 countersunk screws
  1. Use the M2 6mm (panhead) screws and nuts to attach the front caster housing, then push the caster ball into the housing
  2. Use the M2.5 6mm panhead and 8mm countersunk screws to fit the battery pack onto the 2 metal pillars: **ENSURE the on/off switch is at the rear of the Bit:Bot**
  3. Push the wheels on with the smooth side outwards. The axle should come flush with the outside of the wheel and not protrude (or the inside can catch on the motor housing)
  4. Push your BBC micro:bit into the edge connector with the LEDs and switches on the top

Click on any image to enlarge

### Step 1 - Fit the Front Caster

![Step1](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step1-300x225.jpg)

> _This simply prints every 3 seconds the distance measured by the sensor_

![Step2](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step2-300x225.jpg)

![Step3](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step3-300x225.jpg)

> _You could replace the item "Purple" with the red/green/blue block shown underneath if you want_

![Step4](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step4-300x225.jpg)

![Step5](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step5-300x225.jpg)

### Step 2 - Fit the Battery Holder

At this point you should have 4 screws left. Either 4 x 8mm countersink, or 2 x 6mm panhead and 2 x 8mm countersink.

If you have the 6mm panhead screws, use these to fit the 12mm brass pillars to the Bit:Bot main PCB.

Always use 8mm countersink screws to fit the battery holder to the brass pillars.

![Step6](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step6-300x225.jpg)

Use either 6mm panhead or 8mm countersink to fit the 12mm brass pillars to the main board (above)

![Step7](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step7-300x235.jpg)

> _To move the motor at full speed in reverse, we change which pin is 0 (Low) and 1 (High)_

Use the 8mm countersink screws to fit the battery holder to the brass pillars.

### Step 3 - Fit the Wheels

![Step8](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step8-300x225.jpg)

> _Push the wheels on, so that the axle is flush with the outside of the wheel_

### Step 4 - Attach your BBC micro:bit

![Step9](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/Step9-300x225.jpg)

## Know Your Bit:Bot

### Above

![bb17a](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/bb17a-300x225.jpg)

This shows the neopixels (6 on each arm), the 2 light sensors, on/off switch and indicator LED

The buzzer is below the on/off switch and the edge-connector is below the front of the battery holder

### Below

![bb15a](http://4tronix.co.uk/blog/wp-content/uploads/2016/12/bb15a-300x225.jpg)

Now you can see the 2 line sensors and the port for neopixel extensions and general purpose expansion connector. Connection labelling is on the underside

## Programming

I find [Microsoft PXT ](https://pxt.microbit.org/?lang=en)the best block based language for Bit:Bot as it happily works with the extended pin set used and supports neopixels easily also.

*NEW* There is now a Microsoft PXT package for Bit:Bot (thanks to Sten Roger Sandvik, @stenrs on Twitter). Go to the Advanced tab or the Tools gear icon and select Add Package, then search for BitBot.

For text-based programming there is micro-python, and I prefer to use this offline using the Mu editor. It provides a very neat and easy way of interfacing to the micro:bit without all the fuss of dragging and dropping. **NOTE:** At the time of writing (December 2016), there are problems with Mu when using PWM with neopixels and other things, so it best to use the online micropython editor for now.

The following examples use both of these languages to show code fragments.

Note on examples: We want to show people how the various features can be used. We don't want to do the coding for you - that is the learning experience you should be taking away from using it. In the following examples, we will give you the tools to use all the features of Bit:Bot but it is up to you to combine them together in your code to make it do something useful. We do give a complete example of line-following - but it is a very basic algorithm and will get confused at T-junctions and crossings; and it doesn't use the neopixels.

Download Python examples at the bottom of this page.

Some great tutorials/examples by [Mark Atkinson here](http://multiwingspan.co.uk/micro.php?page=bitbot)

### Motors

Each motor has two pins connected to it. One determines the speed and the other the direction:

Left motor: Speed Pin 0, Direction, Pin 8

Right motor: Speed Pin 1, Direction Pin 12

The simplest way to make the motors move is to set the Speed pin to HIGH and the Direction pin to LOW (to move full speed forwards)

#### In Python, move left motor Forwards:

pin0.write_digital(1)  
pin8.write_digital(0)

#### In PXT, move left motor Forwards:

NB. You can find the output pin commands in the "advanced" tab, under "pins"

#### In Python, move left motor Reverse:

pin0.write_digital(0)  
pin8.write_digital(1)

#### In PXT, move left motor Reverse:

If we want to change the speed of a motor, so that it is not going at full speed all the time, we need to use PWM (Pulse Width Modulation). This is means of changing the amount of power given to the motor by switching it on and off very fast. The percentage value of PWM determines the amount of each cycle that the output is ON. So a percentage of 100% is the same as being on all the time and thus the same as the examples above. A percentage of 50% would mean that the motor is only energised half the time, so it will go much slower. Note that the actual speed of the motor is not the same as the percentage of PWM - the motor won't turn at all if the PWM value is too low and you will also get some stuttering at certain values. Nevertheless, being able to change the speed makes for a much better robot. For example, you can make a line follower that smoothly follows the line, rather than the normal shaking left and right.

To change the PWM value of a pin, we must use the analog_write commands. These can be set to a value between 0 (always off) to 1023 (always on), so 50% would be 511. Here are the commands to change the speed of the Right motor to approx 75% (value is 770)

#### In Python, move right motor forwards at 75%

pin1.write_analog(770)  
pin12.write_digital(0)

#### In PXT, move right motor forwards at 75%

Doing this for the motors moving in reverse is a little confusing. Remember we need to change the direction pin to 1 for reverse. Then we need to set the amount of time in each cycle that the speed pin is LOW. This is the opposite of moving forwards, where we set the time for it to be High. Se we simply take the number (770 in this case) away from 1023, giving 253.

#### In Python, move right motor Reverse at 75%

pin1.write_analog(253)  
pin12.write_digital(1)

#### In PXT, move right motor reverse at 75%

### Neopixels

In fact, the name "neopixel" is a termed coined by Adafruit, but like "hoover" was a name of a brand of vacuum cleaner and is now a general term for all similar products, whoever makes it. The generic term is "smart RGB pixel" and is usually referenced with the name of the chip WS2812B. However, there are many different chips, all performing in a compatible way. The ones on the Bit:Bot are actually SK6812-3535

These smart RGB pixels are able to display any of 16 million colours by selecting a value of 0 to 255 for each of the Red, Green and Blue LEDs on each chip. The whole thing is controlled by a single pin on the BBC micro:bit (pin 13 for Bit:Bot). It is simple to use the included neopixel libraries to control each pixel individually.

The pixels are labelled on the Bit:Bot. From 0 to 5 on the left arm and from 6 to 11 on the right arm. If you connect any more neopixels into the extension port, then the new ones will start at 12.

#### In Python, set neopixel 2 to purple (red and blue)

import neopixel  
np = neopixel.NeoPixel(pin13, 12)  
np[2] = (40, 0, 40)  
np.show( )

The first line imports the neopixel library. We only need to do this once, at the very top of your Python programThe second line creates an Python list with an element for each pixel. As shown, it specifies 12 pixels connected to pin 13. If you added more neopixels then you would increase the number from 12 by the number of pixels you added. eg. if you added a McRoboFace, then the total would be 12 + 17 = 29 so you would change the line to: np = neopixel.NeoPixel(pin13, 29)  
The third line sets the pixel we have selected (number 2 in this case) to the colour which is set by three values in the brackets, each value can be from 0 to 255 and covers Red, Green and Blue. In our example we have set Red and Blue to 40.  
The fourth line tells the neopixel library to copy all the data to the neopixels, from the Python list that we have been working with. It is only at this point that the LEDs change. In general, you would make all the changes you want and only at the end would you use a np.show( )

#### In PXT, set neopixel 2 to purple

Just like in Python, we need to add the neopixel library. Do this from the menu. Select add package and then select neopixels

### Line Follower Sensors

These are digital inputs and connected to Pin 11 (left) and Pin 5 (right). These are the same pins as used by the buttons, so pressing a button will have the same effect as detecting a black line. This may have unexpected side-effects - as switching the micro:bit on when both buttons are pressed can cause it to enter Bluetooth pairing mode (depending what software is installed).

So you can use the normal Button inputs to read the sensors if you want, or you can use digital_read commands (as shown below). If the left sensor detects a line, it means the Bit:Bot is too far to the right, so it should move left. The opposite is the case if the right sensor detects a line. Here is some simple code for line following in Python (the actual motor commands are in separate functions for clarity)

while True:  
lline = pin11.read_digital()  
rline = pin5.read_digital()  
if (lline == 1):  
spinLeft( )  
elif (rline == 1):  
spinRight( )  
else:  
forward(speed)

In PXT, this looks more complicated than the Python, as all the code is inline. You may need to add pauses during the loop depending on your line following track

### Light Sensors

These are analog sensors and will give a value of 0 to 1023, where 0 is fully dark and 1023 is maximum brightness. As there are only 3 analog pins available on the micro:bit (without affecting the LED displays) and we are using 2 of them to control the motors, we only have one left (Pin 2) to read the analog values from 2 line sensors. How can we do this? Well, the Bit:Bot has an analog switch that uses a digital output signal (pin 16) to determine whether the analog input we are reading is for the left sensor or the right sensor.

Therefore, to read the light sensors we need to set the selection output pin first, then read the analog data.

I**n Python**, we can do it like this to read the values into 2 variables called leftVal and rightVal:

Pin16.write_digital(0) # select left sensor  
leftVal = Pin2.read_analog()  
Pin16.write_digital(1) # select right sensor  
rightVal = Pin2.read_analog()

**In PXT**, we can do it a very similar way:

### Buzzer

The buzzer is a very simply device that outputs a 2.4kHz sound when it is set to ON. It is NOT controlled by the tone signal that can be output by the micro:bit on Pin 0 so you don't need to install any libraries to operate it.

It is connected to Pin14. Setting this to ON (1) will activate the buzzer and setting to OFF (0) will deactivate it.

In Python, a very simple and annoying beep, beep, beep sound can be made as follows:

while True:  
pin14.write_digital(1)  
sleep(400)  
pin14.write_digital(0)  
sleep(400)

An equally annoying sound can be made in PXT:

### Ultrasonic Distance Sensor

This optional HC-SR04 ultrasonic distance sensor addon can be used most easily in Microsoft PXT. In MicroPython we are hampered by the lack of a microsecond resolution timer. (but see the demo "Ultrasonic Obstacle Avoider" below)

Within PXT you need to add the package 'Sonar'. You can do this from the Advanced tab (at the bottom) or using the Tool menu (top right cog gear icon)

Both the Ping and the Echo are on the same pin (Pin 15). So you can make a block like this:

![](data:image/png;base64,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)

##  Example Micropython Programs
