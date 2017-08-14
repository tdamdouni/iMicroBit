############# ignore this bit for now #############
from microbit import *

def display_image(image):
    display.show(image)
    sleep(1000/8)
    

images = [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE,
          Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]

def show():
    ############# edit below #############
    
    # images is a list of arrow images.
    # display each of those images using display_image:
    # display_image(my_image) displays my_image if it is 
    # a variable containing an image.
    
    ############# edit above #############
    

while True:
    show()