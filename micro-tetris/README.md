# micro:tetris
micro:tetris is a tetris implementation for [micro:bit](https://www.microbit.co.uk/) written in (kind of) a speedrun in 2 and a half days. Not to be confused with [Micro Tetris](http://troglobit.github.io/tetris.html)!

### Compiling

Because micro:tetris is not written in python or created in block editor as proposed in the micro:bit website (it is written in C++) you need to use the mbed online compiler to compile it:
- Start off by going to https://developer.mbed.org/ and create an account in this website;
- When logged in go to https://developer.mbed.org/compiler/#import:/teams/Lancaster-University/code/microbit-dal/;mode:lib;platform: and click to *Import as* **program** and then **Import**;
- When imported, import the source code of micro:tetris to the library's project and compile it (don't use **Build only**);
- A file with a .hex extension should now download if compiling was successful;
- Now install the program to the micro:bit (drag and drop the .hex file to the micro:bit);

Alternatively you can just drag and drop the pre-compiled file to the micro:bit.
