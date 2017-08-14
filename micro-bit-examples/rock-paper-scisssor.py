# Add your Python code here. E.g.
from microbit import *

num = 0
while True:
    if button_a.is_pressed():
        num = num - 1
        sleep(250)
    if button_b.is_pressed():
        num = num + 1
        sleep(250)

    if num == 3:
        num = 0
    if num == -1:
        num = 2

    moves = [Image.SQUARE, Image.DIAMOND, Image.TRIANGLE]
    move = moves[num]
    display.show(move)
