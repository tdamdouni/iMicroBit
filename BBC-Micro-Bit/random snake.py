from microbit import *

from random import randint
x=2
y=2
x1=2
y1=2
x2=2
y2=2
blank = Image("00000:""00000:""00000:""00000:""00000")
while True:
    display.show(blank)
    display.set_pixel(x, y, 9)
    display.set_pixel(x1, y1, 7)
    display.set_pixel(x2, y2, 5)
    sleep(50)
    x2 = x1
    y2 = y1
    x1 = x
    y1 = y
    direction=(randint(0,3))
    if   direction==0:      y=min(y+1,4)
    elif direction==1:      x=min(x+1,4)    
    elif direction==2:      y=max(0,y-1)
    elif direction==3:      x=max(0,x-1)
