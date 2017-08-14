# resistor.py  15/03/2016  D.J.Whale

from microbit import *

def draw_dots(n):
    display.clear()
    for i in range(n):
        display.set_pixel(i % 5, int(i / 5), 9)
    
def run(): 
    while True:
        #v = pin0.read_analog()
        v = accelerometer.get_x()
        #v = accelerometer.get_y()
        if v > 1023:
            v = 1023
        v = v / 41
        draw_dots(v)
        sleep(100)

run()

    