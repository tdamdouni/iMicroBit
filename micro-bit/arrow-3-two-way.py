"""microbit spin arrow both ways with speed/direction controlled by buttons

arrow-3-two-way.py

This was the next logical iteration from arrow-2-speeding.js 
where the speed and direction was under more logical control from the buttons
(B accelerates to left, A accelerates to left - or slows to right)

We worked out a consistent formula as 1 over 2 to-the-power-of speed
and then found that PXT JavaScript DID NOT support exponentiation !*!*!

So it was an excuse to roll up sleeves with MicroPython at last

Then discovered that microbit micropython Image class 
has built-in arrows already - yay, short and sweet!
"""
from microbit import *

speed=0
arrow=0
delay=0
while True:
  if button_a.is_pressed():
    speed=speed-1
  elif button_b.is_pressed():
    speed=speed+1

  if speed<0:
    delay=2**speed
    arrow=arrow-1
    if arrow<0:
      arrow=7
  elif speed>0:
    delay=1/(2**speed)
    arrow=arrow+1
    if arrow>7:
      arrow=0
  
  display.show(Image.ALL_ARROWS[arrow])
  sleep(delay*1000)
