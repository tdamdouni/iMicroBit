# How Tall Is It?

_Captured: 2017-08-06 at 20:35 from [learn.adafruit.com](https://learn.adafruit.com/how-tall-is-it?view=all)_

![circuit_playground_diagram.png](https://cdn-learn.adafruit.com/assets/assets/000/036/654/large1024/circuit_playground_diagram.png?1476724338)

This is a fun and simple beginner project that turns the Circuit Playground into an inclinometer. An inclinometer is a device that can determine the angle of something relative to the horizontal. With this information and some right angle math, the height of tall objects can be determined. Don't worry, all the math is provided and use of a calculator is allowed.

  * ![circuit_playground_items.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/645/medium640/circuit_playground_items.jpg?1476714943)

  * 3 x AAA Batteries (NiMH work great!)

To build the inclinometer, you will need a few other items. A plastic tube is used to create a sight. This could be a drinking straw, the barrel of an old writing pen, or anything similar. Some rubber bands are used to hold the sight to the battery pack. Double backed tape provides a secure way of mounting the Circuit Playground to the battery pack.

  * ![circuit_playground_parts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/655/medium640/circuit_playground_parts.jpg?1476725003)

  * Plastic straw or other tube
  * Rubber bands
  * Double backed tape

If you are new to the Circuit Playground, you may want to first read these overview guides.

This project will use the Arduino IDE. Make sure you have added the board support for the Circuit Playground as well as installed the Circuit Playground library. **MUST DO BOTH. **This is covered in the guides linked above.

Since this project uses the accelerometer, let's start by exploring how it works and behaves. You can read some technical details in the [Lesson #0 Guide](https://learn.adafruit.com/../../../../circuit-playground-lesson-number-0/accelerometer). And for reference, here is where the accelerometer is located on the Circuit Playground.

![circuit_playground_accel.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/609/large1024/circuit_playground_accel.jpg?1476483106)

There is an example sketch included with the Circuit Playground library that we can use to play around with the accelerometer. It can be found in the following location:

**File -> Examples -> Adafruit Circuit Playground -> Hello_CircuitPlayground -> Hello_Accelerometer**

With this sketch loaded and running on the Circuit Playground, open the Serial Monitor.

**Tools -> Serial Monitor**

The current values from the accelerometer will be printed once a second.

![circuit_playground_accelerometer_serialmon.png](https://cdn-learn.adafruit.com/assets/assets/000/036/539/large1024/circuit_playground_accelerometer_serialmon.png?1476400806)

Try rotating the Circuit Playground around in various orientations and watch how the values change. The values are in units of m/s2 (meters per second squared). If you are doing this on planet Earth, you will see a value of 9.8 m/s2 showing up when an axis is aligned vertically. This value will be there even if the Circuit Playground is held still and does not move. More on this later.

Another way to watch the values of the accelerometer is to use the Serial Plotter. To do this, let's first modify the code slightly. The code below changes the format of the output to work with the Serial Plotter and increases the rate at which the values are displayed.
    
          1. float X, Y, Z;
      2. void setup() {
      3. Serial.begin(9600);
      4. void loop() {
      5.   X = CircuitPlayground.motionX();
      6.   Y = CircuitPlayground.motionY();
      7.   Z = CircuitPlayground.motionZ();
      8. Serial.print(X);
      9. Serial.print(",");
      10. Serial.print(",");

With this sketch loaded and running on the Circuit Playground, open the Serial Plotter.

**Tools -> Serial Plotter  
**

The accelerometer values will now be plotted like a strip chart as shown below. There should be 3 lines, one each for the X, Y, and Z values. Again, play around with rotating the Circuit Playground and watch the values change.

In the example below, the Circuit Playground was slowly rotated so that each axis aligned with the vertical, held there for a bit, and then rotated again. Finally, it was given a bit of a shake.

![circuit_playground_accelerometer_time_history1.png](https://cdn-learn.adafruit.com/assets/assets/000/036/540/large1024/circuit_playground_accelerometer_time_history1.png?1476400824)

![circuit_playground_earth_gravity.png](https://cdn-learn.adafruit.com/assets/assets/000/036/597/large1024/circuit_playground_earth_gravity.png?1476469038)

If we zoomed way in to just the local area where you might be, say standing outside with a Circuit Playground, it would look more like the figure below. The Earth is so big that close up it looks flat. Now all the lines are straight and point down.

![circuit_playground_local_gravity.png](https://cdn-learn.adafruit.com/assets/assets/000/036/598/large1024/circuit_playground_local_gravity.png?1476469054)

Just like gravity happens in a direction (down), acceleration also happens in a direction. In order to determine the direction, the Circuit Playground uses an XYZ coordinate system. For reference, there's a little diagram printed on the silk screen next to the accelerometer chip. A larger version is shown in the figure below. Z points out.

![circuit_playground_cp_coord_sys.png](https://cdn-learn.adafruit.com/assets/assets/000/036/599/large1024/circuit_playground_cp_coord_sys.png?1476469074)

So let's say you held the Circuit Playground at a little tilt angle as shown by the coordinate system below. Gravity, as shown by the blue arrow, will still point down. In this case, the accelerometer will sense some of it in the X direction and some of it in the Y direction. However, from the point of view of the Circuit Playground, it feels like it's accelerating in the direction of the green arrow. You can test this yourself by placing the Circuit Playground flat on your desk. The Z axis will be pointing up and gravity will be pointing down. However, the value returned from `motionZ()`is positive. The Circuit Playground feels like it's accelerating up off your desk!

![circuit_playground_rotated_with_gravity.png](https://cdn-learn.adafruit.com/assets/assets/000/036/600/large1024/circuit_playground_rotated_with_gravity.png?1476469090)

OK, now for the math. Sorry, but this is important. It's how we can use the accelerometer to measure angles and turn the Circuit Playground into an inclinometer. Also, rockets are built using math like this.

The same tilted axis and green arrow from above are shown again below. The red arrow represent the amount that the X axis will sense and returned by `motionX()`. Similarly, the blue arrow represents the amount the Y axis will sense and returned by `motionY()`. All together they form a special kind of triangle called a "right triangle", where one of the angles is a "right angle", which means it equals 90 degrees.

The tilt angle is shown in two places. The one on the left is what we are really interested in. However, it turns out it is the same as the one on the right, inside our right triangle. That's cool, since it let's us use `motionX()` and `motionY()` to compute the tilt angle.

![circuit_playground_rotated_with_components.png](https://cdn-learn.adafruit.com/assets/assets/000/036/601/large1024/circuit_playground_rotated_with_components.png?1476469115)

![circuit_playground_right_angle_math.png](https://cdn-learn.adafruit.com/assets/assets/000/036/602/large1024/circuit_playground_right_angle_math.png?1476469163)

The function **atan** is called the arctangent, or inverse tangent. It does the opposite of what the tangent function does. They are both part of a whole discipline of math called trigonometry. We will use the tangent function later when we go outside to measure the height of things. However, we will let either the Circuit Playground or a calculator do the math for us.

OK, a little more math. But don't worry, this is pretty much the same thing as the previous page, just with different values. There's our friend the right triangle shown again in the figure below. This time, we want to compute the **HEIGHT**. To do so, we use the tangent function and do a little rearranging. The resulting equation is shown below.

![circuit_playground_distance_height_math.png](https://cdn-learn.adafruit.com/assets/assets/000/036/656/large1024/circuit_playground_distance_height_math.png?1476725784)

So all we need to know is the **DISTANCE** and the **ANGLE** and we can compute the **HEIGHT**. The figure below shows how this would work for measuring the height of a tree.

![circuit_playground_diagram.png](https://cdn-learn.adafruit.com/assets/assets/000/036/607/large1024/circuit_playground_diagram.png?1476482410)

We will use the Circuit Playground to give us the **ANGLE** value. We will then use a calculator to compute the tangent of that angle. There are various ways to come up with the **DISTANCE** to the object, which you will see later in some example use cases.

Download and print the following worksheet to help guide you through the process. It also has the decoder ring for reading the angle value off the Circuit Playground.

  * ![circuit_playground_assy_step_1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/633/medium640/circuit_playground_assy_step_1.jpg?1476667575)

Draw a reference line 3/4" below the top of the battery pack. This will be used to help align the Circuit Playground when we mount it.

  * ![circuit_playground_assy_step_2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/634/medium640/circuit_playground_assy_step_2.jpg?1476667634)

Cut off a piece of double backed tape. About 1" x 1" is good.

  * ![circuit_playground_assy_step_3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/635/medium640/circuit_playground_assy_step_3.jpg?1476667707)

Apply the double backed tape to the battery pack.

  * ![circuit_playground_assy_step_4_align.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/640/medium640/circuit_playground_assy_step_4_align.jpg?1476672073)

When placing the Circuit Playground on the tape, try to keep the line centered in the 3.3V hole on the left and the GND hole on the right.

  * ![circuit_playground_assy_step_4.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/636/medium640/circuit_playground_assy_step_4.jpg?1476667765)

Apply the Circuit Playground to the double backed tape and press down firmly.

  * ![circuit_playground_assy_step_5.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/641/medium640/circuit_playground_assy_step_5.jpg?1476672175)

Attach the plastic straw to the top of the battery case using the rubber bands.

![circuit_playground_assy_final.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/646/large1024/circuit_playground_assy_final.jpg?1476719994)

> _Now let's load the inclinometer software._
    
          1. float X, Y, Z;
      2. ///////////////////////////////////////////////////////////////////////////////
      3. CircuitPlayground.setPixelColor(9, 255, 0, 0);
      4. ///////////////////////////////////////////////////////////////////////////////
      5. if ( (CircuitPlayground.leftButton()  == true) ||
      6. (CircuitPlayground.rightButton() == true) ) {
      7. for (int i=0; i<10; i=i+1) {
      8.       X = X + CircuitPlayground.motionX();
      9.       Y = Y + CircuitPlayground.motionY();
      10.       Z = Z + CircuitPlayground.motionZ();
      11.     Z = Z / 10.0;
      12.     angle = atan2(Y, X);
      13.     totalAccel = sqrt(X*X + Y*Y + Z*Z);
      14. if (abs(Z) > 1.0) {
      15. // Gravity (9.8 m/s^2) should be the only acceleration, but allow a small amount of motion.
      16. if (totalAccel > 10.0) {
      17. if (goodReading == true) {
      18. CircuitPlayground.setPixelColor(9, 0, 255, 0);
      19. CircuitPlayground.setPixelColor(9, 255, 0, 0);
      20. CircuitPlayground.setPixelColor(8, 0, 0, 255);
      21. CircuitPlayground.setPixelColor(8, 0, 0, 0);
      22. // Display angle magnitude, in degrees, on NeoPixels 0-7 as 8 bit value.
      23.     angleDisplay = uint8_t(abs(angle * 57.29578));
      24. for (int p=0; p<8; p=p+1) {
      25. if (angleDisplay & 0x01 == 1) {
      26. CircuitPlayground.setPixelColor(p, 255, 255, 255);
      27. CircuitPlayground.setPixelColor(p, 0, 0, 0);

With the inclinometer sketch loaded and running on the Circuit Playground, you can now use it to make angle measurements. The general steps are:

  1. Sight in the top of the object through the plastic tube.
  2. Hold the Circuit Playground upright and still, then press either button to take a reading.
  3. The results will be shown on the NeoPixels #0-#8.
  4. If the #9 NeoPixel is red, try again. The Circuit Playground was either not upright or there was too much motion.
![circuit_playground_tilt.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/690/large1024/circuit_playground_tilt.jpg?1476757919)

> _Reading the Angle_

If there were some kind of text display on the Circuit Playground, we could use that to display the angle directly. However, there isn't one, so we need to do something else. The approach taken here is to use the first 8 NeoPixels, #0-#7, to indicate the magnitude of the angle. The sign (+ or -) is indicated on the #8 NeoPixel.

The [worksheet](https://cdn-learn.adafruit.com/assets/assets/000/036/608/original/How_Tall_Is_It_Worksheet.pdf) includes the following diagram to help determine the angle from the sequence of lit NeoPixels.

![circuit_playground_decoder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/691/large1024/circuit_playground_decoder.jpg?1476758082)

To figure out the angle, simply add up each number shown for each NeoPixel that is lit. If the NeoPixel is not lit, do not add in that number.

For example, if these NeoPixels were lit (remember numbering starts with #0):

**#1, #3, and #5**

We would add up the corresponding numbers:

**2 + 8 + 32 = 42**

To come up with the value **42**. If the #8 NeoPixel had been lit blue, then the value would have been **-42**.

![circuit_playground_space_needle_1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/647/large1024/circuit_playground_space_needle_1.jpg?1476722370)

  * ![circuit_playground_dist_maps_1.png](https://cdn-learn.adafruit.com/assets/assets/000/036/648/medium640/circuit_playground_dist_maps_1.png?1476722445)

Move mouse pointer to the location of the object (in this case, the Space Needle) and right click to bring up menu. Select **Measure distance**.

  * ![circuit_playground_dist_maps_2.png](https://cdn-learn.adafruit.com/assets/assets/000/036/649/medium640/circuit_playground_dist_maps_2.png?1476722532)

A small round circle will be placed to indicate the starting location. This can be relocated by grabbing and moving it with the mouse.

  * ![circuit_playground_dist_maps_3.png](https://cdn-learn.adafruit.com/assets/assets/000/036/650/medium640/circuit_playground_dist_maps_3.png?1476722632)

Click on the location where you are taking the angle measurement. A line will be drawn between the two points and the distance will be shown. Rounding to the nearest foot is fine, so in this case **780 ft**.

![circuit_playground_space_needle_2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/651/large1024/circuit_playground_space_needle_2.jpg?1476722827)

![circuit_playground_space_needle_3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/684/large1024/circuit_playground_space_needle_3.jpg?1476752372)

Now we can use the [worksheet](https://cdn-learn.adafruit.com/assets/assets/000/036/608/original/How_Tall_Is_It_Worksheet.pdf) to determine what angle is being indicated. In this case:

**1 + 4 + 32 = 37 degrees**

Then use a calculator to get the tangent of this angle:

**tan (37 deg) = 0.7536**

We determined our distance was 780 feet above, so just need to multiply to get the final answer:

**780 x 0.7536 = 587.808**

Let's just call it **588 feet**.

![circuit_playground_space_needle_4.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/685/large1024/circuit_playground_space_needle_4.jpg?1476752774)

> _The actual height of the Space Needle is 605 feet. So our reading was off by 17 feet. Oh well, not perfect, but not bad for a plastic straw and some rubber bands._

![circuit_playground_tree_1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/652/large1024/circuit_playground_tree_1.jpg?1476723312)

![circuit_playground_tree_2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/653/large1024/circuit_playground_tree_2.jpg?1476723400)

![circuit_playground_tree_3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/686/large1024/circuit_playground_tree_3.jpg?1476753445)

Now we can use the [worksheet](https://cdn-learn.adafruit.com/assets/assets/000/036/608/original/How_Tall_Is_It_Worksheet.pdf) to determine what angle is being indicated. In this case:

**1 + 8 + 16 = 25 degrees**

Then use a calculator to get the tangent of this angle:

**tan (25 deg) = 0.4663**

We determined our distance was 44 paces above, so just need to multiply to get the final answer:

**44 x 0.4663 = 20.5  
**

Let's just call it **21 paces**.

![circuit_playground_tree_4.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/687/large1024/circuit_playground_tree_4.jpg?1476753579)

Great. But how tall is that? If you take this approach you will need to determine how big your paces are. You can place a tape measure on the ground and step next to it to get an idea. I came up with about 3 feet for my pace, which gives:

**3 feet/pace x 21 paces = 63 feet**

The tree is about **63 feet** tall.

The following are some questions related to this project along with some suggested code challenges. The idea is to provoke thought, test your understanding, and get you coding!

While the inclinometer sketch provided works, there is room for improvement and additional features. Have fun playing with the provided code to see what you can do with it.

  * Why is it important for the Circuit Playground to be upright and held still?
  * Are there any issues with making the angle reading at eye level?
  * Would this work on the moon?
  * Would this work in space, for example, on the International Space Station?
  * Add an audio cue to indicate if the measurement is good or bad.
  * Improve the resolution of the indicated angle measurement.
  * Incorporate all the math into the Circuit Playground so it provides height directly.
