# BBC micro:bit Pedestrian Crossing Project

_Captured: 2017-09-10 at 18:53 from [www.kitronik.co.uk](https://www.kitronik.co.uk/blog/bbc-microbit-pedestrian-crossing-project)_

This Pedestrian Crossing project was submitted to us by Thomas Stratford. Thomas started this project to try out the pre-written code that came with the [IET Pedestrian Crossing resource](http://faraday.theiet.org/resources/overview/product-prototype.cfm). The aim is to use the BBC micro:bit to develop a prototype for a pedestrian crossing for a local secondary school.

Thomas Stratford is an ICT Technician for the [Misbourne School](http://www.misbourne.bucks.sch.uk/). When he isn't fixing IT problems, he spends his time making, tinkering and building Electronics projects. He is currently learning about the recently released BBC micro:bit.

### BBC micro:bit Pedestrian Crossing Project:

In order to create this project in the same way as the example below, you will need to source the following components:

**Parts List:**

**Note:** With the exception of the 5 x 220Ω resistors, all of the parts used used in this Project can be found in the[ Kitronik Inventors Kit](https://www.kitronik.co.uk/5603-inventors-kit-for-the-bbc-microbit.html). If you have the Inventors Kit you can substitute the 220Ω resistors for the 47Ω resistors that come with the Kit.

### Stage 1 - The Traffic Lights:

First, I connected three LED's to P0, P1 & P2 via series resistors as show in the picture below.

**Stage 1 Suggested Breadboard Layout:**

![BBC micro:bit Pedestrian Crossing Project -edge-connector-lights-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/06/pedestrian-crossing-edge-connector-lights-870.jpg)

BBC micro:bit Edge Connector Breakout Board Breadboard Connection

P0 pin
Red Traffic LED via 220Ω Resistor.

P1 pin
Orange Traffic LED via 220Ω Resistor.

P2 pin
Green Traffic LED via 220Ω Resistor.

0V Pin
Breadboard negative rail.

3V Pin
Breadboard positive rail.

**Stage 1 Completed Example:**

![BBC micro:bit Pedestrian Crossing Project -lights-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/06/pedestrian-crossing-prototyping-board-lights-870.jpg)

### Stage 2 - Adding Pedestrian Crossing LEDS:

This worked well so I thought I would try adding two more LED's via series resistors to ports (P8 & P12). I modified the pre-written program so that the two additional LED's would also be controlled.

**Stage 2 Suggested Breadboard Layout:**

![BBC micro:bit Pedestrian Crossing Project -connector-pedestrian-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/06/pedestrian-crossing-edge-connector-pedestrian-870.jpg)

BBC micro:bit Edge Connector Breakout Board Breadboard Connection

P0 pin
Red Traffic LED via 220Ω Resistor.

P1 pin
Orange Traffic LED via 220Ω Resistor.

P2 pin
Green Traffic LED via 220Ω Resistor.

P8 pin
Green Pedestrian LED via 220Ω Resistor.

P12 pin
Red Pedestrian LED via 220Ω Resistor.

0V Pin
Breadboard negative rail.

3V Pin
Breadboard positive rail.

**Stage 2 Completed Example:**

![BBC micro:bit Pedestrian Crossing Project -prototyping-board-no-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/06/pedestrian-crossing-prototyping-board-no-870.jpg)

## Stage 3 - Adding The Crossing Beeper:

The final part of this project was to add a piezo sounder to simulate the crossing beeper. I connected a piezo sounder to port (P16) via a driver transistor. I modified the code once more to add this functionality.

**Stage 3 Suggested Breadboard Layout:**

![BBC micro:bit Pedestrian Crossing Project -edge-connector-all-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/06/pedestrian-crossing-edge-connector-all-870.jpg)

BBC micro:bit Edge Connector Breakout Board Breadboard Connection

P0 pin
Red Traffic LED via 220Ω Resistor.

P1 pin
Orange Traffic LED via 220Ω Resistor.

P2 pin
Green Traffic LED via 220Ω Resistor.

P8 pin
Green Pedestrian LED via 220Ω Resistor.

P12 pin
Red Pedestrian LED via 220Ω Resistor.

P16 pin
2.2kΩ Resistor for Transistor.

0V Pin
Breadboard negative rail.

3V Pin
Breadboard positive rail.

**Stage 3 Completed Example:**

![BBC micro:bit Pedestrian Crossing Project -complete-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/06/pedestrian-crossing-prototyping-board-complete-870.jpg)

**Note:** The Breadboard layout shows a buzzer with leads but the completed example shows a buzzer that fits directly to the breadboard, therefore the wire link or jumper wire is connected differently. It would be better to follow the breadboard image layout as this is easier to follow.

**Code:**

The code has been written in Microsoft Touch Develop and can be found [here](https://www.microbit.co.uk/rlgqypuvdb).

We would like to thank Thomas for sharing his excellent project with us. For up to the minute accounts of Thomas' projects, follow him on Twitter: [@MrTomsWorld](https://twitter.com/MrTomsWorld)

(C)Kitronik Ltd - You may print this page & link to it, but must not copy the page or part thereof without Kitronik's prior written consent.

![Same Day Dispatch](https://www.kitronik.co.uk/img/banners/same_day_dispatch.png)

> _<- Previous Post Next Post ->_
