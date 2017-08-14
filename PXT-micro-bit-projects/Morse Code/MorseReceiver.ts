// Morse decoder for micro-bit
// P. Golden, 7th Jan 2017
// With helpful modifications from R. Shufflebotham, 8th Jan 2017

let MorseArray: number[] =[];
// Stores each received letter
let lastTime: number = 0;
// Stores the time of last received bit
// Every time a radio packet is received, record the time and add the bit to MorseArray
radio.setGroup(0);
radio.onDataPacketReceived(({receivedNumber}) => {
    lastTime = input.runningTime();
    MorseArray.push(receivedNumber);
})

// Check every half second whether there has been a 3 second gap after a received bit
// If so, decode and display the letter, and empty the array 
while (true) {
    if (input.runningTime() - lastTime >= 3000 && MorseArray.length != 0) {
        decode(MorseArray);
        MorseArray =[];
    }
    basic.pause(500);
    // Do this check every half second
}

// Look-up-table to decode the bits into letters
// Morse dash = 1, Morse dot = 0 
function decode(array: number[]) {
    basic.clearScreen();
    if (compArray(array,[0, 1])) {
        basic.showString("A");
    } else if (compArray(array,[1, 0, 0, 0])) {
        basic.showString("B");
    } else if (compArray(array,[1, 0, 1, 0])) {
        basic.showString("C");
    } else if (compArray(array,[1, 0, 0])) {
        basic.showString("D");
    } else if (compArray(array,[0])) {
        basic.showString("E");
    } else if (compArray(array,[0, 0, 1, 0])) {
        basic.showString("F");
    } else if (compArray(array,[1, 1, 0])) {
        basic.showString("G");
    } else if (compArray(array,[0, 0, 0, 0])) {
        basic.showString("H");
    } else if (compArray(array,[0, 0])) {
        basic.showString("I");
    } else if (compArray(array,[0, 1, 1, 1])) {
        basic.showString("J");
    } else if (compArray(array,[1, 0, 1])) {
        basic.showString("K");
    } else if (compArray(array,[0, 1, 0, 0])) {
        basic.showString("L");
    } else if (compArray(array,[1, 1])) {
        basic.showString("M");
    } else if (compArray(array,[1, 0])) {
        basic.showString("N");
    } else if (compArray(array,[1, 1, 1])) {
        basic.showString("O");
    } else if (compArray(array,[0, 1, 1, 0])) {
        basic.showString("P");
    } else if (compArray(array,[1, 1, 0, 1])) {
        basic.showString("Q");
    } else if (compArray(array,[0, 1, 0])) {
        basic.showString("R");
    } else if (compArray(array,[0, 0, 0])) {
        basic.showString("S");
    } else if (compArray(array,[1])) {
        basic.showString("T");
    } else if (compArray(array,[0, 0, 1])) {
        basic.showString("U");
    } else if (compArray(array,[0, 0, 0, 1])) {
        basic.showString("V");
    } else if (compArray(array,[0, 1, 1])) {
        basic.showString("W");
    } else if (compArray(array,[1, 0, 0, 1])) {
        basic.showString("X");
    } else if (compArray(array,[1, 0, 1, 1])) {
        basic.showString("Y");
    } else if (compArray(array,[1, 1, 0, 0])) {
        basic.showString("Z");
    }
}

// This function does an element by element comparison of 2 arrays
function compArray(array1: number[], array2: number[]): boolean {
    if (array1.length !== array2.length) {
        return false;
    }
    for (let i = 0; i < array1.length; i++) {
        if (array1[i] !== array2[i]) {
            return false;
        }
    }
    return true;
}
