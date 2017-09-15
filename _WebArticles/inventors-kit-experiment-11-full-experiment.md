# Inventors Kit Experiment 11 Full Experiment

_Captured: 2017-09-10 at 18:49 from [www.kitronik.co.uk](https://www.kitronik.co.uk/blog/inventors-kit-experiment-11)_

In this tutorial you will find Experiment 11 Making a Pedestrian Crossing for the [Kitronik Inventors Kit](https://www.kitronik.co.uk/5603-inventors-kit-for-the-bbc-microbit.html) for the [BBC micro:bit](https://www.kitronik.co.uk/5613-bbc-microbit-board-only.html). This is an additional experiment to the ten that were included with the Inventors Kit, and has been created for you to get more from your kit. You will learn how to build the circuit and how to code the BBC microbit to control the circuit.

![Inventors Kit  for the bbc micro:bit Experiment 11-main-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/11/experiment-11-pedestrian-crossing-main-870.jpg)

You can complete this experiment with or without the Inventors Kit. If you do not have the Kitronik Inventors Kit you will have to source all of the required components separately, a full list of the things you will need can be found below. We also advise the use of a breadboard as trying to complete this experiment with crocodile leads would be more than a little challenging.

### This Experiment Requires:

### **The Aims Of This Experiment Are:**

  * To use six output pins to drive five LEDs and a buzzer.
  * To use the 'repeat' loop.
  * To use the 'play tone' block.
  * To learn how to setup initial LED states(outside of the main function loop).

### Experiment 11 Video Walk Through:

## Experiment 11 Making a Pedestrian Crossing:

Using Block commands it is possible to control up to six outputs. This experiment will use all six to create a traffic light and pedestrian crossing demonstration. Five of the outputs will be used to drive LEDs, three of which will be used for the traffic light and two will be used for the stop and go indicators on the pedestrian crossing. The remaining output will be used to drive the piezo buzzer.

This will all be controlled by a relatively simple sequence of Block commands.

### The Microsoft PXT Editor For The BBC micro:bit:

This experiment is created using the Microsoft PXT Editor.

The Microsoft PXT Editor is a drag and drop visual editor that provides a simple introduction to programming. Blocks snap together to build pr ograms and are grouped by the type of function they do. When a group is selected the commands in that group are shown and can be selected.

### Create The Following Code:

![experiment-11-pedestrian-crossing-code-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/06/experiment-11-pedestrian-crossing-code-870.jpg)

![experiment-2-block-editor-3-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/06/experiment-2-block-editor-3-870.jpg)

If you're having difficulty producing your own code for this experiment, we've created the code for you that you can compile, download and place onto your [BBC micro:bit](https://www.microbit.co.uk/). You will find the links for the code towards the end of this article.

### **Building This Circuit On The Prototyping System:**

It is possible to build this circuit using the [Prototyping System](https://www.kitronik.co.uk/5609-prototyping-system-for-the-bbc-microbit.html) for the BBC micro:bit and the components listed at the top of the page. Once you have sourced the required parts you can follow the diagram below.

![Inventors Kit  for the bbc microbit Experiment 11 -prototyping-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/11/experiment-11-pedestrian-crossing-prototyping-870.jpg)

### What Will Happen?:

First of all the traffic light LEDs default to 'green' and the pedestrian crossing LEDs default to 'red'. When button A is pressed on the BBC microbit the traffic light LEDs go from 'green' to 'amber' to 'red'. The pedestrian LEDs then change from 'red' to 'green' indicating that it is safe to cross, during which the buzzer beeps. After eight beeps the pedestrian LEDs change back to 'red' and the traffic lights go through the 'red' to 'red + amber' to 'green' sequence. This is now back at the original starting state.

### **Circuit Diagram: **

![Inventors Kit  for the bbc microbit Experiment 11 -diagram-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2016/11/experiment-11-pedestrian-crossing-diagram-870.jpg)

### What's Going On?:

The set 'digital write 1 to pin P12' and 'digital write 1 to pin P2' are used to set the initial LED states, which turn on the 'green' traffic light LED and the 'red' pedestrian crossing LED. These Blocks just execute once when the BBC micro:bit is turned on.

The code then waits for button A to be pressed on the BBC micro:bit before executing the main loop of code. When button A is pressed the Blocks before the 'repeat' loop execute causing the traffic light LEDs go from 'green' to 'amber' to 'red'. The pedestrian LEDs then change from 'red' to 'green' indicating that it is safe for the pedestrian to cross. The 'pause' blocks give the delays between each step of the sequence.

**The LEDs are connected as follows:**

TRAFFIC LIGHTS. PEDESTRIAN CROSSING. BBC micro:bit PINS.

Red
P1

Amber
P8

Green
P12

Red
P2

Green
P16

When it is safe to cross and the 'green' pedestrian crossing LED is lit up and the buzzer then beeps eight times. This is controlled by the 'repeat' loop. In each loop a tone is played and then there is a pause after each tone.

After the beeps the next set of Blocks execute which change the pedestrian LEDs back to 'red' and causes the traffic lights go through the 'red' to 'red + amber' to 'green' sequence. This is now back at the original starting state and the code awaits another press of button A.

## Inventors Kit Experiment 11 Code Examples:

### Extension Tasks:

  * Can you alter the tone of the beeps and how many times they are repeated?
  * Try adding an image on the BBC micro:bit display when it is safe to cross the pedestrian crossing.

### Thank You!:

This experiment was inspired by work produced by Thomas Stratford who is an ICT Technician for the Misbourne School. When he isn't fixing IT problems, he spends his time making, tinkering and building Electronics projects. He is currently learning about the recently released BBC micro:bit.

For up to the minute accounts of Thomas' projects, follow him on Twitter:

Tom created his code using Touch Develop and more details can be found at:

<https://www.kitronik.co.uk/blog/bbc-microbit-pedestrian-crossing-project>

## Kitronik Inventors Kit Resources:

Exp No#. Experiment Name. Resource Type.

1
[Say Hello to the BBC micro:bit.](https://www.kitronik.co.uk/blog/inventors-kit-experiment-1-help)
Further Help.

2
[Using an LDR and analog inputs.](https://www.kitronik.co.uk/blog/experiment-2-using-an-ldr-analog-inputs/)
Full Experiment + Further Help.

3
[Dimming an LED using a potentiometer](https://www.kitronik.co.uk/blog/inventors-kit-experiment-3-further-help).
Further Help.

4
[Using a transistor to drive a motor.](https://www.kitronik.co.uk/blog/experiment-4-using-a-transistor-to-drive-a-motor/)
Full Experiment + Further Help.

5
[Using the accelerometer to control motor speed](https://www.kitronik.co.uk/blog/inventors-kit-experiment-5-further-help).
Further Help.

6
[Setting the tone with a piezo buzzer](https://www.kitronik.co.uk/blog/inventors-kit-experiment-6-help).
Further Help.

7
[Wind Power](https://www.kitronik.co.uk/blog/experiment-7-wind-power).
Full Experiment + Further Help.

8
[Making a game using the compass](https://www.kitronik.co.uk/blog/inventors-kit-experiment-8-further-help).
Further Help.

9
[Capacitor charge circuit](https://www.kitronik.co.uk/blog/inventors-kit-experiment-9-help).
Further Help.

10
[Using an RGB LED](https://www.kitronik.co.uk/blog/inventors-kit-experiment-10-help).
Further Help.

11
Making a pedestrian crossing.
Full Experiment + Further Help.

12
[Making a random dice](https://www.kitronik.co.uk/blog/inventors-kit-experiment-12).
Full Experiment + Further Help.

## Get The Kitronik Inventors Kit For The BBC microbit:

We do two versions of the Inventors Kit for the BBC micro:bit, with or without the BBC micro:bit included. Chose the option that is right for you from the links below.
