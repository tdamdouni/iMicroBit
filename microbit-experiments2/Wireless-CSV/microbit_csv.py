# By Andrew Mulholland - https://github.com/gbaman/microbit-experiments

import serial
import csv
import sys
from serial.tools.list_ports import comports as list_serial_ports


def guess_port():
    """
    From https://github.com/ntoll/microrepl
    Returns the port for the first micro:bit found connected to the computer
    running this script. If no micro:bit is found, returns None.
    """
    ports = list_serial_ports()
    platform = sys.platform
    if platform.startswith("linux"):
        for port in ports:
            if "VID:PID=0D28:0204" in port[2].upper():
                return port[0]
    elif platform.startswith("darwin"):
        for port in ports:
            if "VID:PID=0D28:0204" in port[2].upper():
                return port[0]
    elif platform.startswith("win"):
        for port in ports:
            if "VID:PID=0D28:0204" in port[2].upper():
                return port[0]
    return None


def main():
    data = [["Value", "Time", "Name"], ]
    try:
        port = guess_port()
        if port == None:
            print("No micro:bit detected!")
            sys.exit(1)
        ser = serial.Serial(port, baudrate=115200)
        print("Micro:bit connected and reading data from it.")
        print("To save the data, simply close the program and it will be saved to microbit_data.csv.")
        while True:
            line = ser.readline().decode()
            lineraw = line[1:len(line) - 4]
            line = ""
            for char in lineraw:
                if char != "\"":
                    line = line + char
            line = line.split(",")
            values = []
            for index, value in enumerate(line):
                if len(line) == 4 and index != 2:
                    values.append(value.split(":")[1])
            data.append(values)
    finally:
        try:
            ser.close()
            with open("microbit_data.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
                print("Data saved to microbit_data.csv!")
        except UnboundLocalError:
            pass

main()
