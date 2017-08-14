import os
import time

print 'Starting programme'
time.sleep(2)

##### Record the slow motion video #####
# '-w' sets the width  # '-h' sets the height
# '-fps' sets the frames per second (90 maximum - for slow motion)
# 't' sets the time in milliseconds (30000 = 30 seconds)
# '-o' sets the output filename
 
print 'Recording started (30 seconds)'
os.system("raspivid -w 640 -h 480 -fps 90 -t 5000 -o slowmotion.h264")
 
print 'Recording complete. Please wait...'
time.sleep(2)
 
##### Convert the raw recorded video file to playable mp4 #####
# '-add' is the name of the raw video we want to convert
# The second file name is the output mp4 file (followed by '.mp4')
 
print 'Converting video. Please wait...'
os.system("MP4Box -add slowmotion.h264 slowmotion.mp4") 
 
print 'Video conversion complete'
time.sleep(2)
 
print 'Closing programme'
time.sleep(2)
