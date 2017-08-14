input.onButtonPressed(Button.A, () => {
    basic.showLeds(`
        . # # # .
        # . . . .
        # . # # .
        # . . # .
        . # # # .
        `)
    music.playTone(Note.G, music.beat(BeatFraction.Breve))
})
input.onButtonPressed(Button.B, () => {
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # .
        `)
    music.playTone(Note.C, music.beat(BeatFraction.Breve))
})
input.onPinPressed(TouchPin.P1, () => {
    basic.showLeds(`
        # # # # .
        # . . . .
        # # # . .
        # . . . .
        # # # # .
        `)
    music.playTone(Note.E, music.beat(BeatFraction.Breve))
})
input.onPinPressed(TouchPin.P2, () => {
    basic.showLeds(`
        . . # . .
        . # . # .
        # # # # #
        # . . . #
        # . . . #
        `)
    music.playTone(Note.A, music.beat(BeatFraction.Breve))
})
