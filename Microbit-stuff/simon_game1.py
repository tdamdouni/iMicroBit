#Simon Game - based on code from http://www.multiwingspan.co.uk/micro.php?page=simon
from microbit import *
import music
import random

button_pins = [pin13, pin14, pin15, pin16]
led_pins = [pin1, pin8, pin12, pin2]
notes = [659, 880, 330, 554]

def GetRandomSequence():
    return [int(4*random.random()) for i in range(0,100)]

def PlaySequence(t, s):
    for i in range(0,t):
        led_pins[s[i]].write_digital(1)
        music.pitch(notes[s[i]],500)
        led_pins[s[i]].write_digital(0)
        sleep(200)

def Win():
    for i in range(0,4):
        for j in range(0,4):
            led_pins[j].write_digital(1)
            music.pitch(notes[j],50)
            led_pins[j].write_digital(0)    
    sleep(1000)
    
def Loss():
    music.play(music.WAWAWAWAA)
    sleep(1500)
    
def PlayGame():
    turn = 0
    sequence = GetRandomSequence()
    userSequence = [0]*100
    seqlen = 0
    playing = True
    played = False
    while playing==True:
        if turn==0:
            # Just started
            Win()
            turn = turn + 1
        if seqlen==0 and played==False:
            # Sequence needs playing
            PlaySequence(turn, sequence)
            played = True
        elif seqlen==turn:
            # User has entered the sequence
            Win()
            played = False
            turn = turn + 1
            seqlen = 0
        else:
           # User still entering pattern
           for i in range(0,4):
               if button_pins[i].read_digital()==1:
                   userSequence[seqlen] = i
                   if userSequence[seqlen]!=sequence[seqlen]:
                       Loss()
                       playing = False
                   else:
                       seqlen = seqlen + 1
                       led_pins[i].write_digital(1)
                       music.pitch(notes[i],500)
                       led_pins[i].write_digital(0)   
            
def main():
    sleep(50)
    while True:
        display.scroll("Simon")
        if button_a.was_pressed():
            display.clear()
            PlayGame()
            sleep(1000)
        sleep(50)

main() 
