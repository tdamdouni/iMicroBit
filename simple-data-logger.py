###############################################
#                                             #
#  Python Data Logger D Burrin April 2016     #
#                                             #
#  Logs accelerometer to Sparkfun openlogger  #
#                                             #
###############################################

# http://microbitsandbobs.co.uk/downloads/MicroPi-Logger.py
# http://www.microbitsandbobs.co.uk/projects.html

#for more details on the microbit api see
#http://microbit-micropython.readthedocs.org/en/latest/microbit_micropython_api.html

#for more detils on the sparkfun open logger see
#https://www.sparkfun.com/tutorials/393


from microbit import *

#Configure the output rate for the microbit url 
#it supports a range of bauds and strem types
#Openlogger supports th full range of bauds but seems fixed to 8N1
#As the default setting for open logger is 9600 baud i've left it alone
#and initilised the microbit to match
uart.init(baudrate=9600, bits=8, parity=None, stop=1, pins=None)

#Write a set of heading to the log file for use in your spreadsheet later
#the newline at the start is to seperate from the openlog control value that is written on initilaisation
uart.write("\nTime,X,Y,Z,\n")


#microbit infinity loop
while True:
    #start logging
    if button_a.is_pressed():
        #Write a set of heading to the log file for use in your spreadsheet later
        #the newline at the start is to seperate from the openlog control value that is written on initilaisation
        uart.write("\nTime,X,Y,Z,\n")
        
        
        #get the initialisation time in MS of the Microbit  we'll use this later for tracking time
        #running time is the number of miliseconds since power on
        starttime = running_time()
        
        #display an X to show logging has started
        display.show("X")
        while True:
            #get time of data was logged 
            logtime = running_time()-starttime
            
            #convert to string and write to uart
            uart.write(str(logtime))
            uart.write(",")
        
            #get values from accelerometer - comes in as a list (x,y,z) 
            G_reading=accelerometer.get_values()
            
            #write x value
            uart.write(str(G_reading[0]))
            #write the seperator
            uart.write(",")
            
            #Write y value
            uart.write(str(G_reading[1]))
            uart.write(",")
            
            #Write Z value
            uart.write(str(G_reading[2]))
            
            #write new line character
            uart.write("\n")
            
            #stop logging on button b
            if button_b.is_pressed():
                #Clear the screen
                display.clear()
                #wait for 0.5 seconds to ensure last value is writtrn befofe exit
                sleep(500)
                break
        
    display.show("Not Logging")