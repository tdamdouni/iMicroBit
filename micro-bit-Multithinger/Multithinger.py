from microbit import *
import random

class Timer:
    def __init__(self, time):
        self.time = time
        self.start_time = running_time()
        
    def Start(self):
        self.start_time = running_time()
        
    def Check(self, reset=True):
        if running_time() - self.start_time > self.time:
            if reset:
                self.start_time = running_time()
                
            return True

class ShowTemp():
    def __init__(self):
        self.timer = Timer(3000)    # 3 seconds, best guess
    
    def main(self):
        if self.timer.Check():
            display.scroll("{0}C".format(temperature()), delay=100, wait=False)
    
class ShowImage:        
    def __init__(self):
        self.images = (
            Image.HEART, Image.HEART_SMALL, Image.HAPPY, Image.SMILE, Image.SAD,
            Image.CONFUSED, Image.ANGRY, Image.ASLEEP, Image.SURPRISED, Image.SILLY,
            Image.FABULOUS, Image.MEH, Image.YES, Image.NO, Image.CLOCK12, Image.CLOCK11,
            Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6,
            Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1,
            Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S,
            Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW, Image.TRIANGLE, 
            Image.TRIANGLE_LEFT, Image.CHESSBOARD, Image.DIAMOND, Image.DIAMOND_SMALL,
            Image.SQUARE, Image.SQUARE_SMALL, Image.RABBIT, Image.COW,
            Image.MUSIC_CROTCHET, Image.MUSIC_QUAVER, Image.MUSIC_QUAVERS,
            Image.PITCHFORK, Image.XMAS, Image.PACMAN, Image.TARGET, Image.TSHIRT,
            Image.ROLLERSKATE, Image.DUCK, Image.HOUSE, Image.TORTOISE, Image.BUTTERFLY,
            Image.STICKFIGURE, Image.GHOST, Image.SWORD, Image.GIRAFFE, Image.SKULL,
            Image.UMBRELLA, Image.SNAKE
        )
        
        self.timer = Timer(5000)    # 5 seconds

    def main(self):
        if self.timer.Check():
            display.show(random.choice(self.images))
        

def __main__():
    showTemp = ShowTemp()
    showImage = ShowImage()
    programs = [showTemp.main, showImage.main]

    curState = 0
    curProgram = programs[curState]
    
    while True:
        lastState = curState
        if button_a.was_pressed():
            curState = curState - 1
        elif button_b.was_pressed():
            curState = curState + 1
            
        if curState < 0:
            curState = len(programs) - 1
        elif curState >= len(programs):
            curState = 0
        
        if curState != lastState:
            curProgram = programs[curState]
        
        curProgram();

__main__()