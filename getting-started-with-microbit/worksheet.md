# Getting started with the micro:bit

If you're one of the thousands of schoolchildren across the UK to receive one of the BBC's amazing micro:bits, and you want to learn how you can send code to it from your Raspberry Pi, then this resource will give you a quick and easy setup guide to help you start exploring the micro:bit.

## Starting mu

MicroPython is a small but very fast version of Python 3 that has been specially designed to work on microcontrollers, such as those found on the micro:bit. To start writing MicroPython code on your Raspberry Pi, it's helpful to have an IDE (Integrated Development Environment), to make things a little easier for you. Luckily, **[mu](https://github.com/ntoll/mu)** is an open-source editor designed especially for children, and can run on your Raspberry Pi.

1. Open `Mu` from the main menu under `Programming`.

1. A new window should open up that looks like this:

	![mu screenshot](images/screen1.png)

## Plugging in your micro:bit

The micro:bit has a micro USB port that you can use to connect it to your Raspberry Pi. This will provide a power *and* data connection.

1. Connect your Raspberry Pi to the micro:bit using a USB A-to-micro-B cable, as shown below:

	![usb setup](images/usb.png)

1. You'll know that the micro:bit has connected to your Raspberry Pi, because a dialogue box should pop up like the one below:

	![screen2](images/screen2.png)

1. This dialogue box might pop up a few times while you're playing with the micro:bit. You can simply click on `Cancel` when it does.

## Using mu

The mu software has been designed with young learners in mind. It has a very easy to use interface, and most of the menu items should be self-explanatory.

![screen3](images/screen3.png)

1. The `New` button will open a *new* file. In mu this is done in a new tab. Have a go opening a few new files, and then closing them again.

1. The `Load` button is for opening existing code that you have written.

1. The `Save` button saves any work you have in the visible tab.

1. The `Flash` button will push your code onto the micro:bit. You'll learn more about this later on.

1. The `Repl` button opens an **interactive shell**. This is covered in the next section.

1. The `Zoom` buttons will alter the size of the text in the window.

1. The `Theme` button switches between **light** and **dark** themes. You can choose your preference.

1. The `Help` button will open the Epiphany web browser and take you to the help pages.

1. The `Quit` button will close mu.

## Using the REPL

The *REPL* is an interactive shell, running on the micro:bit itself. Here you can write code and instantly see it running on your micro:bit.

1. Click on the `Repl` button and wait for the interactive shell at the bottom to open up:

	![screen4](images/screen4.png)

1. You can click into the *REPL* and start writing your code straight away. Try the following two lines:

  ```python
  from microbit import *
  display.scroll('Woop, woop')
  ```

1. Did you see the text scrolling across the LED matrix of the micro:bit? If not, you can type the second line again to scroll the message a second time:

  ```python
  display.scroll('Woop, woop')
  ```

1. The *REPL* is a great place to write single lines of code to test them out, but for larger scripts, you'll need to use files.

## Writing and pushing code

1. Click on the `Repl` button again to close the *REPL*.

1. In the main window, you can now write a simple little script to use the micro:bit's buttons:

  ```python
  from microbit import *
  while True:
      if button_a.is_pressed():
          display.scroll('A PRESSED')
      if button_b.is_pressed():
          display.scroll('B PRESSED')
  ```

1. Now you can save this script by clicking on the `Save` button. Call the file **what_pressed.py**.

1. Next, you need to use the mysterious `Flash` button. Press the button and a dialogue box should appear:

	![screen5](images/screen5.png)

1. The amber LED on the underside of your micro:bit should also flash. This is because the file is being loaded onto your micro:bit.

1. Have a go at pushing the buttons on the micro:bit to see the scrolling text across the LED matrix.

## More features of the micro:bit

Some of the cool features on the micro:bit are the GPIO pins, the accelerometer, and compass.

1. If you have access to an LED, a resistor and some leads, you can connect up the micro:bit to the components as shown below. If you don't, then no need to worry. The program you will write also uses the LED matrix.

	![circuit](images/circuit.png)

2. You're going to write a little bit of code that will light an external LED, and some of the LEDs on the matrix, when the micro:bit is shaken. Have a read through the code below, and then use mu to push it to the micro:bit.

  ```python
  from microbit import *

  shake = False
  while True:
      if shake:
          pin0.write_digital(1)
          display.show(Image.SQUARE)
      else:
          pin0.write_digital(0)
          display.clear()
      if accelerometer.was_gesture('shake'):
          shake = not shake
          sleep(500)
  ```

3. Flash the code to your micro:bit and then give it a good shake. Do you see the LEDs changing?

## What next?

- As always, the best way of finding out how to use a new piece of hardware or software (in this case both) is to have a look at the documentation. You can find documentation for MicroPython on the micro:bit at [this site](https://microbit-micropython.readthedocs.org/en/latest/).
- You could have a go at some of the other cool projects using a Raspberry Pi and a micro:bit. Have a look at the following resources:
1. [micro:bit selfies](https://www.raspberrypi.org/learning/microbit-selfies)
2. [micro:bit game controller](https://www.raspberrypi.org/learning/microbit-game-controller)
2. [micro:bit meteorologist](https://www.raspberrypi.org/learning/microbit-meteorologist)

