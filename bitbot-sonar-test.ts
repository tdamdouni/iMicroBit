let distance = 0
basic.forever(() => {
    distance = sonar.ping(
    DigitalPin.P15,
    DigitalPin.P15,
    PingUnit.Centimeters
    )
    basic.showNumber(distance)
    basic.pause(300)
})
