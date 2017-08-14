# -*- coding: utf-8 -*-
# @Author: Lucy Fletcher
# @Date:   30/07/2017

"""Roleplaying Dice on a Microbit"""

from microbit import *
import random

def NumToPos(num, y_priority = False):
    """Convert a number to its location on the pixel grid.
    
    Accepts values from 0-24, maps from left-right, top-bottom.
    y_priority - swaps mapping to top-bottom, left-right.
    """
    if not y_priority:
        x = num % 5
        y = num // 5
    else:
        y = num % 5
        x = num // 5
    
    return x, y

def TailAnim(time, tail_size = 5, y_priority = False):
    """Plays the 'tail animation'"""
    steps = 24 + tail_size
    sleep_time = time / steps
    for i in range(steps):
        display.clear()
        
        brightness = 9
        for pos in reversed(range(i - tail_size, i)):
            if pos < 0 or pos > 24:
                brightness = brightness - 2
                continue
            
            x, y = NumToPos(pos, y_priority)
            display.set_pixel(x, y, brightness)
            brightness = brightness - 2
        
        sleep(sleep_time)
        
def TailAnimY(time):
    """Plays the 'tail animation' from top-bottom"""
    TailAnim(time, y_priority=True)
    
def WallAnim(time, tail_size = 5, y_priority = False):
    """Plays the 'Wall Animation'"""
    steps = 4 + tail_size
    sleep_time = time / steps
    for i in range(steps):
        display.clear()
        
        brightness = 9
        for pos in reversed(range(i - tail_size, i)):
            if pos < 0 or pos >= 5:
                brightness = brightness - 2
                continue
            
            x, y = NumToPos(pos, y_priority)
            
            if not y_priority:
                while y < 5:
                    display.set_pixel(x, y, brightness)
                    y = y + 1
            else:
                while x < 5:
                    display.set_pixel(x, y, brightness)
                    x = x + 1
                
            brightness = brightness - 2
            
        sleep(sleep_time)
        
def WallAnimY(time):
    """Plays the 'Wall Animation' from top-bottom"""
    WallAnim(time, y_priority=True)
    
def ThinkingAnimation(time):
    """Picks and plays a random animation"""
    animations = (TailAnim, TailAnimY, WallAnim, WallAnimY)
    play = random.choice(animations)
    play(time)
    
def Clamp(num, lbound, ubound):
    return max(lbound, min(num, ubound))
          
def ShowNumber(num, dimNum = 0):
    """Displays a number using the pixel grid"""
    display.clear()
    
    num = Clamp(num, 0, 25)
    dimNum = Clamp(dimNum, num, 25)
    
    for i in range(dimNum):
        x, y = NumToPos(i)
        display.set_pixel(x, y, (9 if i < num else 3))
    
def __main__():
    """Main execution loop, handles input"""
    MIN_SIDES = 2   # Make the roll mean something
    MAX_SIDES = 25  # Limited by the number of pixels in the grid
    
    ANIM_TIME = 750
    
    sides = MIN_SIDES
    ShowNumber(sides)
    
    result = -1
    
    pulseFlag = False
    pulseTime = 0
    pulsePeriod = 500
    
    while True:
        newSides = sides
        
        if button_a.was_pressed():
            if sides > MIN_SIDES:
                newSides = sides - 1
        elif button_b.was_pressed():
            if sides < MAX_SIDES:
                newSides = sides + 1
                
        # Prevents overwriting the displayed result
        if newSides != sides:
            sides = newSides
            ShowNumber(sides)
            result = -1
                
        # Shaking isn't very reliable...
        if accelerometer.was_gesture("shake"):
            ThinkingAnimation(ANIM_TIME)
            result = random.randint(1, sides)
            pulseFlag = False
            
        if result != -1:
            if running_time() - pulseTime > pulsePeriod:
                pulseFlag = not pulseFlag
                pulseTime = running_time()
                
                if pulseFlag:
                    ShowNumber(result, sides)
                else:
                    ShowNumber(0, sides)
            
__main__()