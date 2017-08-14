############# ignore this bit for now #############
from microbit import *

def get_message(times_pressed):
    ############# edit below #############
    
    # times_pressed is a variable that holds an integer telling you how often
    # button A was pressed. Your task is to create a message that is going to
    # be displayed on the microbit
    message = 'My message'
    
    
    ############# edit above #############
    return message

while True:
    presses = button_a.get_presses()
    display.scroll(get_message(presses))