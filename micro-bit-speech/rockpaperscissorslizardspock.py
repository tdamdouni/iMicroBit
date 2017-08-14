let Sheldon = 0
input.onGesture(Gesture.Shake, () => {
    Sheldon = Math.random(5)
    if (Sheldon == 0) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    }
    if (Sheldon == 1) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
    if (Sheldon == 2) {
        basic.showLeds(`
            . # # # .
            . # . # .
            . # . # .
            . # . # .
            . # # # .
            `)
    }
    if (Sheldon == 3) {
        basic.showLeds(`
            # # # . .
            # # . # .
            # . . # #
            # # # . .
            # # . . .
            `)
    }
    if (Sheldon == 4) {
        basic.showLeds(`
            # # . # #
            # # . # #
            # # . # #
            # # # # #
            # # # # #
            `)
    }
})
input.onButtonPressed(Button.A, () => {
    game.addScore(1)
    basic.showString("WINS:")
    basic.showNumber(game.score())
})
input.onButtonPressed(Button.B, () => {
    game.addScore(-1)
    basic.showString("LOSSES:")
    basic.showNumber(game.score())
})
