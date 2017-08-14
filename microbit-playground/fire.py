"""
Fire simulator. Use buttons A+B to decrease/increase the flame.
"""

import microbit

class Fire:
    def __init__(self, blur_factor):
        self.set_blur_factor(blur_factor)

        #  pixel buffers (double buffering FTW!)
        self.pixels = bytearray(5*5)
        self.pixels_temp = bytearray(5*5)

        # image used to display pixels
        self.image = microbit.Image(5, 5)


    def set_blur_factor(self, blur_factor):
        """Update current blur_factor. Factor is clamped to [3,9]"""

        # make sure blur factor is at least 3 because we're averaging 3 pixels
        # also it doesn't make much sense to have blur > 9, the output looks the same
        self.blur_factor = min(9.0, max(3.0, blur_factor))

        print("Blur factor:", self.blur_factor)


    def show(self):
        """Update image from pixels and display it on the screen"""
        for y in range(5):
            for x in range(5):
                self.image.set_pixel(x, y, self.pixels[y*5+x])

        microbit.display.show(self.image)


    def step(self):
        """Update pixels, using pixels_temp"""
        # the basic algorithm is to
        # - shift pixels up
        # - generate random pixels in the empty (bottom) row
        # - blur everything

        # generate random first row in pixels
        # the row will get get discarded because of shifting up
        for x in range(5):
            self.pixels[x] = microbit.random(10)

        # blur pixels into pixels_temp taking
        # rows 0-3 from pixels rows 1-4 and
        # row 4 from random pixels row 0
        for y in range(5):
            for x in range(5):
                v =  self.get_pixel(x,   y)
                v += self.get_pixel(x-1, y)
                v += self.get_pixel(x+1, y)

                self.pixels_temp[y*5+x] = round(v/self.blur_factor)

        # now just swap pixel buffers
        self.pixels, self.pixels_temp = self.pixels_temp, self.pixels


    def get_pixel(self, x, y):
        """Read pixel from pixels or random buffer, offset by one row to achieve shifting up"""
        if 0 <= x < 5:
            if y == 4:
                # last row is read from the random row
                return self.pixels[x]
            else:
                # any other row is read from row+1 in pixels
                return self.pixels[5+5*y+x]
        else:
            # x is out of bounds
            return 0


blur_delta = 0.1
fire = Fire(4.3)

# main loop
while True:
    fire.step()
    fire.show()

    # check buttons - A to decrease the flame, B to increase
    if microbit.button_b.is_pressed():
        fire.set_blur_factor(fire.blur_factor-blur_delta)

    if microbit.button_a.is_pressed():
        fire.set_blur_factor(fire.blur_factor+blur_delta)
