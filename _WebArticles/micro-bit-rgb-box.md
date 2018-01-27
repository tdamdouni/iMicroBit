# micro:bit RGB box

_Captured: 2017-11-12 at 12:11 from [lorrainbow.wordpress.com](https://lorrainbow.wordpress.com/2017/11/11/microbit-rgb-box/)_

![](https://lorrainbow.files.wordpress.com/2017/11/20171111_212313.jpg?w=1640&h=624&crop=1)

Last Christmas I taught my son's school algorithms by getting them to write an algorithm for some Christmas lights.

The younger children had to colour in 3 boxes with 3 different colours. The older ones had to write down the time delays. The eldest group had a look at RGB values and loops.

When a child asked me what does 255, 100, 100 look like in lights I quickly coded it on the micro:bit and turned on the strip of lights. The problem was once one child saw their light all the others wanted to see theirs! It just took forever to have to keep changing the numbers and upload the code to the micro:bit. (In hindsight if I had used python and the MU editor this would have been a lot quicker)

To combat the problem I've made an RGB box! A very simple box with 3 buttons - Red, Green, Blue. As you press each button it increases that colour in the strip of lights. It's a great way to demonstrate how RGB works in lights.

# Equipment

  * 3 buttons (I used these arcade buttons from Pimoroni: <https://shop.pimoroni.com/products/colourful-arcade-buttons>)
  * 2.8mm female spade terminals to connect wire to those buttons: <http://www.ebay.co.uk/itm/Insulated-Female-Spade-Terminals-Crimp-Connector-Electrical-Terminal-Wiring-Wire-/132076481575>
  * A strip of lights (I used a 1 metre strip of 30 WS2812B RGB from e-bay: <http://www.ebay.co.uk/itm/WS2812B-5050-RGB-D-Fxib-Strip-1M-30-60-144-D-Individual-Addressab-5V-AG-/291973865378>
  * 2 X AAA batteries and battery holder for the micro:bit
  * 2 x AAA batteries and a battery holder for the lights (I used this one from CPC as the wires are ready and it has a switch on it, and it's cheap: <http://cpc.farnell.com/pro-power/sbh-421-1as/battery-holder-2xaaa-encl-leads/dp/BT06089>)
  * Female to female jumper wires
  * micro:bit
  * micro:bit edge connector

# Build

We need to connect wire to 4 pins to connect 3 buttons and the light strip. Therefore I used the Edge Connector to access more pins on the micro:bit.

I used jumper wires and chopped their heads off to connect from the edge connector to the buttons and the light strip.

## Connect the lights to the edge connector

  1. Connect a female to female jumper wire to GND
  2. Chop off the other half of the wire
  3. Strip the wire to expose the wire underneath
  4. Connect it to the ground of the lights using a terminal block
  5. Connect a female to female jumper wore to Pin 1
  6. Chop off the other half of the wire
  7. Strip the wire to expose the wire underneath
  8. Connect it to the data wire of the lights using a terminal block
  9. ![20171111_221731.jpg](https://lorrainbow.files.wordpress.com/2017/11/20171111_221731-e1510439177307.jpg?w=1240)

> _The ground and data wires of the lights connected to jumper wires_

## Connect the buttons

  1. Cut a female to female jumper wire in half
  2. Strip the one half of the wire to expose the wire underneath
  3. Crimp a spade terminal onto the exposed wire
  4. Connect the jumper wire to GND on the edge board
  5. Connect the other wire to Pin 0 on the edge board
  6. Do the same for the other two buttons connecting red to Pin 3 and GND then connect blue to Pin 2 and GND ![A wire chopped & stripped](https://lorrainbow.files.wordpress.com/2017/11/20171111_194122.jpg?w=220&h=294)

![Crimped](https://lorrainbow.files.wordpress.com/2017/11/20171111_201740.jpg?w=392&h=294)

  7. Cut holes in your box and place the buttons in
  8. Connect the wires to the buttons - each button has a data wire and a ground wire. ![20171111_202351.jpg](https://lorrainbow.files.wordpress.com/2017/11/20171111_202351.jpg?w=4032)

  1. On the opposite side of the strip of lights connect the battery. 
    1. Connect the black ground wire from the battery to the white ground wire of the lights.
    2. Connect the red live wire from the battery cage to the red live wire of the lights

On your edge board you should have wires connected to all the 4 grounds, Pins 0, 1, 2 and 3

# Code

  1. Go to <https://makecode.microbit.org/>
  2. Under on start: 
    1. Select Advanced > Add Package and select Neopixel to add the Neopixel menu
    2. Set the variable item to 30 lights on Pin 1
    3. Set the lights on Pin 0, 2 and 3 to pull up (this block is under Advanced > Pins > More)
    4. Create Variables R, G and B and set them to 0![setup1](https://lorrainbow.files.wordpress.com/2017/11/setup1.png)

    5. Create a function called changeColour. This is called anytime a button or buttons are pressed. It sets the lights to the colour of the variables R, G and B. 
      1. Set item to the RGB variables R, G and B![changeColour](https://lorrainbow.files.wordpress.com/2017/11/changecolour.png)

> _Under forever we're going to check for button presses._

    1. Add the logic blocks 
      1. if
      2. 0 = 0
      3. and
    2. If digital read pin 3 (red) and digital read pin 0 (green) both = 0 that means they pressed the red and green buttons together. (Digital read pin is found under Advanced > Pins) 
      1. Set variables R, G and B to 0 - turn the lights off
      2. Call the function changeColour
    3. If digital read pin 3 = 0 they pressed red
    4. If digital read pin 0 = 0 they pressed green
    5. If digital read pin 0 = 0 they pressed blue
    6. For each check change that variable (R,G or B by 1) and call the function changeColour. ![forever](https://lorrainbow.files.wordpress.com/2017/11/forever.png)

## Finish

  1. Press Download to download the code to your computer
  2. Drag and drop that file onto your micro:bit
  3. Plug the micro:bit into the edge connector
  4. Put batteries in the battery cages
  5. Turn the lights battery cage on
  6. Press some buttons!

## Troubleshooting

  * My lights aren't coming on 
    * Is your battery box on? It has a switch!
    * Put some code under On Button A to test the lights separate to the buttons
    * You must power the lights separately to the micro:bit. The micro:bit can only power 8 lights. The power source needs to have a similar voltage to 2xAAA batteries.
    * You must ground the lights to the micro:bit
  * My buttons aren't working 
    * Check all the spade connections
    * Each button has 2 connections - data and ground. Check both are connected on both ends - that's 4 checks on 3 butttons!
    * Make sure you've pulled the pins up on start
    * Make sure you're checking for 0 (not 1) in the code
  * When I press red the lights on the micro:bit go weird? 
    * Pin 3 controls some lights on the micro:bit. When you use that pin some lights on the micro:bit will turn on. Don't worry - it's not an error
  * Blue isn't working but red is 
    * Change your light batteries. Blue is the first colour to go when batteries start to fade
