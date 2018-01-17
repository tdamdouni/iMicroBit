// RED LIGHT
pins.digitalWritePin(DigitalPin.P16, 0)
// AMBER LIGHT
pins.digitalWritePin(DigitalPin.P1, 0)
// GREEN LIGHT
pins.digitalWritePin(DigitalPin.P2, 1)
// RED MAN
pins.digitalWritePin(DigitalPin.P12, 1)
// GREEN MAN
pins.digitalWritePin(DigitalPin.P8, 0)
// WAIT LIGHT
pins.digitalWritePin(DigitalPin.P13, 0)
input.onButtonPressed(Button.A, () => {
    // WAIT LIGHT
    pins.digitalWritePin(DigitalPin.P13, 1)
    basic.pause(5000)
    // GREEN LIGHT
    pins.digitalWritePin(DigitalPin.P2, 0)
    // AMBER LIGHT
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(2000)
    // AMBER LIGHT
    pins.digitalWritePin(DigitalPin.P1, 0)
    // RED LIGHT
    pins.digitalWritePin(DigitalPin.P16, 1)
    basic.pause(3000)
    // WAIT LIGHT
    pins.digitalWritePin(DigitalPin.P13, 0)
    // RED MAN
    pins.digitalWritePin(DigitalPin.P12, 0)
    // GREEN MAN
    pins.digitalWritePin(DigitalPin.P8, 1)
    for (let i = 0; i < 25; i++) {
        music.playTone(Note.B5, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Quarter))
    }
    // GREEN MAN
    pins.digitalWritePin(DigitalPin.P8, 0)
    for (let i = 0; i < 2; i++) {
        basic.pause(500)
        // GREEN MAN
        pins.digitalWritePin(DigitalPin.P8, 1)
        basic.pause(500)
        // GREEN MAN
        pins.digitalWritePin(DigitalPin.P8, 0)
    }
    // RED LIGHT
    pins.digitalWritePin(DigitalPin.P16, 0)
    for (let i = 0; i < 7; i++) {
        basic.pause(500)
        // GREEN MAN
        pins.digitalWritePin(DigitalPin.P8, 1)
        // AMBER LIGHT
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.pause(500)
        // GREEN MAN
        pins.digitalWritePin(DigitalPin.P8, 0)
        // AMBER LIGHT
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    // RED MAN
    pins.digitalWritePin(DigitalPin.P12, 1)
    for (let i = 0; i < 2; i++) {
        basic.pause(500)
        // AMBER LIGHT
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.pause(500)
        // AMBER LIGHT
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    basic.pause(500)
    // GREEN LIGHT
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.pause(5000)
})
