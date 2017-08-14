radio.setGroup(0)
radio.onDataPacketReceived(({receivedNumber}) => {
    if (receivedNumber == 1) {
        // I am the receiver - send an ACK
        radio.sendNumber(2)
        // Display
        basic.showString("<- ")
    }
    if (receivedNumber == 2) {
        // Got an ACK
        basic.showString("< ")
    }
})
basic.forever(() => {
    if (input.buttonIsPressed(Button.A)) {
        radio.sendNumber(1)
        basic.pause(300)
    }
})
