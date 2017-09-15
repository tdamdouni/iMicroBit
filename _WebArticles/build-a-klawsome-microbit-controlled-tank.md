# Build A Klawsome microbit Controlled Tank

_Captured: 2017-09-10 at 18:44 from [www.kitronik.co.uk](https://www.kitronik.co.uk/blog/klawsome-microbit-controlled-tank/)_

Kitronik Technical Director Dave Sanderson can often be found taking to twitter and [sharing](https://twitter.com/SolutionsByDave/status/862271295014264833) the goings on in the design and development office at Kitronik HQ. Whilst testing an upcoming product called the Klaw, he's [tweeted](https://twitter.com/SolutionsByDave/status/862332920765304835) progress a number of times and each time the response has been positive.

![tank-zumo-claw-fidget-spinner-microbit-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/tank-zumo-claw-fidget-spinner-microbit-1000.jpg)

> _The tweeting has prompted a good number of requests for a tutorial on how to make the tank and how to control it. Dave did a new build and recorded the process. There are also downloads for the DXF file and code that Dave produced. Over to you Dave..._

## Build A Klawsome microbit Controlled Tank:

Although our Klaw hasn't yet been released you can still build the tank minus the Klaw and add it as and when it becomes available (as and when = it's almost here). You'll still have a totally awesome tank that can be controlled with a mobile or tablet.

## You Will Need:

  * 1 x Klaw (Released soon).
  * A computer and an internet connection.

## Howto Build:

First I needed to laser cut the tank chassis. I added 4 holes to the DXF ([Download the DXF here](https://www.kitronik.co.uk/zip/tank-cutting-template-klaw-microbit.zip).) to mount the motor driver board, and a couple to allow the KLAW to bolt on.

### Amending The Design:

![cad-design-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/cad-design-1000.jpg)

> _Cutting it out on the laser cutter:_

![laser-cutting-top-plates-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/laser-cutting-top-plates-870.jpg)

> _Once the parts were cut it was a case of following the tank building resource instructions from here._

### Mechanical Assembly:

Starting with the bag of bits:

![tank-parts-pre-build-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/tank-parts-pre-build-870.jpg)

> _I retrieved all of the track parts from the bag of bits and assembled the tracks._

![tank-tracks-pre-build-200](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/tank-tracks-pre-build-1000.jpg)

![assembling-tank-tracks-200](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/assembling-tank-tracks-1000.jpg)

![assembled-tracks-200](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/assembled-tracks-1000.jpg)

Once I'd assembled the tracks, I then built the chassis, still following the instructions [from here](https://www.kitronik.co.uk/pdf/2125_Buggy_teaching_notes_V1_4.pdf).

![tank-kit-undeside-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/tank-kit-undeside-870.jpg)

> _The Klaw has a premade set of mounting holes. I screwed it into the 2 additional holes I added to the bottom chassis plate._

![driver-wheels-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/driver-wheels-870.jpg)

![top-view-built-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/top-view-built-870.jpg)

![fixing-the-klaw-870](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/fixing-the-klaw-870.jpg)

### Wiring:

That's the basic mechanical build done, now onto the wiring.

![ready-for-top-plate-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/ready-for-top-plate-1000.jpg)

Note that the mechanical kit doesn't come with a battery box, which comes with the older motor driver that the tank was originally designed for. I used a [4xAA box](https://www.kitronik.co.uk/2222) instead.

![the-battery-box-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/the-battery-box-1000.jpg)

> _This box has an on off switch. I'm using the switch mounted on the Tank chassis, so I made sure this one was set to on before sticking the box down with double sided foam Pads._

![battery-box-sticky-pads-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/battery-box-sticky-pads-1000.jpg)

> _Each motor has a + marking on it, so I made sure the coloured wire was soldered to that terminal._

![motor-terminals-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/motor-terminals-1000.jpg)

> _I twisted the wires for neatness and routed them to the motor driver board._

![motor-driver-board-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/motor-driver-board-1000.jpg)

> _The Battery box is connected to the power input of the motor driver board, with the positive lead going via the switch that is mounted on the chassis._

I cut the servo plug on the Klaw servo off, so it could be wired into the motor driver board. You could also make it plug in using a [servo extension lead](https://www.kitronik.co.uk/4157) to wire to the motor driver board. The servo power and ground go to the power connection, and the signal (orange on this servo) goes to the P1 breakout terminal on the motor driver board.

Notice that I have the motors wires with the black leads in the middle (yellow, black, black, red). The "Yellow" motor is at the "Rear" of my tank, and the "Red" motor is at the "Front", where the Klaw is mounted. Because the motors are mounted on opposite sides of the tank to drive 'Forwards' on motor spins clockwise, and one anti-clockwise.

### Coding:

With the wiring in place its time to write some test code.

Kitronik has created some custom blocks for the microbit Javascript Block editor. These can be found in the Kitronik github. For the motor driver board, the address is:

<https://github.com/KitronikLtd/pxt-kitronik-motor-driver>

In the JavaScript Block editor click the 'Advanced' button in the toolbox, then click the 'Add Package' button and type in the github URL. Press the search magnifying glass and the package should appear:

![add-motor-driver-package-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/add-motor-driver-package-1000.jpg)

> _Simply click on it to add it to the project. You will now have access to the following blocks:_

![kitronik-motor-driver-blocks-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/kitronik-motor-driver-blocks-1000.jpg)

> _The tank will stand on its rear, which is handy for developing the test code, as it stops it driving away, and allows access to the microbit buttons._

![tank-testing-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/tank-testing-1000.jpg)

> _Create the following test code:_

![test-pxt-editor-code](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/test-pxt-editor-code.jpg)

> _This code will drive both tracks forward when button A is pressed, and stop them when button A and B are pressed. It also opens the Klaw when button B is pressed and closes it when button A and B are pressed._

Use this code to make sure that your tank is built correctly - for instance, I had to loosen the track slightly as it was too tight.

### Bluetooth:

![blutooth-control-code-1000](https://www.kitronik.co.uk/wp/wp-content/uploads/2017/05/blutooth-control-code-1000.jpg)

With a little code, it is possible to control the tank over Bluetooth using the [bitty software](http://www.bittysoftware.com/) gamepad on a mobile device, you will need to download the App:

  * [Get the Apps](http://www.bittysoftware.com/apps/bitty_controller.html).

You can download the gamepad tank control [code here](https://www.kitronik.co.uk/zip/tank-kit-microbit-bluetooth-hex-file.zip).

(C)Kitronik Ltd - You may print this page & link to it, but must not copy the page or part thereof without Kitronik's prior written consent.

![Robox 3D Printer](https://www.kitronik.co.uk/img/banners/robox_3d_printer.png)

> _<- Previous Post Next Post ->_
