# micro:bit games

I have been playing with the [BBC micro:bit](https://www.microbit.co.uk/) and have taught it some games.

micro:bit code is a [standard `.hex` file](https://www.kanda.com/blog/microcontrollers/pic-microcontrollers/pic-hex-file-format/) compiled in the cloud by [an online editor](https://www.microbit.co.uk/app).

The editor offers two languages at the moment:

# [Python](/py)
Some mad genius managed to get the micro:bit, which has roughly the computing power of a teabag, to run [a pretty much fully featured version of Python](https://microbit-micropython.readthedocs.org).

Your `.hex` file, then, is essentially a tiny version of Python followed by your script.

The main advantages of using Python to write code for your micro:bit are:

* The language is *far* less limiting
* [You can compile your code offline](/py/README.md).

[Here is my Python game collection](/py)

# [Javascript](/js)

The basic language choice looks like Javascript, although it lacks many features of true Javascript, including function calls, arrays, objects, floating point numbers, type coersion, dynamic variables, increment operators and, well, nearly everything else that makes Javascript different from assembler.

Your `.hex` file, then, is essentially a heavily compressed and optimised version of the Javascript you enter.

The main advantages of using Javascript to write code for your micro:bit are:

* Syntax errors are shown on your computer instead of scrolling along the micro:bit display.
* The resulting `.hex` files are smaller and send to your micro:bit faster.
* There are graphical editors for those less familiar with code editing.
* The event-driven way of working is often easier to use than Python's stateful model.

[Here is my Javascript game collection](/js)

# Thoughts

Personally, I would like a closer-to-the-metal language than the Javascript-like one that I can compile offline, but the current setup is pretty impressive.
