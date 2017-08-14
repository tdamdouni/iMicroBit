import serial
import sys
import pygame
from pygame.locals import *

# Define colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define a few constants for pygame window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
FPS = 30
BUTTONSIZE = 60
BUTTONGAPSIZE = 10

# Calculate the datum for centre image of the window
CENTRE_X = (WINDOWWIDTH / 2) - (BUTTONSIZE / 2)
CENTRE_Y = (WINDOWHEIGHT / 2) - (BUTTONSIZE / 2)

SMALLIMAGESIZE = int(BUTTONSIZE / 2)

# Import the images to be used
imageLeft = pygame.image.load('Rotate270AntiClockwise3Green.png')
imageRight = pygame.image.load('Rotate270Clockwise3Green.png')
imageUp = pygame.image.load('Up.png')
imageDown = pygame.image.load('Down.png')
imageCrane = pygame.image.load('tower_crane2.gif')

# Define scaled images to be used on screen
imageLeftSmall = pygame.transform.scale(imageLeft, (SMALLIMAGESIZE, SMALLIMAGESIZE))
imageRightSmall = pygame.transform.scale(imageRight, (SMALLIMAGESIZE, SMALLIMAGESIZE))
imageLeftLarge = pygame.transform.scale(imageLeft, (BUTTONSIZE, BUTTONSIZE))
imageRightLarge = pygame.transform.scale(imageRight, (BUTTONSIZE, BUTTONSIZE))
imageUpSmall = pygame.transform.scale(imageUp, (SMALLIMAGESIZE, SMALLIMAGESIZE))
imageDownSmall = pygame.transform.scale(imageDown, (SMALLIMAGESIZE, SMALLIMAGESIZE))
imageUpLarge = pygame.transform.scale(imageUp, (BUTTONSIZE, BUTTONSIZE))
imageDownLarge = pygame.transform.scale(imageDown, (BUTTONSIZE, BUTTONSIZE))
imageCrane = pygame.transform.scale(imageCrane, (WINDOWHEIGHT, WINDOWHEIGHT))

# Set up some shapes to be used as buttons
buttonUp1 = pygame.Rect(CENTRE_X,
                        CENTRE_Y - BUTTONGAPSIZE - BUTTONSIZE,
                        BUTTONSIZE, BUTTONSIZE)
buttonUp2 = pygame.Rect(CENTRE_X,
                        CENTRE_Y - 2 * BUTTONGAPSIZE - 2 * BUTTONSIZE,
                        BUTTONSIZE, BUTTONSIZE)
buttonDown1 = pygame.Rect(CENTRE_X,
                          CENTRE_Y + BUTTONGAPSIZE + BUTTONSIZE,
                          BUTTONSIZE, BUTTONSIZE)
buttonDown2 = pygame.Rect(CENTRE_X,
                          CENTRE_Y + 2 * BUTTONGAPSIZE + 2 * BUTTONSIZE,
                          BUTTONSIZE, BUTTONSIZE)
buttonLeft1 = pygame.Rect(CENTRE_X - BUTTONGAPSIZE - BUTTONSIZE,
                          CENTRE_Y,
                          BUTTONSIZE, BUTTONSIZE)
buttonLeft2 = pygame.Rect(CENTRE_X - 2 * BUTTONGAPSIZE - 2 * BUTTONSIZE,
                          CENTRE_Y,
                          BUTTONSIZE, BUTTONSIZE)
buttonRight1 = pygame.Rect(CENTRE_X + BUTTONGAPSIZE + BUTTONSIZE,
                           CENTRE_Y,
                           BUTTONSIZE, BUTTONSIZE)
buttonRight2 = pygame.Rect(CENTRE_X + 2 * BUTTONGAPSIZE + 2 * BUTTONSIZE,
                           CENTRE_Y,
                           BUTTONSIZE, BUTTONSIZE)

# Define line terminator for serial comms
lineTerminator = "\n"

# Open serial connection to micro:bit
comm = serial.Serial('/dev/ttyACM0', 115200)

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Crane Controller')
    DISPLAYSURF.fill(WHITE)

    # Send an initial serial string to stop both motors
    x = 2
    y = 2

    sendString = str(x) + str(y) + lineTerminator
    comm.write(sendString)

    # Display images and shapes for screen buttons
    DISPLAYSURF.blit(imageCrane, (0, 0))

    pygame.draw.rect(DISPLAYSURF, BLUE, buttonUp1)
    pygame.draw.rect(DISPLAYSURF, BLUE, buttonUp2)
    pygame.draw.rect(DISPLAYSURF, BLUE, buttonDown1)
    pygame.draw.rect(DISPLAYSURF, BLUE, buttonDown2)
    pygame.draw.rect(DISPLAYSURF, BLUE, buttonLeft1)
    pygame.draw.rect(DISPLAYSURF, BLUE, buttonLeft2)
    pygame.draw.rect(DISPLAYSURF, BLUE, buttonRight1)
    pygame.draw.rect(DISPLAYSURF, BLUE, buttonRight2)

    offset = int((BUTTONSIZE - SMALLIMAGESIZE) / 2)

    DISPLAYSURF.blit(imageLeftSmall, (buttonLeft1.left + offset, buttonLeft1.top + offset))
    DISPLAYSURF.blit(imageRightSmall, (buttonRight1.left + offset, buttonRight1.top + offset))
    DISPLAYSURF.blit(imageLeftLarge, (buttonLeft2.left, buttonLeft2.top))
    DISPLAYSURF.blit(imageRightLarge, (buttonRight2.left, buttonRight2.top))
    DISPLAYSURF.blit(imageUpSmall, (buttonUp1.left + offset, buttonUp1.top + offset))
    DISPLAYSURF.blit(imageDownSmall, (buttonDown1.left + offset, buttonDown1.top + offset))
    DISPLAYSURF.blit(imageUpLarge, (buttonUp2.left, buttonUp2.top))
    DISPLAYSURF.blit(imageDownLarge, (buttonDown2.left, buttonDown2.top))

    while True: # main game loop
        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                sendString = getButtonClicked(mousex, mousey) + lineTerminator
                comm.write(sendString)
            if event.type == MOUSEBUTTONUP:
                # If button is released, stop both motors
                sendString = "22" + lineTerminator
                comm.write(sendString)
            if event.type == KEYDOWN:
                if event.key == K_q:
                    x = 0
                elif event.key == K_w:
                    x = 4
                elif event.key == K_a:
                    y = 0
                elif event.key == K_s:
                    y = 4

                sendString = str(x) + str(y) + lineTerminator
                comm.write(sendString)

            elif event.type == KEYUP:
                if event.key == K_q:
                    x = 2
                elif event.key == K_w:
                    x = 2
                elif event.key == K_a:
                    y = 2
                elif event.key == K_s:
                    y = 2

                sendString = str(x) + str(y) + lineTerminator
                comm.write(sendString)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    comm.close()
    pygame.quit()
    sys.exit()

def getButtonClicked(x, y):
    if buttonUp1.collidepoint( (x, y) ):
        return "21"
    elif buttonUp2.collidepoint( (x, y) ):
        return "20"
    elif buttonDown1.collidepoint( (x, y) ):
        return "23"
    elif buttonDown2.collidepoint( (x, y) ):
        return "24"
    elif buttonRight1.collidepoint( (x, y) ):
        return "12"
    elif buttonRight2.collidepoint( (x, y) ):
        return "02"
    elif buttonLeft1.collidepoint( (x, y) ):
        return "32"
    elif buttonLeft2.collidepoint( (x, y) ):
        return "42"
    else:
        return "22"
    return None

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
