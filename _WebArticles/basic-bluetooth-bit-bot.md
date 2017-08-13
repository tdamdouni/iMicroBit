# Basic Bluetooth bit:bot

_Captured: 2017-08-12 at 21:07 from [ukbaz.github.io](https://ukbaz.github.io/howto/basic_bitbot.html)_

## Overview

Rather than programming the micro:bit on the bit:bot I decided to use the [Bluetooth](https://lancaster-university.github.io/microbit-docs/ble/profile/#gatt-services) profile for the micro:bit to control the pins remotely from a Raspberry Pi. I did a little video demo of it at:

## Equipment

  * [bit:bot](http://4tronix.co.uk/blog/?p=1490) : Learn how to program the bit:bot without using Bluetooth
  * [bit:bot](http://4tronix.co.uk/store/index.php?rt=product/product&product_id=588) : Where to buy the bit:bot
  * [Pi 3](https://shop.pimoroni.com/products/raspberry-pi-3) : Any Linux board should work although I used one of these

## Setting Up The micro:bit

Thanks to Bitty Software this is very easy as they have done a hex file for the micro:bit that exposes all of the Bluetooth services we need. This was created for their micro:bit blue app (you should check the app out as it is very good). You can download the hex file from their [webiste](http://www.bittysoftware.com/downloads.html). You will need to look for "Main Bluetooth services, pairing not required" link for the download. The loading of the hex file is standard for the micro:bit.

First time you start the micro:bit with this hex file it will get you to draw a circle. This is to calibrate the magnetometer. Once that is done you are done on the micro:bit.

## Setting Up the Raspberry Pi

This is a little bit more involved as you will require a newer version of BlueZ (the Linux Bluetooth stack) than comes as default with the Raspberry Pi. The full [instruction](https://github.com/ukBaz/python-bluezero/blob/master/docs/install_bluez.rst) are available in the Bluezero repository.

Make sure you take care to follow the instructions in the [note](https://github.com/ukBaz/python-bluezero/blob/master/docs/install_bluez.rst#how-to-config-and-compile-bluez-543-and-later) if you have a Raspberry Pi 3

## Getting the Bluezero microbit library

You will need to get the source of the library from <https://github.com/ukBaz/python-bluezero>

## Commands

CommandDescription

connect
Connect to the specified microbit for this instance

disconnect
Disconnect from the microbit

spin_right
Spin right wheel forward and left wheel backwards so bit:bot spins

spin_left
Spin left wheel forward and right wheel backwards so bit:bot spins

forward
Spin both wheels forward

reverse
Spin both wheels backwards

stop
Stop both wheels of the bit:bot

buzzer_on
Play the buzzer

buzzer_off
Stop the buzzer

## Example

` from time import sleep  
from bluezero import microbit  
bitbot = microbit.BitBot(name='micro:bit')  
bitbot.connect()  
bitbot.buzzer_on()  
sleep(0.5)  
bitbot.buzzer_off()  
sleep(0.5)  
bitbot.spin_right()  
sleep(1)  
bitbot.spin_left()  
sleep(1)  
bitbot.forward()  
sleep(1)  
bitbot.reverse()  
sleep(0.5)  
bitbot.stop()  
bitbot.disconnect()  
`
