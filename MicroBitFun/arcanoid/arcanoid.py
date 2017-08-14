from microbit import *
import radio
import random
import math


DEG2RAD = math.pi / 180
OFF = 0
HALF = 5
FULL = 9
HEIGHT = WIDTH = 5
MIN_HIEGHT = 0
MAX_HEIGHT = HEIGHT - 1
MIN_WIDTH = 0
MAX_WIDTH = WIDTH - 1
BOARD_QUEUE = {}

def clamp(number, min, max):
    """Returns number limited to range specified by min and max, inclusive"""
    if number < min:
        return min
    elif number > max:
        return max
    else:
        return number

def get_index(raw_value, last_index):
    index = int(round((raw_value / 200) + 1.5, 0))
    return clamp(index, max(last_index - 1, MIN_WIDTH), min(last_index + 1, MAX_WIDTH))

def show_board():
    for (x, y), value in BOARD_QUEUE.items():
        display.set_pixel(x, y, value)
    BOARD_QUEUE.clear()
    
#class 
        
class Plate:
    def __init__(self):
        self.position = 2
        self.width = 2
    def left(self):
        self.position = max(MIN_WIDTH, (self.position - 1))
        self.update_board()
    def right(self):
        self.position = min(MAX_WIDTH + 1 - self.width, (self.position + 1))
        self.update_board()
    def get_plate_indexes(self):
        return range(self.position, self.position + self.width)
    def get_board_row(self):
        plate = self.get_plate_indexes()
        return [FULL if i in plate else OFF for i in range(WIDTH)]
    def update_board(self):
        for i, value in enumerate(self.get_board_row()):
            BOARD_QUEUE[i, MAX_HEIGHT] = value
            
class Ball:
    def __init__(self):
        self.init()
    def init(self):
        self.x = MAX_WIDTH / 2.
        self.y = MAX_HEIGHT / 2.
        self.step = 0.07
        self.set_direction()
    def set_direction(self):
        angle = (random.randrange(90) + 135) % 360
        angle = angle * DEG2RAD
        self.delta_x = math.sin(angle) * self.step
        self.delta_y = math.cos(angle) * self.step
    def process_step(self):
        self.x += self.delta_x
        self.y += self.delta_y
    def process_collision(self, plate):
        x, y = self.get_position()
        indexes = plate.get_plate_indexes()
        hit = False
        if self.delta_y > 0 and y == MAX_HEIGHT and x in indexes:
            self.set_direction()
            hit = True
        if self.x < MIN_WIDTH:
            self.x = MIN_WIDTH
            self.delta_x = -self.delta_x
        if self.x > MAX_WIDTH:
            self.x = MAX_WIDTH
            self.delta_x = -self.delta_x
        if self.y < MIN_HIEGHT:
            self.y = MIN_HIEGHT
            self.delta_y = -self.delta_y
        if self.y > MAX_HEIGHT and not hit:
            raise GameOver()
    def get_position(self):
        return int(self.x + 0.5), int(self.y + 0.5)
class GameOver(Exception):
    pass
while 1:
    try:
        plate = Plate()
        plate.update_board()
        ball = Ball()
        last_ball_position = ball.get_position()
        while 1:
            x = accelerometer.get_x()    
     
#            position = min(3, get_index(x, plate.position))
#            if plate.position != position:
#                plate.position = position
            #print (x)
            #plate.position = x
            plate.update_board()
            show_board()            
            if button_a.was_pressed():
                plate.left()
                plate.update_board()
                show_board()
                #print(123)
            if button_b.was_pressed():
                plate.right()
                plate.update_board()
                show_board()
                #print(321)
            ball.process_step()
            ball.process_collision(plate)
            #display.set_pixel(last_ball_position[0], last_ball_position[1], 0)
            current_ball_position = ball.get_position()
            if current_ball_position != last_ball_position:
                BOARD_QUEUE[current_ball_position] = FULL
                BOARD_QUEUE[last_ball_position] = OFF
                last_ball_position = current_ball_position
            plate.update_board()
            show_board()
    except GameOver:
        display.show(Image.SAD)
        sleep(1000)
        display.clear()