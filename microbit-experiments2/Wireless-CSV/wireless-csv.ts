// By Andrew Mulholland - https://github.com/gbaman/microbit-experiments
// Simple example to go alongside the Python script for reading data wirelessly using 2 BBC micro:bits.
// Transmits the 3 accelerometer values alongside a title to allow them to be distinguished later.
// When they are recieved on the other end, simply write to the serial port to be picked up by the Python Script.
// Script was written with the Microsoft PXT platform, it can also be found at https://m.pxt.io/vxdmdu.

// If copying below into PXT code section, ignore all comments and copy from line below.

radio.setGroup(1);
basic.forever(() => {
    radio.sendValue("Acc-X", input.acceleration(Dimension.X));
    basic.pause(30);
    radio.sendValue("Acc-Y", input.acceleration(Dimension.Y));
    basic.pause(30);
    radio.sendValue("Acc-Z", input.acceleration(Dimension.Z));
    basic.pause(30);
});
radio.onDataReceived(() => {
    radio.writeValueToSerial();
});
