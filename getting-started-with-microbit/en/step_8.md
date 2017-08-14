## Writing and pushing code

- Click on the `Repl` button again to close the *REPL*.

- In the main window, you can now write a simple little script to use the micro:bit's buttons:

  ```python
  from microbit import *
  while True:
      if button_a.is_pressed():
          display.scroll('A PRESSED')
      if button_b.is_pressed():
          display.scroll('B PRESSED')
  ```

- Now you can save this script by clicking on the `Save` button. Call the file **what_pressed.py**.

- Next, you need to use the mysterious `Flash` button. Press the button and a dialogue box should appear:

	![screen5](images/screen5.png)

- The amber LED on the underside of your micro:bit should also flash. This is because the file is being loaded onto your micro:bit.

- Have a go at pushing the buttons on the micro:bit to see the scrolling text across the LED matrix.

