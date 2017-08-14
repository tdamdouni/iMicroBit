# https://microbitmathsblog.wordpress.com/2017/03/01/microbit-data-logging/

from microbit import *

logTime = 0
xAccel = accelerometer.get_x()
logData = ""

readInterval = 250
fileName = "acceldata.csv"

def readData(fileName):
    with open (fileName) as myFile:
        data = myFile.read()
    return(str(data))
    
def writeData(fileName, data):
    with open (fileName,'w') as myFile:
        data= str(data)
        myFile.write(data)
    
while True:
    display.show(Image.ARROW_E)
    
    if button_a.is_pressed():
        display.show("X")
        sleep(1000)
        display.clear()
        break
        
    if button_b.is_pressed():
        display.show("W")
        
        logData = "Time,Acceleration\r"
        writeData(fileName, logData)
        
        for x in range(40):
            logData = readData(fileName)
            xAccel = str(accelerometer.get_x())
            logTime = x/(1000/readInterval)
            logData = logData +  str(logTime) + "," + xAccel + "\r"
            writeData(fileName, logData)
            logData = readData(fileName)
            sleep(readInterval)
            
        if button_a.is_pressed():
            display.show("X")
            sleep(1000)
            display.clear()
            break