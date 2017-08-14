# test.py  20/11/2016  D.J.Whale
#
# Capture accelerometer data from micro:bit to a CSV file

import time
import microbit # will auto connect

FILENAME = "log.csv"

with open(FILENAME, "w") as file:
    file.write("time,x,y,z\n")
    while True:
        line = microbit.get_next_message()
        if line is not None:
            ##print(line)
            x, y, z = line.split(' ')
            now = time.time()
            data = "%d,%s,%s,%s" % (now, x, y, z)
            file.write("%s\n" % data)
            file.flush()
            print(data)



