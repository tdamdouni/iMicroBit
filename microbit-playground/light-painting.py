"""
Light-painting test. Results could be much better
with a proper motor instead of waving my hand in front of the camera.
"""

import microbit


# banner bitmap, exported from gimp to XPM+search/replace
banner = bytearray( "97579"
                    "  5  "
                    "  5  "
                    "95579"
                    "     "
                    "95579"
                    "9 5 9"
                    "9 5 9"
                    "9   9"
                    "     "
                    "95579"
                    "9    "
                    "9    "
                    "9    "
                    "     "
                    "75579"
                    "7    "
                    "7    "
                    "7    "
                    "     "
                    " 557 "
                    "9   9"
                    "9   9"
                    " 557 "
                    "     "
                    "     "
                    "     "
                    "     "
                    "99799"
                    "   7 "
                    "  5  "
                    "   7 "
                    "97579"
                    "     "
                    "9   9"
                    "97579"
                    "9   9"
                    "     "
                    " 757 "
                    "9   9"
                    "9   9"
                    " 7 7 "
                    "     "
                    "97579"
                    " 7  9"
                    " 7  9"
                    "9 57 "
                    "     "
                    " 755 "
                    "9   9"
                    "9   9"
                    " 757 "
                    "     "
                    " 7 7 "
                    "     "
                    "97579"
                    "9 5 9"
                    "9 5 9"
                    " 7 5 "
                    "     "
                    "9   9"
                    "97559"
                    "9   9"
                    "     "
                    "    9"
                    "97559"
                    "    9"
                    "     "
                    "     "
                    "9 559"
                    "     "
                    "     "
                    "     "
                    "     "
                    "     "
                    "     "
                    "     "
                    "     "
                    "     "
                    "     "
                    "     "
                    "     ")


# convert banner values to 0-9
for i, x in enumerate(banner):
    if x == ord(" "):
        x = 0
    else:
        x = x - ord("0")

    banner[i] = x


# calculate delays
number_of_columns = int(len(banner)/5)
exposure = 4.0 # seconds

frame_wait_ms = int(1000*exposure/number_of_columns)


# image that contains window of the banner
image = microbit.Image(5, 5)

# current banner ptr
banner_ptr = 0

banner_ptr_end = len(banner)

# main loop
while True:
    start_frame_ms = microbit.running_time()

    #  display current banner window
    ptr = banner_ptr

    for y in range(5):
        for x in range(5):
            image.set_pixel(y, 4-x, banner[ptr])
            ptr += 1

        # wrap around
        if ptr >= banner_ptr_end:
            ptr = 0

    # display the image
    microbit.display.show(image)

    # next banner row
    banner_ptr += 5
    if banner_ptr >= banner_ptr_end:
        banner_ptr = 0

    # wait for the next frame
    microbit.sleep(frame_wait_ms - (microbit.running_time()-start_frame_ms))
