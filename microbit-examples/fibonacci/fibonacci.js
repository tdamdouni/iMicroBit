let c = 0
let a = 1
let b = 1
input.onButtonPressed(Button.A, () => {
    c = a + b
    a = b
    b = c
    basic.clearScreen()
    basic.showNumber(c)
})
