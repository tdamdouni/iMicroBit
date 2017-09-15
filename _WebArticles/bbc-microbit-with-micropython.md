# BBC Microbit with MicroPython

_Captured: 2017-09-03 at 23:44 from [blog.gbaman.info](http://blog.gbaman.info/?p=727)_

![](http://blog.gbaman.info/wp-content/uploads/2016/02/IMG_9870-1038x576.jpg)

**If you haven't read my initial [first impressions of the Microbit blog post](http://blog.gbaman.info/?p=711), I would suggest have a glance over it first.**

**_This blog post is still a work in progress._**

A few months back, I got the opportunity to sit in a meeting with [Nicholas Tollervey](https://twitter.com/ntoll) while at Raspberry Pi on internship. He had with him an item, rarer at the time than gold dust, an early prototype of a BBC Microbit and he was very excited!  
Around then, [Damien George](https://github.com/dpgeorge) (lead developer of [MicroPython](https://micropython.org/)) had just got a very rough build of MicroPython running on the Microbit.  
Nicholas just had a very rough prototype with him which you simple got a REPL (Read Eval Print Loop, type command in, instantly get result) over a serial connection to the Microbit. But, it was enough to get us all very excited!

Since then, the project as a whole has come a huge way including the development of the excellent Mu editor and overall is now generally very stable with an [excellent set of documentation](https://microbit-micropython.readthedocs.org/en/latest/index.html).

## So why is this exciting?

Although the [other platforms](http://blog.gbaman.info/?p=711) built for kids to write code with for the Microbit are great, Python has the massive advantage that kids already learning it.  
Python is by far the most popular programming language for schools today. The Microbit will work as a great inroad for schools wanting to teach new students a fun introduction to Python.  
For those schools already teaching it Python, those students can go even further using some of the more advanced features and libraries!

## Writing your Python code with Mu

![Mu editor with the same shake program, written in Python using MicroPython.](http://blog.gbaman.info/wp-content/uploads/2016/02/Screen-Shot-2016-02-06-at-18.24.32.png)

> _Mu editor with the same shake program, written in Python using MicroPython._

One of the extremely exciting additions recently has been the launch of the Mu editor.

Mu is an extremely simple Python editor that has similar features to IDLE, but is far easier to use. It uses the QT platform, allowing single file executables for Windows, Mac and Linux to be built. They just work which is wonderful.  
The editor allows you write your Python code, then simply hit the flash button to flash it onto your plugged in Microbit. That is it, no need to download a .hex file and copy it over manually, **Mu takes care of it all**.

A key feature though of Mu is it is **100% offline**. No web access is required which is a very nice feature that I am sure many schools will appreciate. Although it doesn't include an emulator like the other 3 web based editors, it doesn't really need it given you can just hit flash and it is on your Microbit, simple.

On top of this, it also includes support for the **REPL built in**. The REPL commandline can be opened with a single click. This allows you to see any outputs in your script (done with print()) and even get user input using input().  
I really love this given it lets you experiment and try stuff out, before writing your main program.

![Along with writing your programs in the main editor then flashing them to the Microbit, you can also try out stuff using the REPL.](http://blog.gbaman.info/wp-content/uploads/2016/02/Screen-Shot-2016-02-06-at-19.55.11.png)

> _Along with writing your programs in the main editor then flashing them to the Microbit, you can also try out stuff using the REPL._

## Using Mu in schools

Mu is a really cool tool, but I have been getting questions from a stack of teachers about using it in school on locked down school computers.

### Windows

If you have Windows computers, you can grab Mu (a single .exe file, no installation needed) from the [Github page](https://github.com/ntoll/mu) (or a [direct link to the downloads page](http://ardublockly-builds.s3-website-us-west-2.amazonaws.com/?prefix=microbit/windows/)).

If you want to be able to use the REPL (highly recommended) you will also need to download and [install mbed driver](https://developer.mbed.org/handbook/Windows-serial-configuration).  
It is well worth it, although you are able to do it without it. You just won't have access to the REPL.

### Mac / Linux

On Mac OS and Linux, you can download the single executable applications from the [Github page](https://github.com/ntoll/mu) (or a direct link to the downloads page for [Mac OS](http://ardublockly-builds.s3-website-us-west-2.amazonaws.com/?prefix=microbit/osx/) and [Linux](http://ardublockly-builds.s3-website-us-west-2.amazonaws.com/?prefix=microbit/linux/)).  
There is no mbed driver needed for Mac OS/Linux as it is built in, it is built in so you can use the REPL straight away!

### Raspberry Pi

There are specific versions of Mu for the Raspberry Pi! So if you want to use the Microbit with a Pi, you will soon be able to simply type "sudo apt-get install mu", although unfortunately that isn't ready just yet. The direct link to the Raspberry Pi versions can be [found here](http://ardublockly-builds.s3-website-us-west-2.amazonaws.com/?prefix=microbit/raspberry_pi/).  
There is no mbed driver needed for Raspberry Pi Linux, it is built in so you can use the REPL straight away!

## External hardware

You can do some pretty cool things with MicroPython and the BBC Microbit by connecting other hardware to it.

#### Neopixels!

Everyone loves flashy multicoloured LEDs, right? Well the Microbit can drive a stack of them. In our tests, it can drive at least 256 pixels at one time! I have been working on testing the module and also writing documentation for it.

You can check out the [Neopixel module documentation here](https://microbit-micropython.readthedocs.org/en/latest/neopixel.html).

#### Music!

By attaching a simple buzzer to your Microbit, you can get it to play music. In the case below, Amy Mather also made use of Makey Makey style resistive touch to create a music keyboard!

> -- Lisa Mather (@elsie_m_) [February 3, 2016](https://twitter.com/elsie_m_/status/694673753293373441)

You can check out the [music module documentation here](https://microbit-micropython.readthedocs.org/en/latest/music.html).

## SPI/I2C modules

Unlike the other programming environments, MicroPython allows more advanced students or developers to interact with additional sensors/modules using the [I2C](https://microbit-micropython.readthedocs.org/en/latest/i2c.html)/[SPI](https://microbit-micropython.readthedocs.org/en/latest/spi.html) interface libraries.

This opens up use possibilities for connecting additional modules to the Microbit. For example, you could connect an SPI LCD, an OC2 pressure sensor or even an SPI GSM modem to send text messages from your Microbit!  
Is worth keeping in mind, although you _could_ do all this, it isn't as simple as importing a module. It will require a little work (and datasheet reading), but the important bit is people have the tools to do it.

## Other peoples projects

Nicholas has also been making a few videos to demo some new Micropython features.

# To conclude

I am extremely excited for MicroPython and Mu. Although there is going to be a simple web based MicroPython editor coming soon, I think many schools will want to use Mu instead given it can be run completely offline and includes awesome extra features like the REPL.

Although the other programming environments are excellent, and I take my hat off to their development teams as they have done a really great job. I still think MicroPython is the one everyone should be keeping an eye on. It has huge potential to be grabbed by students and allow them the true freedom to run with their ideas while learning a useful language at the same time!
