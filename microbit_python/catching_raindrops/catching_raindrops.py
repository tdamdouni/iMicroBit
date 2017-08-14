# catching_raindrops.py  08/03/2016  D.J.Whale

from microbit import *
import math
import random

# Game parameters
CUP_CAPACITY = 5
SPEED = 6
MAX_MISSES = 3
SENSITIVITY = 400

speed = SPEED

# Images
BLANK      = Image('00000:00000:00000:00000:00000')
BLINK      = Image('00000:09090:00000:00000:00000')
CUP        = Image('00000:00000:00000:09090:09990')
CUP_FULL   = Image('00000:00000:00000:09990:09990')
CUP_BLINK  = Image('00000:09090:00000:09090:09990')

CUP_CATCH1 = Image('00000:00000:00000:09990:09990')
CUP_CATCH2 = Image('00000:00000:00000:90909:99999')

CUP_JUMP1  = Image('00000:09090:09990:00000:00900')
CUP_JUMP2  = Image('00000:00000:09090:09990:00000')

CUP_DRAIN1 = Image('00000:00000:00900:09090:09990')
CUP_DRAIN2 = Image('00000:00900:00000:09090:09990')
CUP_DRAIN3 = Image('00900:00000:00000:09090:09990')

CUP_OVER1  = Image('00000:00000:09990:09990:09990')
CUP_OVER2  = Image('00000:00000:09090:99999:09990')
CUP_OVER3  = Image('00000:00000:00000:99999:09990')
CUP_OVER4  = Image('00000:00000:00000:09990:99999')

CUP_FLOAT1 = Image('00000:00000:00000:00000:99999')
CUP_FLOAT2 = Image('00000:00000:00000:09990:09090')
CUP_FLOAT3 = Image('00000:00000:00000:99999:00000')
CUP_FLOAT4 = Image('00000:00000:09990:09090:00000')
CUP_FLOAT5 = Image('00000:00000:99999:00000:00000')
CUP_FLOAT6 = Image('00000:09990:09090:00000:00000')
CUP_FLOAT7 = Image('00000:99999:00000:00000:00000')
CUP_FLOAT8 = Image('09990:09090:00000:00000:00000')
CUP_FLOAT9 = Image('99999:00000:00000:00000:00000')

# Animations
SPLASH     = [CUP, CUP_BLINK]
DROPPED    = [CUP, CUP_JUMP1, CUP_JUMP2, CUP]
CAUGHT     = [CUP_CATCH1, CUP_CATCH2, CUP]
DRAINING   = [CUP_FULL, CUP_DRAIN1, CUP_DRAIN2, CUP_DRAIN3, CUP]
OVERFLOW   = [CUP_FULL, CUP_OVER1, CUP_OVER2, CUP_OVER3, CUP_OVER4, CUP_FULL]
HEAVEN     = [CUP, CUP_FLOAT1, CUP_FLOAT2, CUP_FLOAT3, CUP_FLOAT4, CUP_FLOAT5, CUP_FLOAT6, CUP_FLOAT7, CUP_FLOAT8, 
              CUP_FLOAT9, BLANK, BLINK, BLANK]

def show_splash_screen():
    button_a.reset_presses()
    while not button_a.was_pressed():
        display.show(SPLASH, delay=250)

def get_cup_position():
    acc = accelerometer.get_x()/SENSITIVITY
    acc += 2
    if acc > 4:
        acc = 4
    elif acc < 0:
        acc = 0
    return int(acc)

def show_number(n):
    for i in range(4):
        display.show(str(n))
        sleep(500)
        display.clear()
        sleep(500)
        
    display.show(str(n))
    sleep(2000)
       
def play_game(): #TODO
    global speed
    score = 0
    drops_in_cup = 0
    misses = 0
    drop_x = 0
    drop_y = 0
    cup_x = 2
    state = "NEWDROP"
    
    while True:
        cup_inverted = accelerometer.get_y() < -800
        
        if state == "NEWDROP":
            # create new drop at random position
            drop_x = random.randrange(5)
            drop_y = 0
            state = "RAINING"
            
        elif state == "RAINING":
            # show cup
            cup_x = get_cup_position()
            img = CUP.shift_right(cup_x-2)
            display.show(img)
            if drops_in_cup == CUP_CAPACITY: # cup full
                display.show(CUP_FULL)
            # draw drop plot
            display.set_pixel(drop_x, int(drop_y/speed), 9)
            sleep(100)
            if drop_y >= 4*speed:
                state = "ATCUP"
            else:
                # move drop down
                drop_y += 1
            if cup_inverted and drops_in_cup >= CUP_CAPACITY:
                state = "EMPTYING"
            
        elif state == "ATCUP":
            if drop_x == cup_x:
                state = "CATCH"
            else:
                state = "MISS"
            
        elif state == "MISS":
            misses += 1
            display.show(DROPPED)
            if misses > MAX_MISSES:
                state = "GAMEOVER"
            else:
                state = "NEWDROP"
            
        elif state == "CATCH":
            drops_in_cup += 1
            display.show(CAUGHT)
            if drops_in_cup == CUP_CAPACITY:
                state = "FULL"
                score += 1
            elif drops_in_cup > CUP_CAPACITY:
                state = "OVERFLOW"
            else:
                score += 1
                state = "NEWDROP"
            
        elif state == "FULL":
            display.show(CUP_FULL)
            state = "NEWDROP"
            
        elif state == "EMPTYING":
            display.show(DRAINING)
            drops_in_cup = 0
            if speed > 1:
                speed -= 1
            state = "NEWDROP"
            
        elif state == "OVERFLOW":
            display.show(OVERFLOW)
            state = "GAMEOVER"
            
        elif state == "GAMEOVER":
            display.show(HEAVEN)
            break # end of game
            
    return score
        
def run(): #TO TEST
    high_score = 0
    
    while True:
        show_splash_screen()

        score = play_game()
        if score > high_score:
            display.scroll("HIGH")
            high_score = score
        show_number(high_score)

run()

    
    
