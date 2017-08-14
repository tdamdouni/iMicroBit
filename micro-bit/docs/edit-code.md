
## Getting Started

The new site for coding is [http://microbit.org/code/]

They want you to get started quickly and easily, 
so most of the ways you are encouraged to code 
involve online code building tools that run in your browser. 
These sites allow you to 
build up your code and see the results in an emulator, 
before downloading the compiled HEX file to flash to your micro:bit. 

It's incredibly easy so just dive in :) 

Try one of the two simplest scripting tools below, 
allowing a progressing from block building to code writing, 
or for a more powerful range of features, 
take a look at MicroPython.


### Code Kingdoms - JavaScript

* Nice, easy, editor to get started 
* write simple event-driven code
* switch between block edit view and full text code views
* coding environment allows you to start New projects in other languages
* see instant results from the in-page simulator

[https://www.microbit.co.uk/app/]

### Microsoft PXT - JavaScript

* fresh clean interface
* good help system including tutorials 
* lots of block functions available
* switch easily between block editor and code editor
* see instant results from the in-page simulator
* New Projects always in PXT
* some functions not implemented
	- e.g. exponentiation (x ** y - x to the power of y)

[https://pxt.microbit.org/]


### MicroPython

* rich and powerful language
* [https://python.microbit.org]
* language reference [https://microbit-micropython.readthedocs.io/en/latest]
	- see some interesting stuff with `Image` class [http://microbit-micropython.readthedocs.io/en/latest/image.html]
	- roughly based on `MicroPython for pyboard` [https://docs.micropython.org/en/latest/pyboard/reference/index.html]
	- which is based on Python 3.4 [https://docs.python.org/3.4/reference/index.html]
* no built in simulator
	* for a simulator see [https://create.withcode.uk/]
	* where you will see the microbit emulator appear if you run code with the directive `from microbit import *`
* Language hints
	* Cheat sheet [https://microbit-playground.co.uk/cheat-sheet/]
	* remember python `for loops` are a little weird:
		+ `for i in xrange(10)` - does 0 to 9
		+ `for i in xrange(2,8)` - does 2 to 7
		+ `for i in xrange(7,1,-1)` - does 7 to 2
		+ `for a in ["X","Y","A","B"]` - does X Y then A B


## Flashing your code

Flashing code onto the micro:bit is how you get your program on there. 

Again they have made this really simple with the micro:bit, 
and they even have a flashing orange LED on the back 
that lets you know when you are 'flashing' your code. 

They say flashing because in the 1970s some Read Only Memory (ROMs) 
needed to have a strong UV light shined on them to wipe their old contents 
before you could upload a new program onto them. When NAND memory was invented 
in the late 1980s it was called flash memory as it 'flashed' itself without light. 
Now most permanent storage chips are based on flash memory, but 
search for EPROM if you want to find out more on the history. 


### USB drive

Plug your micro:bit into one of your computer's USB ports 
and it should come up as a storage drive. 
In Linux this should just happen, in Windows 10 you might need to 
be patient (or unplug and replug it) so the driver auto-installs properly. 

### Copy the .HEX to flash

Once you have your micro:bit drive just copy and paste your compiled .HEX file 
into there, and you will see the orange LED on the back flash as the binary is uploaded.

## Other editors

The new online Python Editor [python.microbit.org], 
which also supports [saving .py files to your local disk](https://support.microbit.org/support/solutions/articles/19000021644-save-and-load-python-scripts-from-the-web-editor)


## Ubuntu

### MicroPython

* [http://microbit-micropython.readthedocs.io/en/latest/devguide/installation.html]
* 

This is the fork of MicroPython designed for the BBC micro:bit

The source is [https://github.com/bbcmicrobit/micropython]

### Mu editor


#### Installing

As we are still [waiting for an upstream .deb](https://github.com/mu-editor/mu/issues/58) you should use the latest **`.deb`** file from the official downloads location. I know it says Raspberry Pi but it seems to work on Ubuntu too :)

[http://ardublockly-builds.s3-website-us-west-2.amazonaws.com/?prefix=microbit/raspberry_pi/]

Install it with

```
sudo dpkg -i mu-*.deb
sudo apt-get -f install
```

* source [https://github.com/mu-editor/mu]
* release downloads [https://codewith.mu/#download]

#### Troubleshooting

* if the executable fails with a `Permission denied`
	- make the .bin file executable
		+ `chmod +x mu-x.y.zz.bin`
* if the executable fails with a `Segmentation fault`
	- ensure you are in the dialout group
		+ `sudo usermod -a -G dialout $USER`
* if you get other weird errors:
	- ensure you have all dependencies installed

#### Settings and locations

Files     | Location
----------|---------
Code      | ~/mu_code  (can be overridden in settings)
Settings  | ~/.local/share/mu/settings.json
Logs      | ~/.cache/mu/log/mu.log



#### old install

```
# Previous instructions
#
# still waiting for an upstream .deb [https://github.com/mu-editor/mu/issues/58]
#
# so follow the download install instructions at [https://codewith.mu/#download]

# then make the file executable
chmod +x mu-*.bin
# ensure you are in the dialout group
sudo usermod -a -G dialout $USER


### RUNTIME DEPENDENCIES

# according to [https://github.com/mu-editor/mu/issues/161]
# the only runtime dependencies are:
sudo apt-get install python3-pyqt5.qsci python3-pyqt5.qtserialport
# which will pull python3-pyqt5 automatically as their own dependency
#
# Alternatively you could  install Runtime dependencies (expect python3-setuptools) from 
# https://github.com/mu-editor/mu/blob/master/debian/control
sudo apt-get install python3-pyqt5 python3-pyqt5.qsci python3-pyqt5.qtserialport python3-serial python3-pep8 pyflakes
```

also tried 

```
sudo apt-get install python3-setuptools python3-pip
wget https://raw.githubusercontent.com/mu-editor/mu/master/requirements.txt
wget https://raw.githubusercontent.com/mu-editor/mu/master/setup.py
sudo pip3 install requirements.txt
sudo python3 setup.py install
```

Notes:

* [https://github.com/mu-editor/mu/blob/master/requirements.txt] is designed to be used with pip, but do we need to install all the python setup tools just for this? 
* Especially if the devs have not yet clarified the [difference between runtime and build dependencies](https://github.com/mu-editor/mu/issues/217)
* This is the suggested pip3 install method [https://github.com/mu-editor/mu/issues/239]



## REPL

REPL stands for Read-Eval-Print-Loop, which is a slightly obscure way of referring to the _interactive interpreter_, what most people would think of as the _command line / shell / terminal_. 

As it's a MicroPython interpreter, see examples of some of the things you could type into it, and how it might respond: [https://docs.micropython.org/en/latest/pyboard/reference/repl.html]

If you're really interested in accessing it, you'll need to use a _serial_ connection - see [http://microbit-micropython.readthedocs.io/en/latest/devguide/repl.html], and example Linux commands in [https://forum.micropython.org/viewtopic.php?t=2225#p12697]


## OUT


### ARM mbed

BBC got ARM chip designers to help by using their **mbed** platform, 
which supplies useful _stuff_ for small embedded systems like the 
[micro:bit](https://developer.mbed.org/platforms/Microbit/):
* mbed Hardware Development Kit (HDK) to interface with the board
* mbed Software Development Kit (SDK) to develop libraries that work with the board
* mbed compiler to take code and create executables to flash to the board
* mbed online IDE and compiler to support the online coding sites

Have a look at some of the work they put into this board, 
[https://developer.mbed.org/blog/entry/bbc-microbit-mbed-hdk/]
