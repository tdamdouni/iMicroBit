# http://www.microbitsandbobs.co.uk/downloads/lcd3.01.py
# http://www.microbitsandbobs.co.uk/projects.html (project 7)

# 29/4/16 D Burrin
#v3 1/5/16
#v3.01 26/6/16 added full stop for character and init_board fucntion for first start
#removed some unused rubbish
#bugs - there is still a minor niggle with certain charaters.  Captial O seems to leak into the next
#column and lower case o displays as upper.  The Chachater Map appears correct and this maybe to
#differences in the cheap chinese clones of the LCD Display
# Functions to drive a standard 16x2 LCD screen
from microbit import *
#inital state values for the LCD Screen
PINS=[0,0,0,0,0,0,0,0]
RS=0
E=0

#Character set I've not included all just add the extra needed into the dictionary
#The full charactermap can be found as an image in the project website
CharacterMap = {
    'A':"01000001",
    'B':"01000010",
    'C':"01000011",
    'D':"01000100",
    'E':"01000101",
    'F':"01000110",
    'G':"01000111",
    'H':"01001000",
    'I':"01001001",
    'J':"01001010",
    'K':"01001011",
    'L':"01001100",
    'M':"01001101",
    'N':"01001110",
    'O':"01001111",
    'P':"01110000",
    'Q':"01010001",
    'R':"01010010",
    'S':"01010011",
    'T':"01010100",
    'U':"01010101",
    'V':"01010110",
    'W':"01010111",
    'X':"01011000",
    'Y':"01011001",
    'Z':"01011010",
    "a":"01100001",
    "b":"01100010",
    "c":"01100011",
    "d":"01100100",
    "e":"01100101",
    "f":"01100110",
    "g":"01100111",
    "h":"01101000",
    "i":"01101001",
    "j":"01101010",
    "k":"01101011",
    "l":"01101100",
    "m":"01101101",
    "n":"01101110",
    "o":"01101111",
    "p":"01110000",
    "q":"01110001",
    "r":"01110010",
    "s":"01110011",
    "t":"01110100",
    "u":"01110101",
    "v":"01110110",
    "w":"01110111",
    "x":"01111000",
    "y":"01111001",
    "z":"01111010",
    "0":"00110000",
    "1":"00110001",
    "2":"00110010",
    "3":"00110011",
    "4":"00110100",
    "5":"00110101",
    "6":"00110110",
    "7":"00110111",
    "8":"00111000",
    "9":"00111001",
    " ":"00100000",
    "=":"00111101",
    "_":"01011111",
    ".":"00101110"
}

#Clear screen function
def cls(RS,PINS):
    RS= 0
    PINS= [0,0,0,0,0,0,0,1]
    Write2Pins(RS,PINS)

##Function to write to the LCD pins
#Depending on how you wire your LCD you can change the pinxx value to the pin you have connected.
def Write2Pins (RS,PINS):
    #set enable to write
    E=1
    
    pin12.write_digital(RS)#RS
    
    pin9.write_digital(PINS[0])#D7
    pin7.write_digital(PINS[1])#D6
    pin6.write_digital(PINS[2])#D5
    pin4.write_digital(PINS[3])#D4
    
    pin3.write_digital(PINS[4])#D3
    pin2.write_digital(PINS[5])#D2
    pin1.write_digital(PINS[6])#D1
    pin0.write_digital(PINS[7])#D0

    #write
    pin10.write_digital(E)#E
    
    #reset enable to off
    E=0
    pin10.write_digital(E)#e
    
    #some of the command writes take upto 2ms to complete i've gone 5 here for safety 
    #but any value >2 should be fine
    sleep(5)

# Initialise the screen    
def init(RS,PINS):
    RS=0
    PINS=[0,0,1,1,1,0,0,0]#8bit mode 2 lines 5x7
    Write2Pins(RS,PINS)

#set screen up for display    
def PrepScreen(RS,PINS):
    RS=0
    PINS=[0,0,0,0,1,1,1,1]#Display on, Cursor on, Cursor Blink
    Write2Pins(RS,PINS)

#switch to entry mode   
def EntryMode(RS,PINS):
    RS=0
    PINS=[0,0,0,0,0,1,1,0]#Entry mode, Inc cursor, No display shift
    Write2Pins(RS,PINS)

#send charachter to screen    
def Send_Chars(RS,PINS,Message):
    #RS mode HIGH
    RS=1
     
    for Character in Message:
        Char2Write = CharacterMap[Character]
        
        MyChar=list(Char2Write)
        for bit in range (len(Char2Write)):
            #need to send an array of ints not strings
            PINS[bit]=int(MyChar[bit])
    
        Write2Pins(RS,PINS)
        
#initise board for first use
def Init_Board(RS,PINS):
    init(RS,PINS)
    PrepScreen(RS,PINS)
    EntryMode(RS,PINS)
    cls(RS,PINS)        
###########################################################################


#################################### How to use ######################################################
##Below is a demo on using the LCD screen I've linked it with a temperature reading for a bit of fun##
######################################################################################################

#set everything up first this only needs doing once#
Init_Board(RS,PINS)

#clear the screen first - if i didn't do this is worked but i seemed to lose firs char on first display#

#cls(RS,PINS)
#Message = "CATS"
#Send_Chars(RS,PINS,Message)

#######You can also write directly to the LCD########
#cls(RS,PINS)
#Write2Pins(1,[0,1,1,1,1,0,1,0])#display a single z
#sleep(1000)


###############################Real world applicatio demo#####################################
##############This is a demo to display and update the temperature to the lcd screen##########
ambient = 0
#call temperature function a int in degrees C is Recieved
ctemp = temperature()
cls(RS,PINS)

while ctemp != ambient:
    Message="Temperature ="+str(temperature())+"c"
    Send_Chars(RS,PINS,Message)
    sleep (2000)
    cls(RS,PINS)