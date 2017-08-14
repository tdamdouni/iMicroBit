let pos = 0
let speed = 0
let spinner: Image[] = []
basic.forever(() => {
    if (speed > 0) {
        speed = speed - 5
        if (speed < 0) {
            speed = 0
        }
        pos = pos + 1
        if (pos >= spinner.length) {
            pos = 0
        }
    }
    spinner[pos].showImage(0)
})
input.onGesture(Gesture.Shake, () => {
    speed = (speed + 1) * 2
})
spinner = [images.createImage(`
    . . # . .
    . . # . .
    . . # . .
    . # . # .
    # . . . #
    `), images.createImage(`
    . . . # .
    . . # . .
    # # # . .
    . . # . .
    . . . # .
    `), images.createImage(`
    # . . . #
    . # . # .
    . . # . .
    . . # . .
    . . # . .
    `), images.createImage(`
    . # . . .
    . . # . .
    . . # # #
    . . # . .
    . # . . .
    `)]
pos = 0
speed = 0
