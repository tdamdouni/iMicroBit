bluetooth.startAccelerometerService()
bluetooth.startButtonService()
bluetooth.startIOPinService()
bluetooth.startLEDService()
bluetooth.startLEDService()
bluetooth.startTemperatureService()
bluetooth.startMagnetometerService()
bluetooth.onBluetoothConnected(() => {
    basic.showString("C")
})
bluetooth.onBluetoothDisconnected(() => {
    basic.showString("D")
})

