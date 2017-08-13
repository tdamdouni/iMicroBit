# Excel and Micro:Bit - Hacking for fun and creativity!

_Captured: 2017-08-12 at 10:32 from [techcommunity.microsoft.com](https://techcommunity.microsoft.com/t5/Excel-Blog/Excel-and-Micro-Bit-Hacking-for-fun-and-creativity/ba-p/63603)_

Hello,

I'm Yigal, Principal Program Manager in the Excel team. I recently attended the BETT education conference in London. It was inspiring to see how many booths were dedicated to teaching computer programming, using learning aids such as micro controller, robots, and simplified coding environments. Kids of the future will get to learn at least some basic programming from a very early age!

I also got to discover an amazing little micro controller called [BBC Micro:Bit](http://microbit.org/). It's a small micro controller designed for education, packed with functionality and sensors. It's broadly available in the UK and expanding to other parts of the world, and kids in the UK use it to learn computing science. Really cute and cool educational tool!

This made me wonder. What is the role of Excel in this new world of connected devices, Internet of Things, and "makers" culture? If devices are everywhere, could we connect them to Excel and use the power of Excel to analyze data coming from these devices? Could we use Excel logic to control such devices?

And, specifically for the Micro:Bit, can we help kids learn better computer science, while also having some fun with this micro controller? Could we teach them a bit about the world of data analysis? I could easily imagine how doing something like that could encourage curiosity among the young generation and bring with it meaningful learnings in fun ways.

I decided to try it out for myself, and share my learnings with you, the Excel community!

**About the BBC Micro:Bit**  
So, what is this Micro:Bit?

It's a tiny little ARM based micro-controller board. For its' size and price, it has an impressive spec! It has a processor (of course!), several sensors including an accelerometer and a magnetometer, it can measure temperature and light using some "indirect" sensors, it can control external devices and read external inputs using three programmable I/O pins, and it has a 5x5 LED display for showing stuff, and two built in buttons for interactivity. It can also communicate with other computers using serial communications or over BLE (Bluetooth Low Energy). It can operate over battery or be powered using the built in USB port.

All this awesomeness is packed into a tiny low-cost form factor, which looks like this:

![The BBC Micro:Bit - Small Package, Big fun!](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/13764i720F65F585084212/image-size/medium?v=1.0&px=400)

> _The BBC Micro:Bit - Small Package, Big fun!_

If you want to play with it, and be able to follow the experiment I'm going to walk you thru in this blog post, you need to get one! The way to do that is either through the Micro:Bit [site](https://give.microbit.org/), through one of the authorized [resellers](http://microbit.org/resellers/), or just get one on [eBay](http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.Xbbc+micro+bit.TRS0&_nkw=bbc+micro+bit&_sacat=0).

Ready? Got one? Lets get going!

**The Experiment**  
For the purpose of this first entry-level experiment, lets agree that the goal would be to have some basic sensor data collected using the micro controller and then visualized in Excel.

To achieve that, we will go thru four steps:

  1. We will program the controller to collect some sensor data and send it over its' built in serial communication port.
  2. We will connect the Micro:Bit to the PC's serial port.
  3. We will write a small program in Excel that reads the data from the serial port into the grid.
  4. Visualize it, live! This is why we're here for… :-)
![The Experiment Flow - Data flows from Micro:Bit to Excel](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/13765i883EB36245B45F26/image-size/large?v=1.0&px=999)

> _The Experiment Flow - Data flows from Micro:Bit to Excel_

These are the basic building blocks and it's pretty simple to get started. You can do it as your fun weekend project!

Once you get going, the sky is the limit. You can expand to control the device, interact with other devices using the programmable pins, control the LEDs, respond to the buttons, etc. Just use your imagination and creativity, or get yourself inspired by this [list of Micro:Bit project ideas](http://microbit.org/ideas/)!

It's worth mentioning that while this blog focuses on the Micro:Bit, it's totally possible to envision doing the same with your favorite controller of choice. So, if you're a fan of Arduino, for example, feel free to adapt the experiment, and even better - share it back with this community!

**First thing's first: Programming the Micro:Bit**  
Programming the Micro:Bit is the easiest thing you'll ever do. Microsoft actually has a web-based development environment ready for you (Microsoft is one of the founding partners of the Micro:Bit).

All you have to do is, go to [www.makecode.com](http://www.makecode.com), select the Micro:Bit as your device, and write a little program using a visual "Block-based" programming language.

The program we'll write for this experiment will simply collect data from two sensors that we can easily play with - acceleration and light level, and send a sampling of the sensors over the serial communication port every 100ms.

It looks like this:

![The program that we'll run on the Micro:Bit](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/13766iFDD7F612BBF9EC83/image-size/large?v=1.0&px=999)

> _The program that we'll run on the Micro:Bit_

What ends up being written to the serial port are repeating lines of data in this format:

_ D:<light>,<acceleration>_

All you have to do now is load the program into your Micro:Bit. To do that, connect your Micro:Bit to the PC using a USB cable, which will make it appear like a removeable disk drive. Then download the HEX file from within the MakeCode environment and save it onto the device. A few seconds later, the program will start running.

To save you from having to re-type the program yourself, you can find a public copy of it [here](https://pxt.microbit.org/30666-98262-90183-87306).

**Connecting it to the PC**  
Now that we have our controller running and sending data, and before we try it out in Excel, it's a good idea to verify that the PC can indeed see the incoming data stream.  
To do that, you'll need to follow the instructions on [this page](https://www.microbit.co.uk/td/serial-library), which basically means you need to do two things:

  1. Install a driver, which will make the Micro:Bit "appear" as a serial port on your PC.
  2. Test it with a serial communication terminal emulator.

You will need to configure the right COM port. On my environment, it was configured to COM3. The sample code in Excel assumes that, so if yours is different, you'll need to modify the Excel code later on to reflect the right port.

Once you do that, you should see a stream of data that looks something like this inside your emulator:

Working? Time to move to the next step!

**Lets' Excel!**   
Now that we have a stream of incoming data, lets get it into Excel. The spreadsheet comprises of two parts - some VBA code that is used to communicate with the micro controller, and then some basic grid data manipulation functions which are used to break the data points and charts it. You can find a copy of the working spreadsheet **[attached to this blog**](https://techcommunity.microsoft.com/gxcuf89792/attachments/gxcuf89792/ExcelBlog/48.6/1/SensorVisualizer_BlogVersion.zip).

Assuming you want to build it yourself, or at least understand it fully, it's time to pull up your sleeves and write some VBA code that will read the data from the serial port, and push it into the grid.

Because this is an endless stream of data, for the purpose of this experiment, we will iterate thru the last 30 data samples collected. Of course, once you get the idea, you can change it to accumulate forever (or at least till the sheet fills up), push the data into a data model, etc. For now, we'll just iterate thru it, so whenever we reach the 30th row, we'll roll back to the first one.

One more point: When reading from the serial communication port in VBA, the most reliable way to do that is to read byte-by-byte and not whole lines. There's also some chance of losing some data (depending on speed of communications, speed of VBA execution, etc.), which is why I've added the "D:" prefix for each line. If the line we read doesn't start with it, the line gets ignored as garbage data.

With no further ado, here's a snippet from the main loop in the VBA code:

![The main communication read loop. You can find the code inside the attached workbook!](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/13769iE0B5271D5697938C/image-size/large?v=1.0&px=999)

> _A few things to note in this code snippet:_

  1. We open the COM3: port at 115,200 baud (the speed at which the Micro:Bit sends data).
  2. Reading happens a byte at a time, until end of line (char(13)) is detected.
  3. Whenever a line is read, it gets pushed into the grid into the next row in a fixed column. Row numbers are fixed between 2-31 to keep this example simpler.
  4. There is a flag used to stop reading. It's triggered by a stop button (from a different Macro).

The best way to understand this code it is to run it in debug mode and step thru it, so go ahead and download the demo workbook and experiment!

**Moving on to "real" Excel**  
Now that we have the data coming into the grid, we're in the plain old good Excel formula and charting territory. Time to do something with the data we are collecting!

To keep things generic, the VBA scripts reads the data as-is into the grid, so Column "E" contains the actual data, as it arrived over the wire. In our case, it's two numbers, comma-separated.

So, first thing we want to do is to break it up into two distinct values per row. The light level, and the acceleration value. I did that on purpose in the easy to read way - used the FIND formula to find the location of the "," separator inside the incoming data, and then used NUMERVALUE and LEFT and RIGHT formulas to break the string apart and convert it into two numeric values.

Here is a bit more about the formulas I used to break down the values from the input data string:

** =FIND(",",E2,1)** : Finds the location of the first comma separator inside cell E2 (which contains the raw incoming string of comma-separated values).  
**=NUMBERVALUE(LEFT(E2,F2-1))** : Takes the left side of the string, up to the comma location, and convert it to a number value. This gives us a number representing the light sensor value. Light values in the Micro:Bit range from 0 to 255.  
** =NUMBERVALUE(RIGHT(E2,LEN(E2)-F2))** : Similar to the previous formula, only taking the right side number, which is the acceleration value. Values can be on the X,Y or Z axis, or combined, and explained [here](https://pxt.microbit.org/reference/input/acceleration).

I also added a fixed "Row" column numbered 1-30, so that we will have an X axis for our charts.

The final piece of the puzzle - create two charts from the values. In both of them, the X axis is the row number, and the Y axis is the data coming in from the sensor (either light or acceleration).  
This is what it looks like:

![The end result - incoming data is visualized live!](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/13770i859D1310A25977A3/image-size/large?v=1.0&px=999)

> _The end result - incoming data is visualized live!_

All you have to do now is click "Start" and see the data coming in and being charted live! Shake the device and the acceleration level jumps all over. Flash it with a flashlight or cover it with your hands and the light level chart reflects it. You've just built a cool programmable fidget toy with Excel!

From here on, you can of course implement your own logic to analyze the data and make this example do something real with the data, based on what you want to do.

Hope you found this fun and that you're inspired to go try something yourself! I would love to hear your thoughts on it, so please go ahead and comment below with more ideas, wishes, experiments you did based on this blog, or any other feedback you may have!

Yigal
