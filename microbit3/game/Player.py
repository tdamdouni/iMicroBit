from microbit import *

import random
import radio

radio.on()
player_x = 0

shot_y = 1
enemy_x_core = 2
game_over = 0


while True:
    display.set_pixel(player_x,4,9)
    if button_b.was_pressed() and not player_x == 5:
        display.clear()
        player_x = player_x + 1

    if button_b.is_pressed() and player_x == 5:
        display.clear()
        player_x = 0

    if button_a.was_pressed() and not player_x == -1:
        display.clear()
        player_x = player_x - 1

    if button_a.is_pressed() and player_x == -1:
        display.clear()
        player_x = 4
    
    display.set_pixel (enemy_x_core,0,9)
    display.set_pixel (enemy_x_core + 1,0,9)
    display.set_pixel (enemy_x_core - 1,0,9)
    display.set_pixel (enemy_x_core,1,9)

    if running_time() == 1000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 2000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 3000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 4000:
        display.clear()
        enemy_x_core = random.randint(1,3)  

    if running_time() == 5000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 6000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 7000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 8000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 9000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 10000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 11000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 12000:
        display.clear()
        enemy_x_core = random.randint(1,3)  

    if running_time() == 13000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 14000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 15000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 16000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 17000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 18000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 19000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 20000:
        display.clear()
        enemy_x_core = random.randint(1,3)  

    if running_time() == 21000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 22000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 23000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 24000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 25000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 26000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 27000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 28000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 29000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    if running_time() == 30000:
        display.clear()
        enemy_x_core = random.randint(1,3)

    display.set_pixel(enemy_x_core,shot_y,6)

    message = radio.receive()
    
    if message == 'shot':
        shot_y = shot_y + 1

    if message == 'reset':
        shot_y = 1

    if running_time() > 30000 and game_over == 0:
        display.clear()
        display.scroll("YOU WON, SWITCH MICRO:BITS WITH YOUR FRIEND TO LET THEM PLAY AS YOU TRY TO DEFEAT THEM")

    if shot_y == 4 and player_x == enemy_x_core:
        display.clear()
        display.scroll("GAME OVER")
        game_over = 1
