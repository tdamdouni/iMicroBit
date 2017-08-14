let light = 0
basic.forever(() => {
    light = input.lightLevel()
    serial.writeNumber(light)
    serial.writeLine("")
})

