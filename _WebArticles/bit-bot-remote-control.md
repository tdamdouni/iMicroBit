# bit:bot Remote Control

_Captured: 2017-09-04 at 21:46 from [ukbaz.github.io](https://ukbaz.github.io/howto/bitbotRemoteControl.html)_

> With a little help from [@bluetooth_mdw](https://twitter.com/bluetooth_mdw) I now have a remote control for the [@4tronix_uk](https://twitter.com/4tronix_uk) [#bitbot](https://twitter.com/hashtag/bitbot?src=hash) [pic.twitter.com/oYushM2gYW](https://t.co/oYushM2gYW)

Martin Woolley has written a great little app for controlling a micro:bit controlled buggy and I wondered if it could be used for driving the bit:bit from 4tronix. After a brief exchange of messages with Martin it became clear that there is nothing that needs to be changed in the app to be used with different robots, it is just the code on the micro:bit that needs to change.

This allows you to use the correct pin numbers for your robot but also change what the buttons do on the Bitty Software controller.

Martin has documented how he had done it for the original buggy:

## On The Phone

There is an App for Android and iOS that can be downloaded from:

**[Note: Since this page was originally created Bitty Software discontinued the free app and now only offer a paid for app. Some background on the decision is on their [blog](http://bluetooth-mdw.blogspot.co.uk/2017/07/hello-bitty-controller-goodbye-bitty.html)]**

Below is a screen grab of what the app looks like. I've annotated it with the names used in PXT to refer to the buttons:

![dpad#.jpg](https://ukbaz.github.io/asset/bitbot_remote/image00.jpg)

## On The micro:bit

The code for the micro:bit can be done with C++ or with PXT. I choose to go with the PXT editor.

## Events

The app works by sending 'events' to the micro:bit. We have to write code for the micro:bit to interpret those events and make the correct things happen.

It is always nice to have a message display on startup so you know you have the correct program loaded up. E.g.

### On Bluetooth Connection

Set pins to a known state and display a message so you know the connection has been successful

![](https://ukbaz.github.io/asset/bitbot_remote/image08.png)

> _On Bluetooth Disconnection_

When we disconnect then make sure everything is off and send a message to the user

![](https://ukbaz.github.io/asset/bitbot_remote/image07.png)

> _Buzzer_

We can capture when buttons are pressed and released. We will make the buzzer turn on when button 4 is pressed and turn off when button 4 is released.

When button 4 is pressed we do an analog write to pin 14 to make the buzzer sound.

We are going to code up that when button A is pressed we will move forward and when it is released the robot will stop. This is not the only way of doing it but a nice straight forward way for this tutorial.

To move forward we need to set pins 1 and 0 high while pins 12 and 8 are low. We do this when the button A is pressed and all pins are low when the button is released.

![](https://ukbaz.github.io/asset/bitbot_remote/image04.png)

> _Move Backwards_

Button B is going to move the robot backwards and to do this we reverse which pins are high. This means that pins 12 and 8 are high. Same as last time, to stop the robot on releasing the button we set all pins to low.

![](https://ukbaz.github.io/asset/bitbot_remote/image03.png)

> _Spin Left_

Button C is going to make the robot spin left. We do this by making only the right motor move forwards.

![](https://ukbaz.github.io/asset/bitbot_remote/image09.png)

> _Spin Right_

Finally button D is going to spin the robot right and we do this by just rotating the left motor forwards.

![](https://ukbaz.github.io/asset/bitbot_remote/image01.png)

> _Project Settings_

We are going to change the default project settings so that we don't need to pair our phone with the micro:bit:

## What Next

There are a number of ways that this solution could be improved. We could improve the logic so that a couple buttons could be used along with sending analog values to the pins. This would allow better steering etc.

## license
