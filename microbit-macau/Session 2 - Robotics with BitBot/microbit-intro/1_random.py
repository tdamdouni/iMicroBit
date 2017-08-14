############# ignore this bit for now #############
from microbit import *

def display_image(image):
    display.show(image)
    sleep(1000/8)


############# edit below #############

# complete this function that returns
# a random name!

def random_name():
    return "me"
    # your code
    
############# edit above #############
    

while True:
    images = [Image.DIAMOND_SMALL, Image.SQUARE_SMALL,
              Image.DIAMOND, Image.SQUARE]
    display.show(images, loop=False, delay=200)
    display.scroll(random_name())