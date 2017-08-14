import picamera
import os
from PIL import Image
from mcpi.minecraft import Minecraft
from mcpi import *
from gpiozero import Button
import time

# Define the PhotoButton
button = Button(4, pull_up = True, bounce_time = 1)
mc = Minecraft.create()

# Load the PiCamera module as camera
camera = picamera.PiCamera()
camera.resolution = (512,384)

def canvasWipe():
	for m in range(len(prevImage)):
		a,b,c = prevImage[m]
		mc.setBlock(a,b,c,0)
	prevImage[:]=[]

# Define the palette of colours to be using when drawing the image
minePalette = {
    (255, 255, 255):0, 	#white 0
    (255,165,0): 1,		#orange 1
    (255,0,255): 2,		#magenta 2
    (173,216,230): 3,	#light blue 3
    (255,255,0): 4,		#yellow 4
    (0,255,0): 5,		#lime 5
    (255,105,180): 6,	#pink 6
    (128,128,128): 7,	#grey 7
    (192,192,192): 8,	#lightgrey 8
    (0,255,255): 9,		#cyan 9
    (128,0,128): 10,		#purple 10
    (0,0,255): 11, 		#blue 11
    (139,69,19): 12,		#brown 12
    (0,128,0): 13,		#green 13
    (255,0,0): 14,		#red 14
    (0,0,0): 15			#black 15
}

prevCanvas = []
prevImage= []

while True:
	posPrev = mc.player.getPos()	# continually get the players location
			
	if button.is_pressed == True:
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
		time.sleep(0.3)
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
				
			else:
				for y in range(height):
					for x in range(width):
						prevImage.append((pos.x+10, pos.y + height-y, pos.z-(width/2)+x))
						rgb = rgb_im.getpixel((x,y))
						mc.setBlock(pos.x+10, pos.y + height-y, pos.z-(width/2)+x, block.WOOL.id, minePalette[rgb])		
		
		elif abs(xDiff) < abs(zDiff):
			
			if zDiff > 0:
				for y in range(height):
					for x in range(width):
						prevImage.append((pos.x-(width/2)+x, pos.y + height-y, pos.z-10))
						rgb = rgb_im.getpixel((x,y))
						mc.setBlock(pos.x-(width/2)+x, pos.y + height-y, pos.z-10, block.WOOL.id, minePalette[rgb])
				
			else:
				for y in range(height):
					for x in range(width):
						prevImage.append((pos.x+(width/2)-x, pos.y + height-y, pos.z+10))
						rgb = rgb_im.getpixel((x,y))
						mc.setBlock(pos.x+(width/2)-x, pos.y + height-y, pos.z+10, block.WOOL.id, minePalette[rgb])	# create the new block from the real world image pixel
						
		else:
			print('No movement detected')

if __name__ == '__main__'