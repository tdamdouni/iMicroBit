# Developed by Pieter Grobler
# for kode.farm Computer School
# on 27 March 2017

import microbit as m
import math
import random

while True:
    # The following values are set every time the game restarts
    score = 0
    # The snake is represented in a list of coordinates, starting
    # with its head bottom center and tail offscreen
    snake = [{'x': 2, 'y': 4}, {'x': 2, 'y': 5}]
    # Direction of the snake set to UP initially, the x coordinate
    # remains the same (0) and y decreased by 1 with every loop
    direction = {'x': 0, 'y': -1}
    # Random position assigned to the apple
    apple = {'x': random.randrange(5), 'y': random.randrange(5)}
    i = m.Image('00000:'*5)
    s = i.set_pixel
    count_x = 0
    count_y = -0.5
    while True:
        # This loops occurs every half a second
        # We change the direction here: anti-clockwise if the left button
        # was pressed, clockwise if the right button was pressed
        # using a sine calculation
        if m.button_a.was_pressed():
            count_x -= 0.5
            direction['x'] = int(round(math.sin(count_x * math.pi)))
            count_y -= 0.5
            direction['y'] = int(round(math.sin(count_y * math.pi)))
        elif m.button_b.was_pressed():
            count_x += 0.5
            direction['x'] = int(round(math.sin(count_x * math.pi)))
            count_y += 0.5
            direction['y'] = int(round(math.sin(count_y * math.pi)))
        # We establish references to the head and tail of the snake
        snake_tail = snake[len(snake) - 1]
        snake_head = snake[0]
        # We see whether the snake has crashed against the sides
        # and exit this loop if that's the case
        x_out = snake_head['x'] < 0 or snake_head['x'] > 4
        y_out = snake_head['y'] < 0 or snake_head['y'] > 4
        if x_out or y_out:
            break
        # We draw the snake with a brighter head and a dimmer tail
        brightness = 7
        for p in snake:
            if p['x'] >= 0 and p['x'] <= 4 and p['y'] >= 0 and p['y'] <= 4:
                s(p['x'], p['y'], max(brightness, 0))
            brightness -= 2
        # Draw the apple
        s(apple['x'], apple['y'], 9)
        # Render
        m.display.show(i)
        # Using the direction we see where the head of the snake will
        # be next
        new_x = snake_head['x'] + direction['x']
        new_y = snake_head['y'] + direction['y']
        new_snake_head = {'x': new_x, 'y': new_y}
        snake.insert(0, new_snake_head)
        # Did the snake head touch the apple?
        eats_apple = snake_head['x'] == apple['x'] and snake_head['y'] == apple['y']
        # If the snake did not touch the apple, we remove the tail in order for iter
        # to stay the same length
        # If it did touch the apple, we add 1 to the score, and we don't remove this
        # tail this time, so with the addition of the new head, it grows in length by 1
        if not eats_apple:
            snake.remove(snake_tail)
            if snake_tail['x'] >= 0 and snake_tail['x'] <= 4 and snake_tail['y'] >= 0 and snake_tail['y'] <= 4:
                s(snake_tail['x'], snake_tail['y'], 0)
        else:
             score += 1
             apple = {'x': random.randrange(5), 'y': random.randrange(5)}
        # Now we wait half a second before we loop again
        m.sleep(500)

    # This executes if the snake has crashed in the previous loop
    # We show a sad face for a second, then the score
    m.display.show(m.Image.SAD)
    m.sleep(1000)
    m.display.clear()
    m.display.scroll('Score: ' + str(score))
    # Now we wait for pin0 to be touched to start again
    while True:
        if m.pin0.is_touched():
            break
        m.sleep(100)
