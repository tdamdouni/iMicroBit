import random

from microbit import display

names = ['Mary', 'Yolanda', 'Damien', 'Alia', 'Kushal', 'Mei Xiu', 'Zoltan']
display.scroll(random.choice(names))
