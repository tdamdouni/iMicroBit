/**
 * @file arrow-1-spinning.js 
 * spins an arrow around eight points of the compass
 *
 * When trying to think of a fun project for the micro:bit 
 * A felt inspired by make something like a twister spinner, 
 * but obviously it will take a few steps to get there.
 * 
 * Here W put together the images, the delays and a 
 * variable to change the speed
 */
let speed = 0
basic.forever(() => {
    speed = 100
    basic.showLeds(`
        . . # . .
        . # # # .
        . . # . .
        . . # . .
        . . # . .
        `,speed)
    basic.showLeds(`
        . . # # #
        . . . # #
        . . # . #
        . # . . .
        # . . . .
        `,speed)
    basic.showLeds(`
        . . . . .
        . . . # .
        # # # # #
        . . . # .
        . . . . .
        `,speed)
    basic.showLeds(`
        # . . . .
        . # . . .
        . . # . #
        . . . # #
        . . # # #
        `,speed)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        . . # . .
        `,speed)
    basic.showLeds(`
        . . . . #
        . . . # .
        # . # . .
        # # . . .
        # # # . .
        `,speed)
    basic.showLeds(`
        . . . . .
        . # . . .
        # # # # #
        . # . . .
        . . . . .
        `,speed)
    basic.showLeds(`
        # # # . .
        # # . . .
        # . # . .
        . . . # .
        . . . . #
        `,speed)
})
