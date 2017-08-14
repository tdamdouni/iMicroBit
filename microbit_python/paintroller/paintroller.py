# paintroller.py  12/03/2016  D.J.Whale

from microbit import *
import random
import math

# Game parameters
MAX_GAME_TIME = 60000

# Animations
SPLASH_SCREEN = [ ] #TODO
START_GAME    = [ ] #TODO
END_GAME      = [ ] #TODO
ROLLER_MOVE   = [ ] #TODO

def splash_screen():
    button_b.reset_presses()
    while not button_b.was_pressed():
        display.show(SPLASH_SCREEN)
        
def play_game():
    count_dots = 0
    x = 2
    y = 2
    xdir = True
    display.clear()
    start_time = running_time
    prev_compass = compass.heading()
    
    while count_dots < 25 and running_time - start_time < MAX_GAME_TIME:
        #TODO: was_shake: get from gestures
        if was_shake:
            display.show(ROLLER_MOVE)
            r = random.randrange(5)
            if xdir:
                if display.get_pixel(r, y) == 0:
                    display.set_pixel(r, y, 9)
                    count_dots += 1
            else: # must be ydir
                if display.get_pixel(x, r) == 0:
                    display.set_pixel(x, r, 9)
                    count_dots += 1
                    
        h = compass.get_heading()
        if math.abs(h - prev-compass) > 60:
            xdir = not xdir
            prev_compass = h
            if xdir:
                x = random.randrange(5)
            else:
                y = random.randrange(5)

def dots_to_score(dots):
    #TODO: use mathematical division  
    if dots == 25: return 9 # 23 24 25
    if dots >= 22: return 8 # 20 21 22
    if dots >= 19: return 7 # 17 18 19
    if dots >= 16: return 6 # 14 15 16
    if dots >= 13: return 5 # 11 12 13
    if dots >= 10: return 4 # 8 9 10
    if dots >= 7:  return 3 # 5 6 7
    if dots >= 4:  return 2 # 2 3 4
    if dots >= 1:  return 1 # 1
    return 0                # 0

def flash_digit(digit, times):
    for i in range(times):
        display.show(digit)
        sleep(500)
        display.clear()
        sleep(500)
    display.show(digit)
    
def wait_button_b():
    button_b.reset_presses()
    while not button_b.was_pressed():
        pass
    
def run():
    compass.calibrate()
    while True:
        splash_screen()
        display.show(START_GAME)
        score = play_game()
        flash_digit(score)
        wait_button_b()
        display.show(END_GAME)
    
# run()
