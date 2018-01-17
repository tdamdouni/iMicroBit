# Simon Game - based on 101Computing - www.101computing.net/microbit-simon-game
from microbit import *
import music
import neopixel
import random
np = neopixel.NeoPixel(pin8, 4)

plus = Image("00000:"
             "00900:"
             "09990:"
             "00900:"
             "00000")

def clear():
    np[0] = (0,0,0)
    np[1] = (0,0,0)
    np[2] = (0,0,0)
    np[3] = (0,0,0)
    np.show()
    
def doALED():
    clear()
    np[0] = (128,0,0)
    np.show()
    
def doBLED():
    clear()
    np[1] = (0,128,0)
    np.show()
    
def doCLED():
    clear()
    np[3] = (0,0,128)
    np.show()
    
def doDLED():
    clear()
    np[2] = (128,128,0)
    np.show()
    
def doABeep():
    tune = ["C4:2"]
    music.play(tune)
    
def doBBeep():
    tune = ["D4:2"]
    music.play(tune)
    
def doCBeep():
    tune = ["E4:2"]
    music.play(tune)
    
def doDBeep():
    tune = ["F4:2"]
    music.play(tune)
    
def doAllOn():
    for pix in range(0 , 4):
            np[pix] = (64,64,64)
            np.show()
            
def flashReady():
    for flashRDY in range(0 , 4):
            doAllOn()
            sleep(50)
            clear()

simonsString = ["A", "B", "C", "D"]

sequence = random.choice(simonsString) + random.choice(simonsString) + random.choice(simonsString)
            
correct = True
sleep(1000)

while correct == True:
  for character in sequence:
        if character=="A":
            doALED()
            doABeep()
        elif character=="B":
            doBLED()
            doBBeep()
        elif character=="C":
            doCLED()
            doCBeep()
        elif character=="D":
            doDLED()
            doDBeep()
        sleep(500)
        display.show(plus)
        clear()
        sleep(500)
   
  flashReady()
  maxInputs = len(sequence)
  capturedInputs = 0
  while capturedInputs < maxInputs and correct == True:
     if pin16.read_digital() == 0:
        doALED()
        doABeep()
        #Did the user guess it wrong? 
        if sequence[capturedInputs] != "A":
            correct = False
        sleep(200)    
        display.show(plus)        
        capturedInputs += 1
        
        
     if pin1.read_digital() == 0:
        doBLED()
        doBBeep()
       #Did the user guess it wrong? 
        if sequence[capturedInputs] != "B":
            correct = False
        sleep(200)
        display.show(plus)
        capturedInputs += 1
        
        
     if pin12.read_digital() == 0:
        doCLED()
        doCBeep()
       #Did the user guess it wrong? 
        if sequence[capturedInputs] != "C":
            correct = False
        sleep(200)
        display.show(plus)
        capturedInputs += 1 
        
        
     if pin2.read_digital() == 0:
        doDLED()
        doDBeep()
       #Did the user guess it wrong? 
        if sequence[capturedInputs] != "D":
            correct = False
        sleep(200)
        display.show(plus)
        capturedInputs += 1         
        
        
  #Add an extra character to the sequence
  if correct == True:
        sequence = sequence + random.choice(simonsString)
        display.show(Image.HAPPY)
        sleep(1000)

#Display Game Over  + final score
if len(sequence)>3:
    music.play(music.FUNERAL)    
    display.scroll("Game Over: Score: " + str(len(sequence))) 
else:
    music.play(music.FUNERAL)
    display.scroll("Game Over: Score: 0")