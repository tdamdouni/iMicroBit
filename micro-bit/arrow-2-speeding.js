/**
 * @file arrow-1-speeding.js 
 * variable speed spinning arrow around eight points of the compass
 *
 * Taking small steps towards a twister spinner, 
 * this follows on from  arrow-1-spinning.js 
 * 
 * A converted the arrow images into a single bigimage but provided two 
 * - inserting a small one that would allow block mode to be used
 * 
 * Then W built the logic code to vary the speed with buttons
 */
let ArrowImages: Image = null
let speed = 0
basic.forever(() => {
    for (let item = 0; item <= 7; item++) {
        ArrowImages.showImage(item * 5)
        basic.pause(speed)
        if (input.buttonIsPressed(Button.A)) {
            speed += 10
        } else {
            if (input.buttonIsPressed(Button.B)) {
                speed += -10
            }
        }
    }
})
speed = 100

ArrowImages = images.createBigImage(`
    . . # . .   . . # # #
    . # # # .   . . . # #
    . . # . .   . . # . #
    . . # . .   . # . . .
    . . # . .   # . . . .
    `)


ArrowImages = images.createBigImage(`
    . . # . .   . . # # #   . . . . .   # . . . .   . . # . .   . . . . #   . . . . .   # # # . .
    . # # # .   . . . # #   . . . # .   . # . . .   . . # . .   . . . # .   . # . . .   # # . . .
    . . # . .   . . # . #   # # # # #   . . # . #   . . # . .   # . # . .   # # # # #   # . # . .
    . . # . .   . # . . .   . . . # .   . . . # #   . # # # .   # # . . .   . # . . .   . . . # .
    . . # . .   # . . . .   . . . . .   . . # # #   . . # . .   # # # . .   . . . . .   . . . . #
    `)
