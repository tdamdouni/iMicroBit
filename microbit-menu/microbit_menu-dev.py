'''
    MicrobitMenu DEV

    Author: aztec1337
    Github: https://github.com/aztec1337/microbit-menu/

    Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: http://www.gnu.org/licenses/gpl-3.0.txt
'''
from microbit import *
import random
menuAmount = 4  # Count of menus (starting at 0)
menu = 0  # Default menu to start on
void = 0  # If text scrolled already, don't scroll again until button pressed

# -- START OF DISPLAY FUNCTIONS --

def diceImage():
    diceImage = Image("90009:00000:00900:00000:90009")  # Dice image to infer dice
    display.show(diceImage)
def letterImage():
    letterImage = Image("90000:90000:90000:90000:99990")  # Letter 'L' to infer letter
    display.show(letterImage)
def colourImage():
    colourImage = Image("09990:90000:90000:90000:09990")  # Letter 'C' to infer colour
    display.show(colourImage)
def imageImage():
    imageImage = Image("99999:00900:00900:00900:99999")  # Letter 'I' to infer image
    display.show(colourImage)
def creditsDisplay():
    creditNames = "Made by: aztec1337"
    display.scroll(creditNames, delay = 100)

displayFunctions = {0 : diceImage, 1 : letterImage, 2 : colourImage, 3 : imageImage 4 : creditsDisplay}

# -- END OF DISPLAY FUNCTIONS --

# -- START OF PROCESS FUNCTIONS --

def diceFunction():
    display.show(str(random.randint(1, 6)))  # Random int (1 - 6)
def letterFunction():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    display.show(random.choice(letters))  # Choose random of alphabet
def colourFunction():
    colours = ["RED", "BLUE", "GREEN", "YELLOW", "PINK", "BROWN", "WHITE", "BLACK", "PURPLE"]
    display.scroll(random.choice(colours), delay = 100)  # Chose random of colours
def imageFunction():
    images = [Image.HAPPY, Image.SAD, Image.SMILE, Image.CONFUSED, Image.ANGRY, Image.ASLEEP, Image.SUPRISED, Image.SILLY, Image.FABULOUS, Image.MEH, Image.YES, Image.NO, Image.PACMAN]
    display.show(random.choice(images))  # Chose random of images
def creditsFunction():
    githubUrl = "https://github.com/aztec1337/microbit-menu"
    display.scroll(githubUrl, delay = 100)

processFunctions = {0 : diceFunction, 1 : letterFunction, 2 : colourFunction, 3 : imageFunction, 4 : creditsFunction}

# -- END OF PROCESS FUNCTIONS --

# -- START OF MISC FUNCTIONS -- 

def zeroMenu():
    if menu > menuAmount:
        menu = 0

# -- END OF MISC FUNCTIONS --

while True:
    if void == 0:
        displayFunctions[menu]()
        sleep(250)
        void = 1
    if button_a.is_pressed():  # If display button is pressed
        menu += 1  # Increase menu by 1
        void = 0  # Unvoid text scroll
        zeroMenu()
    if button_b.is_pressed():  # If function button is pressed
        processFunctions[menu]()
