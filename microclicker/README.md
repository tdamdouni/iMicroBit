# micro:clicker
![npm version 1.0.6](https://img.shields.io/npm/v/microclicker.svg)

_🔎🖱️ use the bbc micro:bit as a slide clicker_

*here's a vid of it working: https://youtu.be/3ho0ime_nwQ*

## installation

#### 1. [follow instructions to install `bbc-microbit`](https://github.com/sandeepmistry/node-bbc-microbit#prerequisites)
> Make sure to follow the instructions for `noble` too.

#### 2. install microclicker globally with npm
```
npm install microclicker --global
```

## usage

Use the command `microclicker` to start scanning for micro:bits. You should see something like the following:

```
$ microclicker
🔎🖱  micro:clicker

🔮  Scanning for micro:bit...
    Hold your micro:bit level!

🤖  micro:bit found!

🔌  Connecting to micro:bit
🤖  micro:bit connected!
     ➡️  Press right arrow to move right.
     ⬅️  Press left arrow to move left.
   ⬅️ ➡️ ️ Hold both buttons to disconnect.
    🔀  Tilt up to show current progress in slides.
```

> i'm also using the [mi:power accessory](https://www.amazon.co.uk/MI-power-board-BBC-micro/dp/B01JP47T46) to make it more compact and a buzzer sound for fun

## development

### installation

1. [follow instructions to install `bbc-microbit`](https://github.com/sandeepmistry/node-bbc-microbit#prerequisites)
2. install dependancies `npm install` or `yarn`

### usage

1. turn microbit off
2. run `sudo node main.js` (_you'll probably need `sudo` to get access to bluetooth_)
3. turn microbit on
4. you should see a pattern

> press buttons to move slides, you should see a counter to help reflect your position in your slides. turn the microbit upside down to reset the counter
