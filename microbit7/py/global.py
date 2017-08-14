from microbit import *
import random

score = 0

def choose_game():
    global score
    display.show(icon)
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            while button_a.is_pressed() or button_b.is_pressed():
                pass
            score = 0
            play()
            display.scroll(str(score))
            while not button_a.is_pressed() or not button_b.is_pressed():
                pass
            while button_a.is_pressed() or button_b.is_pressed():
                pass
            display.show(icon)

a_was_pressed = False
b_was_pressed = False
on_double = False
def button_sleep(time, doubles = True, queue = None):
    global a_was_pressed
    global b_was_pressed
    global on_double
    if queue == None:
        queue = []
    while time > 0:
        sleep(10)
        time -= 10
        a_down = button_a.is_pressed()
        b_down = button_b.is_pressed()
        a_released = a_was_pressed and not a_down
        b_released = b_was_pressed and not b_down
        a_pressed = not a_was_pressed and a_down
        b_pressed = not b_was_pressed and b_down
        if doubles:
            # if a second button goes down it is a new double.
            if a_down and b_down and (a_pressed or b_pressed):
                on_double = True
            # if one of two buttons is released, that's a double-press
            if a_was_pressed and b_was_pressed and (a_released or b_released):
                queue.append('ab')
            # if the last button is released, clear the double.
            if not a_was_pressed and not b_was_pressed:
                on_double = False
        else:
            on_double = False
        if not on_double:
            if a_released:
                queue.append('a')
            if b_released:
                queue.append('b')
        a_was_pressed = a_down
        b_was_pressed = b_down
    return queue

def is_lit(image, pos):
    if pos['x'] < 0 or pos['x'] >= 5 or pos['y'] < 0 or pos['y'] >= 5:
        return False
    return image.get_pixel(pos['x'], pos['y'])

def light_pixel(image, pos, value = 9):
    if pos['x'] >= 0 and pos['x'] < 5 and pos['y'] >= 0 and pos['y'] < 5:
        image.set_pixel(pos['x'], pos['y'], value)

def unlight_pixel(image, pos):
    light_pixel(image, pos, 0)

def random_pos():
    return { 'x': random.randint(0, 4), 'y': random.randint(0, 4) }

#% GAME CONTENTS HERE

choose_game()
