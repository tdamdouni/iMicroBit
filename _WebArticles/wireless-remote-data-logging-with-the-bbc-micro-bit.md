# Wireless remote data logging with the BBC micro:bit

_Captured: 2017-08-28 at 11:17 from [www.suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2016/06/microbit-logger/)_

I was quite astonished to stumble upon this today - it really is relatively simple to use use the BBC micro:bit to log data remotely, indeed wirelessly.

The micro:bit can log several kinds of data including accelerometer readings in 3 dimensions, magnetic force readings, light levels, compass bearings and temperature (this is I think internal to the board, but may be indicative of the environment).

Here's what you need:

  * 2 BBC micro:bits, one to act as the logger, one as the receiver.
  * A computer with Python and pySerial installed.
  * A battery pack for the logging micro:bit.

I used a MacBook that already had Python 3 / IDLE installed on it, though I had to install pySerial following the instructions here: <http://pyserial.readthedocs.io/en/latest/pyserial.html>

I then followed the instructions here: <https://github.com/gbaman/microbit-experiments/tree/master/Wireless-CSV >

You put [the same code on the logging micro:bit and the receiver](https://github.com/gbaman/microbit-experiments/blob/master/Wireless-CSV/wireless-csv.ts). This uses the Microsoft PXT platform. I found [the PXT editor](https://m.pxt.io/) didn't work properly in Safari, so I used Firefox instead. I also tweaked the code so it logged more than just the accelerometer readings (see below).

You compile the code in the web-based editor, download the HEX file and drag it onto your micro:bits. Send one of them off on its way with a battery pack, and keep one plugged in to your computer. Then you need to run the [Python script](https://github.com/gbaman/microbit-experiments/blob/master/Wireless-CSV/microbit_csv.py) on your computer - this collects data and writes it to a CSV file which you can open in a spreadsheet program like Excel or Open Office. I think it might be better to log time before the other data, and it would be nice if the Python script displayed some data as it comes in - I thought it wasn't working, as the micro:bits don't light up as they are running.

My script logs loads of data so I sorted it in Excel and then made some charts to show temperature changes. See if you can spot when I breathed on it, and when I took it outside:

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2016/06/temp.png)

And from the light levels when I put it in the cupboard under the stairs, and when it went outside:

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2016/06/light-1024x534.png)

I can see plenty of uses for this as the micro:bit devices themselves are relatively inexpensive - science experiments spring to mind. Attach other sensors? Could this even be the basis of a weather station? Attach one to a robot, a drone, perhaps even an animal?! I'm not sure what the range is, but it'll be fun finding out!

Here's my tweaked code that logs way too much data:
    
    
    // By Andrew Mulholland - https://github.com/gbaman/microbit-experiments
    // Simple example to go alongside the Python script for reading data wirelessly using 2 BBC micro:bits.
    // Transmits the 3 accelerometer values alongside a title to allow them to be distinguished later.
    // When they are recieved on the other end, simply write to the serial port to be picked up by the Python Script.
    // Script was written with the Microsoft PXT platform, it can also be found at https://m.pxt.io/vxdmdu.
    
    // If copying below into PXT code section, ignore all comments and copy from line below.
    
    // tweaked by @blogmywiki
    
    radio.setGroup(1);
    basic.forever(() => {
        radio.sendValue("Acc-X", input.acceleration(Dimension.X));
        basic.pause(30);
        radio.sendValue("Acc-Y", input.acceleration(Dimension.Y));
        basic.pause(30);
        radio.sendValue("Acc-Z", input.acceleration(Dimension.Z));
        basic.pause(30);
        radio.sendValue("Compass", input.compassHeading());
        basic.pause(30);
        radio.sendValue("Magnetic force", input.magneticForce(Dimension.Strength));
        basic.pause(30);
        radio.sendValue("Light", input.lightLevel());
        basic.pause(30);
        radio.sendValue("Temp", input.temperature());
        basic.pause(30);
    });
    radio.onDataReceived(() => {
        radio.writeValueToSerial();
    });
    
