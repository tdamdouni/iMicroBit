import serial

# serial port on raspberry pi will probably be /dev/ttyACM0
PORT = "/dev/ttyACM0"

BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
        data = s.readline().decode('UTF-8')
        data_s = data.rstrip().split(' ')
        try:
            x, y, z, a, b = data_s
            print(x,y,z,a,b)

        except:
            pass

s.close()

