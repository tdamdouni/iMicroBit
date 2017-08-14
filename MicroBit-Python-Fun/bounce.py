from microbit import *


class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 4
        self.height = 4
        self.x_speed = 1
        self.y_speed = 1

    def bounce(self, sleep_time):
        #clear out the previous location
        display.set_pixel(self.x, self.y, 0)
        
        # Change the location of the ball using speed
        self.x += self.x_speed
        self.y += self.y_speed

        # if the ball has reached either the right or left edge of the screen
        # multiply speed by -1 to reverse the direction!
        # Identical logic is applied to the y direction as well.
        if self.x > self.width:
            self.x_speed *= -1
            # in case speed is more than 1, the next line makes sure there is no error
            # as the coordinate cannot be more than the width
            self.x = self.width 
        if self.x < 0:
            self.x_speed *= -1
            self.x = 0
        if self.y > self.height:
            self.y_speed *= -1
            self.y = self.height
        if self.y < 0:
            self.y_speed *= -1
            self.y = 0
        display.set_pixel(self.x, self.y, 9)
        sleep(sleep_time) # makes sure the ball doesn't move too fast
        
    def change_x(self):
        display.set_pixel(self.x, self.y, 0)
        self.x += 1
        if self.x > self.width:
            self.x = 0
        display.set_pixel(self.x, self.y, 9)
        
    def change_y(self):
        display.set_pixel(self.x, self.y, 0)
        self.y += 1
        if self.y > self.height:
            self.y = 0
        display.set_pixel(self.x, self.y, 9)


def stop():
    display.clear()
    display.show(Image.HEART)
    sleep(500)
    display.scroll("Bye bye")


def new_ball():
    list_of_balls.append(Ball(random(5), random(5)))


keep_playing = True
list_of_balls = []
new_ball()

# reduce sleep time more the more balls there are so that
# the balls don't slow down too much
sleep_time = 100 // (len(list_of_balls) + 1)

while keep_playing:
    for ball in list_of_balls:
        ball.bounce(sleep_time)
    if button_a.is_pressed() and button_b.is_pressed():
        if len(list_of_balls) > 3:
            stop()
            keep_playing = False
        else:
            new_ball()
    elif button_a.is_pressed():
        for ball in list_of_balls:
            ball.change_x()
    elif button_b.is_pressed():
        for ball in list_of_balls:
            ball.change_y()
