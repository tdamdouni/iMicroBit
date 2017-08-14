let rand = 0
basic.showString("SHAKE ME!")
input.onGesture(Gesture.Shake, () => {
    rand = Math.random(6) + 1
    basic.showNumber(rand)
})
