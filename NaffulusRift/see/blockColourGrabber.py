#This programme was written to identify all the various RGB colours in Minecraft for the Raspberry Pi 
# I'm 100% confident there's an easier way to do it but... damned if I can find it

import os
from PIL import Image
from mcpi.minecraft import Minecraft
from mcpi import *
import pyscreenshot as ImageGrab
import time

mc = Minecraft.create()

mineBlocks =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,26,30,31,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,57,58,60,61,62,64,65,75,71,73,78,79,80,81,82,83,85,89,95,98,102,103,107,246,247]

for i in mineBlocks:
    mc.setBlocks(0,0,0, 5,5,5, mineBlocks[i])
    time.sleep(5)
    