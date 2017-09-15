# BBC micro:bit The File System

_Captured: 2017-08-15 at 19:35 from [www.multiwingspan.co.uk](http://www.multiwingspan.co.uk/micro.php?page=files)_

## Introduction

The micro:bit has a small file system. When you flash a program to the micro:bit, that's where it goes. When the micro:bit is running, you can create, delete, and read files. Re-flashing the micro:bit wipes the local storage but switching on an off does not. The flash memory on the micro:bit is **persistent**, anything stored in there is available when the micro:bit is switched on and off though.

We have about 30K to play with, more than good enough to keep a high score, store some images, and whatever you can think of.

## Programming

Here is an example to help you make sense of the way you might go about this. Some of the output here is to the REPL window.
    
    
    from microbit import *import os
    
    # writes to the filewith open('stuff.txt', 'w') as myFile:
        myFile.write("Some text for the file.")# a listing of the file directoryprint(os.listdir())# read the file and print the contentswith open('stuff.txt', 'r') as myFile:
        a = myFile.read()
        print(a)
        display.scroll(a)

The first thing to notice is that we have imported a new module, **os**. This might be familiar if you're a desktop Python user. This is the module that gives us the functionality that we need.

The **with** statement is a neat way to create a block of code for working with the file. The variable **myFile** is the reference to the file that you use to interact with it. A directory listing is carried out and printed to the REPL window. Finally, the file is opened and its contents scrolled across the screen.

## Reference

Your key statement is the **open** statement, used as you see in the example above. It has the following format,

**open(_filename_, _mode_)**

The file modes 'r' and 'w' are used in the example to indicate whether you are reading from the file or writing to it. By default, the reading and writing is in text mode, but this can be specified by adding a 't ' next to the 'r' or 'w'. There is also an option to read and write in binary mode. For this, you add a 'b' to the mode string.

Once the file is open, you can write to it and read from it using write and read statements like in the example above. The following is a summary of these and other actions you can take with a reference to a file,

close()
Closes the file.

name()
Returns the file name.

read()
You can specify how many bytes of the file to read or leave it blank to read the whole file.

readline()
Read a single line from the file. Enter a number of bytes in the brackets if you want to read only some of the characters on the line.

write()
Add a string or bytes object in the brackets to have that data written to the file.

The following statements from the os module are also available to you,

os.listdir()
Gives a listing of the micro:bit directory. This used in the example below to see if a file already exists.

os.remove(_filename_)
Deletes the file.

os.size(_filename_)
Tells you the size in bytes of the file. Knowing that the micro:bit has limited storage capacity, you could use this to check if a file is getting too large.

os.uname()
An interesting function that gives information about the operating system on a desktop computer. For the micro:bit, you get some version information.

## Example Program

To put this feature into use, I thought I'd add high score functionality to the Shut The Matrix example in this section. The game part of the example has been written into a function. A tally is kept of the number of die rolls and the best score is always the lowest.
    
    
    from microbit import *import random
    import os
    
    faces = [Image('00000:00000:00900:00000:00000:'),
            Image('00009:00000:00000:00000:90000:'),
            Image('00009:00000:00900:00000:90000:'),
            Image('90009:00000:00000:00000:90009:'),
            Image('90009:00000:00900:00000:90009:'),
            Image('90009:00000:90009:00000:90009:')]
         
    def nleds(value):
        img = Image('00000:'*5)
        sp = img.set_pixel
        counter = 0
        for row in range(0,5):
            for col in range(0,5):
                if counter<value:
                    sp(col,row,9)
                else:
                    sp(col,row,0)
                counter += 1
        return img
        
    def RandomImages(n, delay):
        for i in range(0,n):
                display.show(random.choice(faces))
                sleep(delay)
                display.clear()
                sleep(delay)def PlayGame():
        counter = 0
        score = 0
        display.scroll("Press A To Roll")
        while counter!=25:
            if button_a.was_pressed():
                display.clear()
                sleep(250)
                roll = random.randint(1,6)
                score += 1
                RandomImages(10,75)
                display.show(faces[roll-1])
                sleep(500)
                if counter+roll==25:
                    # won
                    counter = counter + roll
                elif counter+roll<25:
                    # add on
                    counter = counter + roll
                else:
                # go to end and come back
                    counter = 50 - (counter + roll)
            display.show(nleds(counter))
            sleep(10)
        for i in range(0,10):
            display.show(nleds(25))
            sleep(200)
            display.clear()
            sleep(200)
        return score
    
    def HighScoreExists():
        files = os.listdir()
        for f in files:
            if f=="hi.txt":
                return True
        return Falsedef SetHighScore(s):
        with open('hi.txt', 'w') as h:
            h.write(str(s))def GetHighScore():
        with open('hi.txt', 'r') as h:
            a = h.read()
            return int(a)
    
    
    display.scroll("Shut The Matrix")if HighScoreExists():
        # display score
        x = GetHighScore()
        display.scroll("Best score so far" + str(x))
    sleep(1000)# Main Game Loopwhile True:
        # Start The Game
        rolls_taken = PlayGame()
        display.scroll(str(rolls_taken))
        if HighScoreExists():
            x = GetHighScore()
            if rolls_taken < x:
                # new high score
                SetHighScore(rolls_taken)
                display.scroll("New Best Score")
        else:
            SetHighScore(rolls_taken)
            display.scroll("New Best Score")
        sleep(1000)

When you test this, you need to do badly in your first game. Whatever you score will be the first best score and will be saved. Play again and hope for a better score (fewer die rolls). If you did it in 9 rolls on your first go, reflash the program. It might take ages to do better than that. The unplug the micro:bit and reconnect. The program should show you the previous best score.

## Other Features & Things To Consider

There is a Python library called **ufs** (microfs) that will allow you to copy files to and from the micro:bit using a computer running a desktop operating system. If you flash an empty program (no characters at all) to the micro:bit, you will flash the MicroPython runtime information - what is needed to run a Python program. If you wrote a micro:bit program and saved it onto the micro:bit using ufs, calling it **main.py**, then this would be the program that the micro:bit would run when it next starts up.

Why would you do this? Well, it gives you the chance to set up a project that consists of a main program and several data files. These data files might contain image or text data that is needed for the program sometimes but not all of the time. It could be that these are large tables of data, like a track or maze for a game. You might have several levels. Working this way keeps your main program small and easier to read and allows you to work on things that are designed separately (like mazes).

As you work with different components, particularly as you combine them with one another in different ways, you find yourself looking back and copying blocks of code each time you do it. I have some functions that I use for MIDI, for shift registers and for reading some components like RTCs. I usually copy the functions from program to program. Another approach would be to create Python files containing the relevant functions and statements. You could call these libraries, written well they would be usable to simplify working with the component in any of your future projects.

For example, there are two types of shift register I use. One is an input shift register and one is an output. The key functions I need for these are usually included in my programs as ShiftIn() and ShiftOut().

Let's say I write a file called **shift.py** and include these two functions. When I did a new project that used an input shift register, I would copy this file onto the micro:bit storage along with a main.py file that contained my main program. In order to get the function available for the program, I would write,
    
    
    from shift import ShiftIn

After this, the ShiftIn function would be available to that file or usable via the REPL module. This is very much like importing a Python module and it has some benefits.

It sounds like a kerfuffle and it probably would be for a really simple project. In the long term though, you would find it quicker to develop new projects with components you have used before. You can import one function at a time, keeping things quite efficient. That gives you the scope for creating a module that contains tons of functions that you regularly or intermittently reuse. You can import them from the file when you need them and get into the habit of having that file in the file system of all of your projects.

You can read more about this in the [MicroPython documentation](http://microbit-micropython.readthedocs.io/en/latest/tutorials/storage.html).

## Challenges

  1. You could start by studying the first example program. Make a simple program that creates 2 files containing image data. When the buttons are pressed, show one of the images, reading it from the relevant file.
  2. Take the previous challenge on a step by making a program that allows you to draw an image on the matrix and then save it for later. Keep it simple by allowing only one image. Shake the micro:bit to enter editing mode. You can find code in the Lights Out program that is similar to what you need. Where that toggles the state of a group of LEDs, you just need to toggle the state of one of them. The user can do that with the A button, the B button can be used to save the image and go into display mode. When the program starts it needs to look for the file. If it exists, then its image data should be read and displayed.
  3. Adapt a Python game or program to keep high scores or other data you want to persist between sessions.
  4. Have the micro:bit take readings of the temperature over time and store the data in the file. You can use the ufs to copy files from the micro:bit as well as to it. This could be put into a spreadsheet and you could do something exciting with the data. If you have the components, connect up a sensor, like an ambient light sensor or a UV sensor. Alternatively, use a breakbeam sensor or PIR and record the timings of events over time. Your micro:bit can be used for some simple data logging.
