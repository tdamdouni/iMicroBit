let cooldown = 0
let isExploding = 0
basic.forever(() => {
    if (cooldown > 0 && isExploding == 0) {
        cooldown += -1
        basic.showNumber(cooldown)
        basic.pause(100)
    }
})
radio.onDataPacketReceived(({receivedNumber, signal}) => {
    if (cooldown == 0 && signal > -55) {
        cooldown = 10
        isExploding = 1
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . # # # .
            # # . # #
            . # # # .
            . . # . .
            `)
        basic.showLeds(`
            . # # # .
            # # . # #
            # . . . #
            # # . # #
            . # # # .
            `)
        radio.sendNumber(1)
        isExploding = 0
    }
})
input.onButtonPressed(Button.A, () => {
    cooldown = 10
    isExploding = 1
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # # # .
        # # . # #
        . # # # .
        . . # . .
        `)
    basic.showLeds(`
        . # # # .
        # # . # #
        # . . . #
        # # . # #
        . # # # .
        `)
    radio.sendNumber(1)
    isExploding = 0
})
isExploding = 0
cooldown = 0
cooldown = 0
isExploding = 0
radio.setGroup(0)
radio.setTransmitPower(1)
