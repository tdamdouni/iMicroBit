let mode = 1
let neo = neopixel.create(DigitalPin.P0, 8, NeoPixelMode.RGB)
neo.setBrigthness(20)
input.onButtonPressed(Button.A, () => {
    mode = 1
})
input.onButtonPressed(Button.B, () => {
    mode = -1
})
neo.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
neo.show()
basic.forever(() => {
    neo.rotate(mode)
    neo.show()
    basic.pause(100)
})

