#About
#'Bit:watch' is a Binary Watch programme written in MicroPython for the BBC Micro:bit by @petejbell and distributed under a MIT licence
#Please share with me what you do with it, I'd love to see what you do!
#You can find a tutorial showing you how to build a strap for your watch here: https://t.co/li9CktVJhg

#Instructions
#1)  Download Mu from here: https://github.com/ntoll/mu
#2)  Copy and paste this BitWatch code to Mu, connect your Micro:bit to your computer and then flash the code to your Micro:bit
#3)  The BitWatch will display 18:50 as the time for 10 seconds and will then show '18:51'.
#    Use Button A to set the Hours and B to set the Minutes. Press each one and you will see the hours/minutes increment on the Micro:bit and the Repl console.
#    Use Buttons A+B together to reset seconds to '0'.
#    
#        Column 0 shows the first digit in the hours (in 24hr clock)
#        Column 1 shows the second digit.
#        Column 2 shows the seconds flashing away.
#        Column 3 shows the first digit in the minutes
#        Column 4 shows the second digit.

#For a crash course on binary, see here: http://www.bbc.co.uk/education/guides/z26rcdm/revision/2


#Sets up microbit
from microbit import *

#Sets time variables
hrs = 18
mins = 50
sec = 50
hours = []
minutes = []
seconds = []

#Sets brightness of time digits
b = 9

#defines functions to display time digits
def one(x):
    zero(x)
    display.set_pixel(x, 3, b),        
def two(x):
    zero(x)
    display.set_pixel(x, 2, b),
def three(x):
    zero(x)
    display.set_pixel(x, 3, b)
    display.set_pixel(x, 2, b),   
def four(x):
    zero(x)
    display.set_pixel(x, 1, b),
def five(x):
    zero(x)
    display.set_pixel(x, 3, b)
    display.set_pixel(x, 1, b),
def six(x):
    zero(x)
    display.set_pixel(x, 2, b)
    display.set_pixel(x, 1, b),
def seven(x):
    zero(x)
    display.set_pixel(x, 1, b)
    display.set_pixel(x, 2, b)
    display.set_pixel(x, 3, b),
def eight(x):
    zero(x)
    display.set_pixel(x, 0, b),
def nine(x):
    zero(x)
    display.set_pixel(x, 0, b)
    display.set_pixel(x, 3, b),    
def zero(x):
    for i in range(0,4):
        display.set_pixel(x, i, 0)

#function to create ticking seconds
def fadesecs(x):
    display.set_pixel(2, 2, x)
    display.set_pixel(2, 1, x)

#functions to create a background to show the binary display 'area' (There must be a more efficient way of doing this! Tweet me @petejbell if you can help!)
def background(x,y):
    if display.get_pixel(x, y) < 1: #checks if each pixel is turned off
        display.set_pixel(x, y, 1)  #if so, sets the pixel to a value of 1
def backgrounds():
    for i in range(4):              #misses the flashing seconds column (2) and the last row
        background(0, i)
        background(1, i)
        background(3, i)
        background(4, i)
    
#function to print the time to Repl in MU f(or testing/debugging)
def printtime():
    print(str(hours)+":"+str(minutes)+":"+str(seconds))

#a list of binaries to be used by the function 'displaybinaries' (below)
binaries = [one, two, three, four, five, six, seven, eight, nine, zero]

#function to show the time in binary using the time digits and binaries functions; with the list of functions ('binaries' above)
def displaybinaries():
    global mins #each variable must be defined as 'global' (otherwise the function thinks they are defined 'locally', within itself)
    global hrs
    global minutes
    global hours
    if mins<10:
        binaries[mins-1](4)     #sets column 4 to digit from minutes (if mins between 0 and 9)
        zero(3)                 #clears column 3
        backgrounds()           #calls the backgrounds to (dimly) light 'off' pixels 
    elif mins > 9:
        minutes = [int(i) for i in str(mins)]   #creates a list of two digits from the string of mins
        binaries[minutes[0]-1](3)               #calls the binaries function to display the first digit 
        binaries[minutes[1]-1](4)               #calls the binaries function to display the second digit
        backgrounds()
    if hrs<10:
        binaries[hrs-1](1)
        zero(0)
        backgrounds()
    elif hrs > 9:
        hours = [int(i) for i in str(hrs)]
        binaries[hours[0]-1](0)
        binaries[hours[1]-1](1)
        backgrounds()

#function to check if buttons pressed and increment mins/secs accordingly
def sleepbutton(x):
    global sec
    global hrs
    global mins
    if button_a.was_pressed():
        if hrs < 24:
            hrs += 1
        else:
            hrs = 0
        displaybinaries()
        print(hrs)
    if button_b.was_pressed():
        if mins < 60:
            mins += 1
            sec = 0
        else:
            mins = 0
            sec = 0
        displaybinaries()
        print(mins)
   #if button_a.is_pressed() and button_b.is_pressed(): # This doesn't work. I don't know why :(
   #    if sec < 60:
   #        sec = 1
   #    displaybinaries()
    sleep(x)
 
while True:
    for i in range(0,5):    #iterates 5 times (x 100 = 500)... but....
        sleepbutton(99)     #The code runs a little slow/fast. Play with this number to get it accurate!
    fadesecs(1)             #calls function to 'flash' seconds
    for i in range(0,5):    #iterates 5 times again
        sleepbutton(98)     #see above
    fadesecs(4)             #calls function to 'flash' seconds
    sec += 1
    if sec % 60 == 0:       #this section increments time
        mins += 1
        if mins % 60 == 0:
            hrs += 1
            mins = 0
            if hrs % 24 == 0:
                hrs = 0
    seconds=str(sec)
    minutes=str(mins)
    hours=str(hrs)
    printtime()
    displaybinaries()
