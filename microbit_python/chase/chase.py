# chase.py  25/04/2016  D.J.Whale

from microbit import *
import random

SPEED = 5

def play_chase():
    player_x = 2
    baddie_x = 0
    baddie_y = 0
    time_lasted = 0
    
    while baddie_y != 4 and time_lasted < SPEED*60:
        display.clear()
        display.set_pixel(baddie_x, baddie_y, 9)
        display.set_pixel(player_x, 4, 9)
        
        if button_a.is_pressed():
            if player_x > 0:
                player_x -= 1

        elif button_b.is_pressed():
            if player_x < 4:
                player_x += 1

        r = random.randint(0,1)
        if baddie_x == player_x:
            baddie_y += r
        elif baddie_x > player_x:
            baddie_x -= r
        else:
            baddie_x += r
       
        sleep(1000/SPEED)   
        time_lasted += 1
        
    return int(time_lasted/SPEED/7)
    
def run():
    while True:
        display.show('C')
        while not button_a.is_pressed():
            sleep(250)
            
        score = play_chase()
        
        for i in range(4):
            display.clear()
            sleep(500)
            display.show(str(score))
            sleep(500)
        sleep(2000)
    
run()

