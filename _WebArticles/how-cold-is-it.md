# How Cold Is It?

_Captured: 2017-08-06 at 20:39 from [learn.adafruit.com](https://learn.adafruit.com/how-cold-is-it?view=all)_

![temperature_banner.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/959/large1024/temperature_banner.jpg?1478015461)

This is a fun and simple beginner project that turns the Circuit Playground into a cold temperature indicator. It uses the on board temperature sensor to read the current temperature. The coldest temperature measured is indicated on the NeoPixels.

An additional sketch is provided which turns the Circuit Playground into a temperature data logger.

  * ![circuit_playground_items.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/733/medium640/circuit_playground_items.jpg?1477091448)

  * 3 x AAA Batteries (NiMH work great!)

If you are new to the Circuit Playground, you may want to first read these overview guides.

This project will use the Arduino IDE. Make sure you have added the board support for the Circuit Playground as well as installed the Circuit Playground library. **MUST DO BOTH. **This is covered in the guides linked above.

Since this project uses the temperature sensor, let's start by exploring how it works and behaves. You can read some technical details in the [Lesson #0 Guide](https://learn.adafruit.com/../../../../circuit-playground-lesson-number-0/temperature-sensor). And for reference, here is where the temperature sensor is located on the Circuit Playground.

![circuit_playground_temp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/734/large1024/circuit_playground_temp.jpg?1477091915)

There is an example sketch included with the Circuit Playground library that we can use to play around with the temperature sensor. It can be found in the following location:

**File -> Examples -> Adafruit Circuit Playground -> Hello_CircuitPlayground -> Hello_Temperature**

With this sketch loaded and running on the Circuit Playground, open the Serial Monitor.

**Tools -> Serial Monitor**

The current value from the temperature sensor will be printed once a second.

![circuit_playground_Screenshot_from_2016-10-29_10-37-32.png](https://cdn-learn.adafruit.com/assets/assets/000/036/881/large1024/circuit_playground_Screenshot_from_2016-10-29_10-37-32.png?1477763037)

Try breathing on the temperature sensor. You should see the value increase, and then slowly decrease when you stop. Now try holding your finger on the sensor. Did the temperature go up?

Another way to watch the values of the temperature sensor is to use the Serial Plotter. To do this, let's first modify the code slightly. The code below changes the format of the output to work with the Serial Plotter and increases the rate at which the values are displayed.
    
          1. void setup() {
      2. Serial.begin(9600);
      3. void loop() {
      4.   tempC = CircuitPlayground.temperature();
      5.   tempF = CircuitPlayground.temperatureF();
      6. Serial.println(tempF);

![circuit_playground_temperature_serial_plotter.png](https://cdn-learn.adafruit.com/assets/assets/000/036/882/large1024/circuit_playground_temperature_serial_plotter.png?1477763914)

![circuit_playground_simple_C.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/913/large1024/circuit_playground_simple_C.jpg?1477934146)

When you retrieve the Circuit Playground, it will show the minimum temperature seen on the NeoPixels. You can select either Fahrenheit (+, left) or Celsius (-, right) using the slide switch. Then, use the diagram below to determine the value.

![circuit_playground_decoder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/912/large1024/circuit_playground_decoder.jpg?1477931911)

> _You come up with the temperature by adding up the value shown for each NeoPixel that is lit. For example:_

  * ![circuit_playground_simple_C2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/922/medium640/circuit_playground_simple_C2.jpg?1477940077)

  * ![circuit_playground_simple_F2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/923/medium640/circuit_playground_simple_F2.jpg?1477940106)

Use these to change whether the log buffer wraps when full and how often to measure the temperature as follows:

  * `LOG_WRAP`: If true, the log buffer will wrap when full and start overwriting older data. If false, logging will stop when the log buffer is full.
  * `LOG_RATE`: Sets how often the temperature is measured and saved to the log. The value is in milliseconds.

With the slide switch in the left (+) position, the Circuit Playground is in logging mode. The NeoPixels on the left half will be lit green to indicate this mode. To control logging, use the two push buttons as follows:

  * **Left Button**: Press to start/stop logging. The #2 NeoPixel, next to the left button, will change to show stopped (red) or running (green).
  * **Right Button + Left Button**: Press both together to clear the log buffer and reset logging. All NeoPixels will temporarily light red.
![circuit_playground_log_mode_1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/916/large1024/circuit_playground_log_mode_1.jpg?1477936492)

  * ![circuit_playground_log_mode_2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/919/medium640/circuit_playground_log_mode_2.jpg?1477936887)

  * #2 NeoPixel is green.
  * Red LED is blinking.
  * 4 of 5 white lights on right are lit indicating log space used.

  * ![circuit_playground_log_mode_3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/920/medium640/circuit_playground_log_mode_3.jpg?1477936996)

  * #2 NeoPixel is red.
  * Red LED is not blinking.
  * All lights on right red, indicating full buffer.

  * ![circuit_playground_log_mode_4.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/921/medium640/circuit_playground_log_mode_4.jpg?1477937096)

**Log is running. Buffer is full. (wrap on)**

  * #2 NeoPixel is green.
  * Red LED is blinking.
  * All lights on right red, indicating full buffer.
  * White light indicates current wrap position.
![circuit_playground_readout_mode_1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/918/large1024/circuit_playground_readout_mode_1.jpg?1477936636)

  * ![circuit_playground_log_example_1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/924/medium640/circuit_playground_log_example_1.jpg?1477950824)

Press the left button and place in freezer.

  * ![circuit_playground_log_example_2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/925/medium640/circuit_playground_log_example_2.jpg?1477950855)

Lights on left are all green. Red LED should blink indicating logging. Buffer is starting to fill.

  * ![circuit_playground_log_example_3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/926/medium640/circuit_playground_log_example_3.jpg?1477950955)

Lights on right are all red indicating the log buffer is full. However, since wrapping was enabled, it is still logging. Red LED is flashing. White NeoPixel is progressing through buffer.

  * ![circuit_playground_log_example_4.jpg](https://cdn-learn.adafruit.com/assets/assets/000/036/927/medium640/circuit_playground_log_example_4.jpg?1477951039)

Remove from freezer. Move slide switch to the right (-) position for Readout Mode. Attach to computer with USB cable.

**Tools -> Serial Plotter**

Use the right button to select one of the plotting output modes: **Celsius Plot** or **Fahrenheit Plot**. Then press the left button and the data should be plotted.

In the example below, the Fahrenheit Plot option was used.

![circuit_playground_temperature_serial_plotter2.png](https://cdn-learn.adafruit.com/assets/assets/000/036/928/large1024/circuit_playground_temperature_serial_plotter2.png?1477951355)

![circuit_playground_log_example_6.png](https://cdn-learn.adafruit.com/assets/assets/000/036/929/large1024/circuit_playground_log_example_6.png?1477951599)

> _You can also dump the entire contents in a tabular format using one of the Table output options. This is mainly meant to be used for downloading the data as described in the next section._

![circuit_playground_log_example_7a.png](https://cdn-learn.adafruit.com/assets/assets/000/036/930/large1024/circuit_playground_log_example_7a.png?1477951774)

![circuit_playground_log_example_7b.png](https://cdn-learn.adafruit.com/assets/assets/000/036/931/large1024/circuit_playground_log_example_7b.png?1477951826)

![circuit_playground_log_example_7c.png](https://cdn-learn.adafruit.com/assets/assets/000/036/932/large1024/circuit_playground_log_example_7c.png?1477951901)

Save the file, giving it a name like **data.csv** or similar. You can now open that file in other applications, like a spreadsheet, for further analysis and plotting.

![circuit_playground_log_example_7d.png](https://cdn-learn.adafruit.com/assets/assets/000/036/933/large1024/circuit_playground_log_example_7d.png?1477951966)

The following are some questions related to this project along with some suggested code challenges. The idea is to provoke thought, test your understanding, and get you coding!

While the sketch provided works, there is room for improvement and additional features. Have fun playing with the provided code to see what you can do with it.

  * Which is colder, the refrigerator or the freezer?
  * How cold is it outside?
  * Change the Cold Temperature Display into a Warm Temperature Display.
  * Add an audio alarm to the Cold Temperature Display that sounds when the temperature goes below freezing.
