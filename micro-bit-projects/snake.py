from microbit import *
import random


def draw_snake(snake):
    for i in snake:
        if i == snake[0]:
            display.set_pixel(i[0], i[1], 7)
        else:
            display.set_pixel(i[0], i[1], 5)


def draw_food(food):
    display.set_pixel(food[0], food[1], 1)


def bind_snake(snake):
    x = snake[0][0]
    y = snake[0][1]
    if x == 5:
        snake[0][0] = 0
    elif x == -1:
        snake[0][0] = 4
    if y == 5:
        snake[0][1] = 0
    elif y == -1:
        snake[0][1] = 4
    return snake


def move_snake(snake, heading):
    x = snake[0][0]
    y = snake[0][1]
    if heading == "N":
        snake.insert(0, [x, y - 1])
    elif heading == "S":
        snake.insert(0, [x, y + 1])
    elif heading == "W":
        snake.insert(0, [x - 1, y])
    elif heading == "E":
        snake.insert(0, [x + 1, y])
    snake.pop()
    snake = bind_snake(snake)
    return snake


def steer_snake(heading, direction):
    snake_compass = ["N", "E", "S", "W"]
    c_index = snake_compass.index(heading)
    if direction == "R":
        if c_index < 3:
            c_index += 1
        else:
            c_index = 0
    if direction == "L":
        if c_index > 0:
            c_index -= 1
        else:
            c_index = 3
    heading = snake_compass[c_index]
    return heading


def food_check(snake, food):
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        snake.insert(-1, snake[-1])
        return snake, "gone"
    return snake, food


def place_food(snake, food):
    food = [random.choice([0, 1, 2, 3]), random.choice([0, 1, 2, 3])]
    while food in snake:
        food = [random.choice([0, 1, 2, 3]), random.choice([0, 1, 2, 3])]
    return food


def snake_check(snake):
    for i in snake[1:]:
        if i == snake[0]:
            return False


def play_snake():
    Running = True
    snake = [[4, 4]]
    heading = "N"
    food = [random.choice([0, 1, 2, 3]), random.choice([0, 1, 2, 3])]
    display.scroll("SNAKE")
    while Running is True:
        draw_snake(snake)
        draw_food(food)
        snake = move_snake(snake, heading)
        if snake_check(snake) is False:
            display.scroll("GAME OVER")
            sleep(1000)
            Running = False
        snake, food = food_check(snake, food)
        sleep(500)
        display.clear()
        if food == "gone":
            food = place_food(snake, food)
        if button_a.was_pressed():
            heading = steer_snake(heading, "L")
        if button_b.was_pressed():
            heading = steer_snake(heading, "R")

while True:
    play_snake()
