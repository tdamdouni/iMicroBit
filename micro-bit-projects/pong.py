from microbit import *
import music
import random


def pong():
    Running = True
    player = 2
    ball = [4, 2]
    ball_bearing = [-1, 1]
    headings = [-1, 1]
    lives = 3
    ball_turn = 0
    while Running is True:
        if lives == 0:
            display.scroll("GAME OVER")
            sleep(1000)
            Running = False
            pong()
        display.set_pixel(0, player, 5)
        display.set_pixel(ball[0], ball[1], 9)
        if button_a.was_pressed() and player > 0:
            player -= 1
        elif button_b.was_pressed() and player < 4:
            player += 1
        if ball_turn == 2:
            ball_bearing = hit_high_edges(ball, ball_bearing)
            ball_bearing = hit_side_edges(ball, ball_bearing, player)
            if ball_bearing is False:
                lives -= 1
                display.show(str(lives))
                sleep(500)
                ball = [4, 2]
                ball_bearing = [random.choice(headings),
                                random.choice(headings)]
            else:
                ball[0] += ball_bearing[0]
                ball[1] += ball_bearing[1]
            ball_turn = 0
        else:
            ball_turn += 1
        sleep(250)
        display.clear()


def hit_high_edges(item, bearing):
    if item[1] == 0:
        bearing[1] = 1
    elif item[1] == 4:
        bearing[1] = -1
    return bearing


def hit_side_edges(item, bearing, player):
    if item[0] + bearing[0] == 0 and player == item[1] + bearing[1]:
        bearing[0] = 1
    elif item[0] == 0:
        return False
    elif item[0] == 4:
        bearing[0] = -1
    return bearing

pong()

