let counter = 0
let connected = 0
bluetooth.onBluetoothConnected(() => {
    basic.showString("C")
    connected = 1
    devices.tellCameraTo(MesCameraEvent.LaunchPhotoMode)
})
bluetooth.onBluetoothDisconnected(() => {
    basic.showString("D")
    connected = 0
})
input.onButtonPressed(Button.A, () => {
    if (connected) {
        counter = 4
        for (let i = 0; i < 4; i++) {
            basic.showNumber(counter)
            basic.pause(1000)
            counter += -1
        }
        basic.showLeds(`
            . # . # .
            . . . . .
            . . . . .
            # . . . #
            . # # # .
            `)
        devices.tellCameraTo(MesCameraEvent.TakePhoto)
        basic.pause(1000)
        basic.clearScreen()
    } else {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        basic.pause(1000)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, () => {
    if (connected) {
        devices.tellCameraTo(MesCameraEvent.ToggleFrontRear)
    }
})

