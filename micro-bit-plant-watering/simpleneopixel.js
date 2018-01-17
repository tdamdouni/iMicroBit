input.onButtonPressed(Button.A, () => {
    neopixel.create(DigitalPin.P0, 32, NeoPixelMode.RGB).showRainbow(1, 360)
})
