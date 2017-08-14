# Having fun with the BBC micro:bit

## Demos

### mood.py

[![micro:bit micropython mood feedback](http://img.youtube.com/vi/CEhl6yVauYY/0.jpg)](http://www.youtube.com/watch?v=CEhl6yVauYY)

Press `A` (sad), `B` (happy) or both (meh) until the "smiley face" becomes
bright enough and flashes.

### rain.py

[![micro:bit micropython rain demo](http://img.youtube.com/vi/FKbMBZA7wAk/0.jpg)](http://www.youtube.com/watch?v=FKbMBZA7wAk)

Nothing to do, just watch "rain pour down the screen".

### morse.py

[![micro:bit micropython morse game](http://img.youtube.com/vi/Ai1WnAvL8yo/0.jpg)](http://www.youtube.com/watch?v=Ai1WnAvL8yo)

Find the morse code for the displayed letter: use the `A` button for short
(less than 250ms) or long (more than 250ms) presses. Once you're done, press
the `B` button to submit your answer.

The proper answer is then scrolled accross the screen.

### temp.py

[![micro:bit micropython temperature](http://img.youtube.com/vi/fFkNeOHV1h4/0.jpg)](http://www.youtube.com/watch?v=fFkNeOHV1h4)

Display the temperature measured by the micro:bit. Display it by "zigzagging"
the display instead of scrolling it from left to right.


### chrono.py

[![micro:bit micropython chrono](http://img.youtube.com/vi/cqSwNh_2GYw/0.jpg)](http://www.youtube.com/watch?v=cqSwNh_2GYw)

Display the time elapsed as HH:MM:SS. Display it by "zigzagging" the display
instead of scrolling it from left to right.

### compass.py

[![micro:bit micropython compass](http://img.youtube.com/vi/086ttLzBSo4/0.jpg)](http://www.youtube.com/watch?v=086ttLzBSo4)

Find the random heading by rotating the micro:bit. The closer you are from the
answer, the brighter the screen will be.

### accel.py

[![micro:bit micropython accel](http://img.youtube.com/vi/4PWaQM7BLF8/0.jpg)](http://www.youtube.com/watch?v=4PWaQM7BLF8)

Shake the micro:bit and see how high you can reach! Press the A button to start
a countdown, when the screen lights up, you have 2 seconds to shake the
micro:bit. It'll then tell you how hard it was shaken.


### usb.py


[![micro:bit micropython usb](http://img.youtube.com/vi/SjCzI3OQxiQ/0.jpg)](http://www.youtube.com/watch?v=SjCzI3OQxiQ)

Read messages sent from the computer connected via USB (serial).

Messages sent to the micro:bit using the pyserial python library on the
computer will be displayed.

An easy way to connect to the micro:bit serial port on the computer is to start
a REPL (using `python`), then:
```
>>> import microfs
>>> s = microfs.get_serial()
>>> s.write("Hello world")
```


## Compiling/Running the demos

The python code in this repository can be compiled to a .hex file using the
[mu editor](http://codewith.mu/) or the
[python microbit online editor](http://python.microbit.org/editor.html).

Connecting your [BBC micro:bit](https://www.microbit.org/) to your computer
using a USB cable will make it appear as a USB mass storage (just as a standard
USB key).

Once you have the .hex file, copy it to the "folder", the led at the back of
the board will blink rapidly while it's flashing it. Once it's done flashing,
everything is ready to enjoy ;)


## Flash from the command line

Say you have created a
[python virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
and installed the requirements using:

```
pip install -r requirements.txt
```

You can now flash your python script from the command line:

```
uflash <your_script_name>.py
```

It will (try to) autodetect your micro:bit. If it can't, then specify the path
to its volume (eg `/Volumes/MICROBIT/<some_file_name>.hex`):

```
uflash <your_script_name>.py /Volumes/MICROBIT/<some_file_name>.hex
```


## Use the "main.py" loader

[![micro:bit micropython loader](http://img.youtube.com/vi/IzlabY8lnFs/0.jpg)](http://www.youtube.com/watch?v=IzlabY8lnFs)

This is a very useful trick:
[mainly main.py](https://microbit-micropython.readthedocs.io/en/latest/tutorials/storage.html#mainly-main-py).

This allows the use of "proper python modules" by uploading a `main.py` file on
the micro:bit filesystem, which will be run on each reset. The prerequisite is
to have an "empty micropython runtime" flashed on the device:

```
uflash
```

Not providing a script will flash the "empty micropython runtime", which will
allow for the use of the `main.py` file you put on the filesystem:

```
ufs put main.py
```

Using `ufs ls` should list the existing files on the filesystem (be careful,
those will all be erased whenever you re-flash your device using `uflash`!).

From now on, and until the next re-flash, whatever is in the `main.py` will be
automatically run on each device reset.

Changing the `main.py` file is MUCH faster than re-flashing the device, and
allows for a much tighter feedback loop (and we all love that).

You can now add the files you want to be run using `ufs put`, and the `main.py`
loader will allow you to choose which one you want to run:
- press the `A` (left) button to cycle through the different modules
- press the `B` (right) button to run the current module
