import serial
import urllib.request

roboturl = 'http://10.5.5.1'

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)


while True:
    rcv = ser.readline()
    cmd = rcv.decode('utf-8').rstrip()
    # make sure it's not empty
    if (cmd):
        fetch_url = roboturl + cmd
        print (fetch_url)
        response = urllib.request.urlopen(fetch_url)
        print (response.read())
