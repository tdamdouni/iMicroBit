# Become a Time Lord with the BBC micro:bit

_Captured: 2017-10-30 at 18:48 from [blog.groklearning.com](https://blog.groklearning.com/become-a-time-lord-with-the-bbc-micro-bit-c4b8b4e2d747)_

As you've seen in our previous posts, [Grok Learning loves teaching with the BBC micro:bit](https://groklearning.com/microbit/). We're excited about it as a way to bring a whole different dimension to how Python can be taught in the classroom.

![](https://cdn-images-1.medium.com/freeze/max/60/1*Upj4KpbqeqPalgWgaWdUeA.jpeg?q=20)![](https://cdn-images-1.medium.com/max/1600/1*Upj4KpbqeqPalgWgaWdUeA.jpeg)

> _Analog clock hands on a micro:bit._

One of the main questions we see for people who've mastered the basics of MicroPython is "how do I make my program do more than one thing". For example: a program might want to display something on the screen for a certain amount of time, but also respond to button presses during that time. Or perhaps it needs to remember to do something at some point in the future, but continue doing its main function until then.

### What's the problem?

This limitation comes up because most of the methods available to you will suspend the program until they have completed. A simple example is shown below where the program first scrolls a message and then starts responding to button presses.

This means that the code can't respond to user input while the message is scrolling on the screen -- the `while` loop doesn't start until after `display.scroll` finishes. Conceptually, the `display.scroll`method "blocks" the program until it's finished.

This program is supposed to count button presses, and it does work most of the time, but it can't detect any presses while it's scrolling the current number.

> _The counter does not match the number of presses._

This can be solved in some cases using the `wait=False`"kwarg" (key word argument) that many of these blocking functions accept. See <http://microbit-micropython.readthedocs.io/en/latest/display.html> for details.

Now the display.scroll function no longer blocks, and we correctly count the number of presses, but this still has the unfortunate effect of "resetting" the display every time the button is pressed. If you're pressing the button fast enough, you'd never actually see anything on the screen.

What we want instead is a way to have the display show the current count periodically -- perhaps every 10 seconds. We'll see how to do this at the end of the article.

### Making MicroPython do the timing.

Another example is a program that wants to display something for a fixed amount of time (e.g. a timer light), but if we press the button again, the timer should reset.

This program works, but the timing is wrong. If you press the button, then press it again two seconds later, the result is that the display stays on for 10 seconds. Confusingly, if you press the button once, then again many times, it still stays on for 10 seconds. Additionally, if the program wanted to respond to a different input (e.g. button B to immediate turn off the display), it cannot while `sleep()`ing.

This can be solved again by using `wait=False` in conjunction with two extra parameters -- `delay=5000`and `clear=True`.

Now the display will always stay on for 5 seconds since the last time the button was pressed, but because the `show` method doesn't "block", it is always responsive to both buttons.

However, this starts to get very complicated when the program is doing multiple things at once, and it doesn't work for functionality that doesn't support the wait/clear/delay options (for example, turning on a pin or sending commands over serial/SPI/I2C). A more realistic example of this scenario would be if the micro:bit was operating as a timer-controlled light or alarm.

The (broken) example above assumes a light or a buzzer is plugged into pins 0 and 1, but there is no equivalent of wait/clear/delay for `[write_digital](http://microbit-micropython.readthedocs.io/en/latest/pin.html#microbit.MicroBitDigitalPin.write_digital)`, so it has all the same problems as the first example above.

`[running_time()](http://microbit-micropython.readthedocs.io/en/latest/microbit.html#microbit.running_time)` returns the number of milliseconds since the micro:bit was turned on. Note that the micro:bit doesn't have a "[Real Time Clock"](https://en.wikipedia.org/wiki/Real-time_clock) so it has no concept of "the time", only the amount of time that has passed. The timing is accurate enough to make a [simple clock or watch](https://github.com/petejbell/BitWatch), but we'd have to re-set it every time we turned on the micro:bit.

The program above just counts in seconds (using `//` in Python 3 for "integer division").

Rather than using blocking functions (or `sleep()`) like we did above to make our program do things for a certain amount of time, we can instead use `running_time()` to see how much time has passed. Most of the time, our code will need to figure out the time elapsed between two calls to running_time.

This program will display out the time elapsed between each subsequent press of the button.

Let's revisit the example earlier that turned on a pin for five seconds and re-write it to use `running_time()`. The goal is to be able to have each press of button A make the pin stay on for another 5 seconds, and button B immediately turn off the pin.

This still has the same bug, all we've done is effectively implement our own version of sleep and it's otherwise identical to the previous example. _(Note: this is exactly how the sleep() function is actually implemented inside MicroPython)._

But now we have a way to modify this code to do what we want.

We can think of `pin_off_time` as a "timer" for something to happen in the future. This approach generalises to multiple timers, just by adding more variables. _You might even write programs that contain lists of timers -- e.g. tuples of _`_(time, name)_`_ to schedule a named event in the future._

Back to our button press counting example from the beginning. We'd like to have the program display the number of presses every 10 seconds, while still being responsive to button presses. This will combine both `wait=False` and `running_time()`.

Now the `next_update` variable is used to figure out when the next time it should display the count is, and by setting `wait=False` on with `display.scroll`, it happens in the background, allowing us to continue to detect button presses.

> _Fixed!! :D_

Are you interested in learning more about programming MicroPython on the BBC micro:bit. Check out Grok's MicroPython and Blockly courses at <https://groklearning.com/microbit.> We also provide an interactive simulator, allowing you to experiment with the code snippets above without having to program a real device.
