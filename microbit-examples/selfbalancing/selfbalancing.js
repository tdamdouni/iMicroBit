let v1 = 0
let v2 = 0
let v3 = 0
let pos = 0
basic.forever(() => {
    // Ändra position baserad på acceleration mätvärde i Y
    // riktning. Dela med minus 100 för att ändra riktning
    // och göra små ändringar.
    v1 = pos + input.acceleration(Dimension.Y) / -100
    // Säkerställa att vi inte går under 0 eller över 180.
    v1 = Math.max(Math.min(v1, 180), 0)
    // Beräkna medelvärde på sista 3 beräknade positioner
    // för att jämna ut rörelser.
    pos = (v1 + v2 + v3) / 3
    // Flytta servo motor till ny position.
    pins.servoWritePin(AnalogPin.P2, pos)
    // Flytta alla värden till nästa plats, och glömma den
    // äldste.
    v3 = v2
    v2 = v1
})
