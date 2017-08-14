# this python code create a 16x16 gif and add the 16 minecraft colours of wool to it
from PIL import Image

minePalette = [
    (255, 255, 255), 	#white 0
    (255,165,0),		#orange 1
    (255,0,255),		#magenta 2
    (173,216,230),	#light blue 3
    (255,255,0),		#yellow 4
    (0,255,0),		#lime 5
    (255,105,180),	#pink 6
    (128,128,128),	#grey 7
    (192,192,192),	#lightgrey 8
    (0,255,255),		#cyan 9
    (128,0,128),		#purple 10
    (0,0,255), 		#blue 11
    (139,69,19),		#brown 12
    (0,128,0),		#green 13
    (255,0,0),		#red 14
    (0,0,0)			#black 15
]


newImage = Image.new("RGB", (4, 4))
i=0
for k in range(4):
    for j in range(4):
        newImage.putpixel((k,j), minePalette[i])
        i = i+1

newImage.save("/home/pi/Desktop/test.gif")

