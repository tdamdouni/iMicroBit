import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1);

textFilename = 'Temperature_Readings.txt'

textFile = open(textFilename, 'w')

while(True):
    rcv = ser.readline();
    cmd = rcv.decode('utf-8').rstrip()
    if (cmd == 'STOP'):
        textFile.close();
        print('Temperature Logging Finished')
        break;

    if (len(cmd) > 0):
        textFile.write(cmd + '\n')
        print(cmd)
