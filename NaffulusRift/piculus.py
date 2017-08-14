# Requires sudo pip3 install pyuserinput python3-xlib

import serial
from time import sleep
from pykeyboard import PyKeyboard
from gpiozero import Button
import picamera
import os
from PIL import Image
from mcpi.minecraft import Minecraft
from mcpi import *


def move ():
    deadzone_x = 200
    deadzone_y = 200
    key_delay = 0.4

    if jumpPad.is_pressed:
        # It's set to pullup then shorted to ground, so we're working backwards here.
        keyboard.press_key('space')
        sleep(key_delay)
        keyboard.release_key('space')
    data = s.readline().decode('UTF-8')
    data_list = data.rstrip().split(' ')
    try:
        x, y, z, a, b = data_list
        if int(x) < (0 - deadzone_x):
            keyboard.press_key('a')
            sleep(key_delay)
            keyboard.release_key('a')
        if int(x) > deadzone_x:
            keyboard.press_key('d')
            sleep(key_delay)
            keyboard.release_key('d')
        if int(y) < (0 - deadzone_y):
            keyboard.press_key('w')
            sleep(key_delay)
            keyboard.release_key('w')
        if int(y) > deadzone_y:
            keyboard.press_key('s')
            sleep(key_delay)
            keyboard.release_key('s')
        else:
            keyboard.release_key('a')
            keyboard.release_key('d')
            keyboard.release_key('w')
            keyboard.release_key('s')
        # print(x, y, z, a, b)
    except:
        pass


def canvasWipe():
    for m in range(len(prevImage)):
        a, b, c = prevImage[m]
        mc.setBlock(a, b, c, 0)
    prevImage[:] = []


if __name__ == "__main__":

    # Set up serial connection to Micro:Bit (move controller)
    PORT = "/dev/ttyACM0"
    # may need to `ls /dev/ttyA*` to find the right Micro:Bit, and sub in line above
    BAUD = 115200

    s = serial.Serial(PORT)
    s.baudrate = BAUD
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE

    keyboard = PyKeyboard()
    jumpPad = Button(11, pull_up=True)

    # Define the PhotoButton
    button = Button(4, pull_up = True, bounce_time = 1)
    mc = Minecraft.create()

    # Load the PiCamera module as camera
    camera = picamera.PiCamera()
    camera.resolution = (512, 384)

    # Camera setup
    # camera.start_preview()
    # time.sleep(2)
    # iso = camera.iso
    # brightness = camera.brightness
    # camera.exposure_mode = 'off'
    # white_balance = camera.awb_gains
    # camera.awg_gains = white_balance
    # print('Setting ISO to:', iso)
    # print('Setting Brightness to:', brightness)
    #
    # camera.stop_preview()

    prevCanvas = []
    prevImage = []

    # Define the palette of colours to be using when drawing the image
    # Define the palette of colours to be using when drawing the image
    minePalette = {
        (255, 255, 255): 0,  # white 0
        (255, 165, 0): 1,	 # orange 1
        (255, 0, 255): 2,	 # magenta 2
        (173, 216, 230): 3,	 # light blue 3
        (255, 255, 0): 4,	 # yellow 4
        (0, 255, 0): 5,		 # lime 5
        (255, 105, 180): 6,	 # pink 6
        (128, 128, 128): 7,	 # grey 7
        (192, 192, 192): 8,	 # lightgrey 8
        (0, 255, 255): 9,	 # cyan 9
        (128, 0, 128): 10,	 # purple 10
        (0, 0, 255): 11, 	 # blue 11
        (139, 69, 19): 12,	 # brown 12
        (0, 128, 0): 13,	 # green 13
        (255, 0, 0): 14,	 # red 14
        (0, 0, 0): 15		 # black 15
    }

    # MAIN LOOP ###
    while True:
        move()  # read serial and process move controller commands

        posPrev = mc.player.getPos()  # continually get the players location

        if button.is_pressed is True:
            print('Image request received')

            # Take the photo using the PiCamera
            camera.capture('/home/pi/Desktop/orig.jpeg')

            # Resize the image using ImageMagick
            os.system("convert /home/pi/Desktop/orig.jpeg -level 0%,100%,1.2 -resize 64x64 /home/pi/Desktop/resized.jpeg")

            # Colourmap the imsage using ImageMagick
            os.system("convert /home/pi/Desktop/resized.jpeg -dither None -remap /home/pi/Desktop/test.gif /home/pi/Desktop/remapped.gif")

            # Open the image in Python  and convert to RGB
            im = Image.open("/home/pi/Desktop/remapped.gif")
            rgb_im = im.convert("RGB")

            width, height = im.size		# get the size of the image
            sleep(0.3)
            pos = mc.player.getPos()
            xDiff = posPrev.x - pos.x
            zDiff = posPrev.z - pos.z

            canvasWipe()

            print('X diff= ', abs(xDiff))
            print('Z Diff= ', abs(zDiff))

            if abs(xDiff) > abs(zDiff):

                if xDiff > 0:

                    for y in range(height):
                        for x in range(width):
                            prevImage.append((pos.x-10, pos.y + height-y, pos.z+(width/2)-x))
                            rgb = rgb_im.getpixel((x,y))
                            mc.setBlock(pos.x-10, pos.y + height-y, pos.z+(width/2)-x, block.WOOL.id, minePalette[rgb])
                    print('dir 2')

                else:
                    for y in range(height):
                        for x in range(width):
                            prevImage.append((pos.x+10, pos.y + height-y, pos.z-(width/2)+x))
                            rgb = rgb_im.getpixel((x,y))
                            mc.setBlock(pos.x+10, pos.y + height-y, pos.z-(width/2)+x, block.WOOL.id, minePalette[rgb])
                    print('dir 4')

            elif abs(xDiff) < abs(zDiff):

                if zDiff > 0:
                    for y in range(height):
                        for x in range(width):
                            prevImage.append((pos.x-(width/2)+x, pos.y + height-y, pos.z-10))
                            rgb = rgb_im.getpixel((x,y))
                            mc.setBlock(pos.x-(width/2)+x, pos.y + height-y, pos.z-10, block.WOOL.id, minePalette[rgb])
                    print('dir 1')


                else:
                    for y in range(height):
                        for x in range(width):
                            prevImage.append((pos.x+(width/2)-x, pos.y + height-y, pos.z+10))
                            rgb = rgb_im.getpixel((x,y))
                            mc.setBlock(pos.x+(width/2)-x, pos.y + height-y, pos.z+10, block.WOOL.id, minePalette[rgb])	# create the new block from the real world image pixel



                    print('dir 3')
            else:
                print('No movement detected')

    s.close()  # Close connection to Micro:Bit (move controller)
