Micro:bit Notes
===============


First steps
-----------

::

    workon microbit
    pip install microrepl
    pip uninstall pyserial
    pip install "pyserial<3.0"

Plug in micro:bit. See how there's a new USB drive called `MICROBIT`. See
that there's a new serial device `/dev/ttyACM0`.

Try out the REPL::

    $ microrepl
    Quit: Ctrl+] | Stop program: Ctrl+C | Reset: Ctrl+D
    Type 'help()' (without the quotes) then press ENTER.
    MicroPython v1.5-150-g46dcc80 on 2015-11-17; micro:bit with nRF51822
    Type "help()" for more information.
    >>>
    >>> help()
    Welcome to MicroPython on the micro:bit!

    Try these commands:
      display.scroll('Hello')
      running_time()
      sleep(1000)
      button_a.is_pressed()

    [...]

    >>> display.scroll("hello")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'display' is not defined
    >>> dir()
    ['FloatDisplay', '__name__', 'microbit', 'math', 'balance']


Ahh, I see, there's still a custom firmware with the program from the previous
recipient of *Monifa* installed on the micro:bit. Let's write the newest
vanilla MicroPython firmware to the micro:bit::

    $ pip install uflash
    $ uflash
    Flashing Python to: /run/media/chris/MICROBIT/micropython.hex

Let's try the REPL again::

    $ microrepl
    Quit: Ctrl+] | Stop program: Ctrl+C | Reset: Ctrl+D
    Type 'help()' (without the quotes) then press ENTER.
    MicroPython v1.6-11-gfa67b52 on 2016-02-01; micro:bit with nRF51822
    Type "help()" for more information.
    >>> dir()
    ['pin15', 'pin2', 'pin0', 'pin1', 'pin3', 'pin6', 'pin4', 'i2c', 'pin5',
    'pin7', 'pin8', '__name__', 'Image', 'pin9', 'pin14', 'pin16', 'reset',
    'pin19', 'temperature', 'sleep', 'pin20', 'button_a', 'button_b',
    'running_time', 'accelerometer', 'display', 'uart', 'spi', 'panic',
    'pin13', 'pin12', 'pin11', 'pin10', 'compass']

Now we're talking! Let's say hello::

    >>> display.scroll("Hello, Chris!")


Observations
------------

* Measuring voltage between 3V and GND pin:

  3.22V when powered over USB

* In scripts, in contrast to the REPL, no names are pre-imported, you have to
  import all modules you need, i.e. ``import microbit as mb`` or ``from
  microbit import display``.


MIDI
----

Circuit:

https://www.midi.org/articles/midi-electrical-specifications

1. 3.3V connected to MIDI output socket pin 4 via a 35 ohm resistor
2. GND connected to MIDI output socket pin 2
3. Pin 0 (TX) connected to MIDI output socket pin 5 via a 10 ohm resistor

Circuit diagram shows MIDI socket from the back, i.e. where the pins, which
plug into the breadboard / circuit board are. Thus, if you look at the socket
from the back, pin 4 (3.3V) is on the left and pin 5 (TX) is on the right.
GND is the middle pin 2.

To initialize UART for MIDI::

    import microbit
    microbit.uart(baudrate=31250)

To send a MIDI message::

    # send NOTE ON for middle C (60) at velocity 100
    microbit.uart.write(b'\x90\x3c\x64')


Misc notes
----------

Updated the mbed firmware to 0234 via maintenance mode from

https://www.mbed.com/en/development/hardware/prototyping-production/daplink/daplink-on-kl26z/

1. Unplug micro:bit
2. Press and hold reset button
3. Plug in micro:bit
4. Mount MAINTENANCE drive
5. Copy firmware hex file to MAINTENANCE drive and wait a few seconds
6. MAINTENANCE drive disappears and MICROBIT drive appears


Recursion Depth
~~~~~~~~~~~~~~~

The maximum recursion depth is *very* limited:

::

    Traceback (most recent call last):
      File "__main__", line 125, in <module>
      File "__main__", line 102, in play
      File "__main__", line 96, in play
      File "__main__", line 75, in playstep
      File "__main__", line 20, in note_on
      File "__main__", line 18, in channel_message
      File "__main__", line 14, in send
    RuntimeError: maximum recursion depth exceeded

Comment from Damien George on the microbit mailing list:

    Yes, the recursion depth is really limited.  Each call uses about 200
    bytes of stack, plus 4 bytes for each argument or local variable.
    Since there's only 2k of stack (some of which is taken by the start up
    code), you only get about 8 nested calls.

    The microbit is really limited on memory, so please don't expect too
    much from it!

