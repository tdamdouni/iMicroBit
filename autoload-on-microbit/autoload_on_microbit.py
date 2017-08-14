#!/usr/bin/env python
# -*- coding: utf-8 -*-
__name__ = "Autoload on Micro:Bit"
__version__ = "1.0"
__description__ = "Script to load .hex files automatically into Micro:Bit"
__author__ = "Jon Ander Besga"
__repository__ = "https://github.com/jabesga/autoload-on-microbit"

import signal
import glob
import shutil

DOWNLOAD_FOLDER = '/home/jon/Downloads'
DESTINATION_DISK = '/run/media/jon/MICROBIT'

print("-= Autoload on Micro:Bit =-")

try:
    print("Waiting .hex file...")
    while(1):
        files_found = glob.glob(DOWNLOAD_FOLDER + '/*.hex')
        if len(files_found) > 1:
            print("WARNING: More than one file found. Go to your DOWNLOAD FOLDER and remove .hex files until you have only one.")
            break
        elif len(files_found) == 1:
            print("Detected .hex file. Loading it into Micro:Bit...")
            file_name = files_found[0].split("/")[-1]
            shutil.move(files_found[0], "{}/{}".format(DESTINATION_DISK, file_name))
            print("SUCCESS: .hex file loaded.")
            print("Waiting .hex file...")
        
except KeyboardInterrupt:
    print("\nAutoload stopped...")
