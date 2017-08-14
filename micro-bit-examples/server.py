"""
http://www.watkissonline.co.uk/wordpress/?p=7906

https://github.com/penguintutor/microbit-micropython/blob/master/
webrobot/pc-webrobot-proxy.py
"""
import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

while True:
    ser.write(b'.')
    try:
        rcv = ser.readline()
    except Exception as e:
        print(e)
        continue
    cmd = rcv.decode('utf-8').rstrip()
