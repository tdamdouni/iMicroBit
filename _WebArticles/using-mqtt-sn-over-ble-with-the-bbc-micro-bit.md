# Using MQTT-SN over BLE with the BBC micro:bit

_Captured: 2017-09-01 at 21:12 from [blog.benjamin-cabe.com](https://blog.benjamin-cabe.com/2017/01/16/using-mqtt-sn-over-ble-with-the-bbc-microbit)_

![](https://blog.benjamin-cabe.com/wp-content/uploads/2017/01/xmqtt-sn-microbit-1038x576.jpg.pagespeed.ic.8fT1gfbaG6.jpg)

The [micro:bit](http://microbit.org/) is one of the best IoT prototyping platforms I've come across in the past few months.

![](https://blog.benjamin-cabe.com/wp-content/uploads/2017/01/xmicrobit-hardware.png.pagespeed.ic.jOj8m0JBA8.png)

The main MCU is a **Nordic nRF51822** with 16K RAM and 256K Flash. A Freescale KL26Z is used for conveniently implementing a USB interface as well as a mass storage driver so as deploying code onto the micro:bit is as simple as directly copying a .hex file over USB (if your familiar with the mbed ecosystem, this will sound familiar :-)).

The board is packed with all the typical sensors and actuators you need for prototyping an IoT solution: accelerometer, compass, push buttons, an LED matrix, … What's really cool, is the built-in BLE support, combined with the battery connector, making it really easy to have a tetherless, low-power [1](https://blog.benjamin-cabe.com/2017/01/16/using-mqtt-sn-over-ble-with-the-bbc-microbit), IoT testing device.

**So how does one take the micro:bit and turn it into an IoT device?** Since there is no Internet connectivity, you need to rely on some kind of gateway to bridge the constrained device that is the micro:bit to the Internet. You can of course implement your own protocol to do just that, but then you have to basically reimplement the wheel. That's the reason why I thought the **micro:bit would be ideal to experiment with MQTT-SN**.

You can [jump directly to the video tutorial at the end of the post](https://blog.benjamin-cabe.com/2017/01/16/using-mqtt-sn-over-ble-with-the-bbc-microbit), and come back later for more in-depth reading.

## What is MQTT-SN and why you should care

If I were to over simplify things, I would just say that MQTT-SN (which stands for "MQTT for Sensor Networks", by the way) is an adaptation of the MQTT protocol to deal with constrained devices, both from a footprint/complexity standpoint, and to adapt to the fact constrained devices may not have TCP/IP support.

MQTT-SN is designed so as to **make the packets as small as possible**. An example is the fact that an MQTT-SN client registers the topic(s) it wishes to us against the server, this way further PUBLISH or SUBSCRIBE exchanges only have to deal with a 2-byte long ID, as opposed to a possibly very long UTF-8 string.

Like I said before, you really don't want to reimplement your own protocol, and using MQTT-SN just makes lot of sense since it bridges very naturally to good ol' MQTT.

## Setting up an MQTT-SN client on the micro:bit

The MQTT-SN supports the BLE UARTService from Nordic, that essentially mimics a classical UART by means of two BLE characteristics, for RX and TX. This is what we'll use as our communication channel.

The Eclipse Paho project provides an [MQTT-SN embedded library](https://github.com/eclipse/paho.mqtt-sn.embedded-c) that turns out to be really easy to use. It allows you to serialize and deserialize MQTT-SN packets, the only remaining thing to do is for you to effectively transmit them (send or receive) over your communication channel - BLE UART in our case.

In order to show you how simple the library is to use, here's an example of how you would issue a CONNECT:

Now what's behind the `transport_sendPacketBuffer` and `transport_getdata` functions? You've guess correctly, this is where either send or read a buffer to/from the BLE UART.  
Using the micro:bit UART service API, the code for `transport_getdata` is indeed very straightforward:

12345
`int` `transport_getdata(unsigned ``char``* buf, ``int` `count)``{``int` `rc = uart-&amp;amp;amp;gt;read(buf, count, ASYNC);``return` `rc;``}`

You can find the complete code for publishing the micro:bit acceloremeter data over BLE [on my Github](https://github.com/kartben/microbit-mqttsn-ble). Note that for the sake of simplifying things, I've disabled Bluetooth pairing so as connecting to a BLE/MQTT-SN gateway just works out of the box.

## MQTT-SN gateway

There are a few MQTT-SN gateways available out there, and you should feel free to use the one that floats your boat. Some (most?) MQTT-SN gateways will also behave as regular MQTT brokers so you won't necessarily have to bridge the MQTT-SN devices to MQTT strictly speaking, but rather directly use the gateway as your MQTT broker.  
For my tests, I've been pretty happy with **RSMB**, an [Eclipse Paho](https://eclipse.org/paho) component, that you can [get from Github](https://github.com/eclipse/mosquitto.rsmb).

The [README](https://github.com/eclipse/mosquitto.rsmb/blob/master/README.md) of the project is pretty complete and you should be able to have your RSMB broker compiled in no time. The default configuration file for RSMB should be named `broker.cfg` (you can specify a different configuration file on the command line, of course).  
Below is an example of the configuration file so as RSMB behaves as both a good ol' MQTT broker, but also an MQTT-SN gateway, bridged to iot.eclipse.org's MQTT sandbox broker. Note that in my example I only care about publishing messages, so the bridge is configured in `out` mode, meaning that messages only flow from my MQTT-SN devices to iot.eclipse.org, and not the other way around. Your mileage may vary if you also want your MQTT-SN devices to be able to subscribe to message, in which case the bridging mode should be set to `both`

broker.cfg

1234567891011121314
`# will show you packets being sent and received``trace_output protocol``# MQTT listener``listener 1883 INADDR_ANY mqtt``# MQTT-S listener``listener 1884 INADDR_ANY mqtts``# QoS 2 MQTT-S bridge``connection mqtts``protocol mqtt``address 198.41.30.241:1883``topic ``# out`

## Bridging the BLE device(s) to the MQTT-SN gateway

Now there is still one missing piece, right? We need some piece of software for forwarding the messages coming from the BLE link, to the MQTT-SN gateway.

I've [adapted an existing Node.js application that does just that](https://github.com/kartben/ble-uart-to-udp). For each BLE device that attaches to it, it creates a UDP socket to the MQTT-SN gateway, and transparently routes packets back and forth. When the micro:bit "publishes" an MQTT-SN packet, it is just as if it were directly talking to the MQTT-SN gateway.

The overall architecture is as follows:

![](https://blog.benjamin-cabe.com/wp-content/uploads/2017/01/619x373xmqtt-sn-microbit-overview-1024x617.png.pagespeed.ic.66emkaXOrQ.png)

Note that it would be more elegant (and also avoid some nasty bugs, actually [2](https://blog.benjamin-cabe.com/2017/01/16/using-mqtt-sn-over-ble-with-the-bbc-microbit)) to leverage MQTT-SN's encapsulation mechanism so as to make the bridge even more straightforward, and not have to maintain one UDP socket per BLE device. To quote the [MQTT-SN specification](http://mqtt.org/new/wp-content/uploads/2009/06/MQTT-SN_spec_v1.2.pdf):

> The forwarder simply encapsulates the MQTT-SN frames it receives on the wireless side and forwards them unchanged to the GW; in the opposite direction, it decapsulates the frames it receives from the gateway and sends them to the clients, unchanged too.

Unfortunately RSMB does not support encapsulated packets at this point, but you can rely on this fork if you want to use encapsulation: <https://github.com/MichalFoksa/rsmb>.

## Visualizing the data: mqtt-spy to the rescue!

Like in my [previous article about Android Things](https://blog.benjamin-cabe.com/2016/12/16/using-mqtt-and-eclipse-paho-in-android-things), I used [mqtt-spy](https://github.com/eclipse/paho.mqtt-spy) to visualize the data coming from the sensors.

Note that publishing sensor data in JSON might not be the best idea in production: the MTU of a BLE packet is just 20 bytes. Those extra curly braces, commas, and double quotes are as many bytes you won't be able to use for your MQTT payload. You may want to look at something like [CBOR](http://cbor.io/) for creating small, yet typed, binary payloads.  
However, JSON is of course pretty convenient since there's a plethora of libraries out there that will allow you to easily manipulate the data…

Using mqtt-spy, it's very easy to visualize the values we're collecting from the accelerometer of the micro:bit, either in "raw" form, or on a chart, using mqtt-spy's ability to parse JSON payloads.

![](https://blog.benjamin-cabe.com/wp-content/uploads/2017/01/mqtt-sn-microbit-mqttspy1-300x219.png)

![](https://blog.benjamin-cabe.com/wp-content/uploads/2017/01/mqtt-sn-microbit-mqttspy2-300x238.png)

## Video tutorial and wrap-up

I've wanted to give MQTT-SN a try for a long time now, and I'm really happy I took the time to do so. All in all, I would summarize my findings as follow:

  * **The Eclipse Paho MQTT-SN embedded client just works!** Similarly to the MQTT embedded client, it is very easy to take it and port it to your embedded device, and no matter what actual transport layer you are using (Bluetooth, Zigbee, UDP, …), you essentially just have to provide an implementation of "transport_read" and "transport_write".
  * You may want to be careful when doing things like "UART over BLE". The main point of BLE is that it's been designed to be really low-power, so if you tend to overly communicate or to remain paired with the gateway all the time, you will likely kill your battery in no time!
  * The NRF5x series from Nordic is very widely available on the market, so it would be really interesting to run a similar MQTT-SN stack on other devices than the micro:bit, therefore demonstrating how it truly enables interoperability. If you build something like this, I really want to hear from you!
  * Although it's true that there are not quite as many MQTT-SN libraries and gateways available out there as there are for MQTT, **the protocol is pretty straightforward and that shouldn't be preventing you from giving it a try!**
