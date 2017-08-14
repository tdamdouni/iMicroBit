/**
 * @file display-spiral.js 
 * displays a spiral pattern on micro:bit LED matrix that appears then disappears
 *
 * This was originally written in PXL block code (pxl.microbit.org)
 * using lots of for loops. By the time we'd made the first three lines 
 * appear and disappear it was getting complex to read so I showed how 
 * to put the repetition into a function. 
 * 
 * Credit to:
 *    F for the concept and initial coding
 *    A for the logic in the function
 */
basic.forever(() => {
    // Appear 1 Across
    ShowOrDisappear(0, 4, 4, true, false)
    // Appear 2 Sides
    ShowOrDisappear(0, 3, 4, true, true)
    // 3 Across
    ShowOrDisappear(0, 3, 3, true, false)
    // 4 Side
    ShowOrDisappear(1, 2, 3, true, true)
    // 5 Across
    ShowOrDisappear(1, 2, 2, true, false)
    // now disappear in reverse
    ShowOrDisappear(2, 1, 2, false, false)
    ShowOrDisappear(2, 1, 3, false, true)
    ShowOrDisappear(3, 0, 3, false, false)
    ShowOrDisappear(3, 0, 4, false, true)
    ShowOrDisappear(4, 0, 4, false, false)
})
/**
* Make a line of dots appear or disappear in sequence
* @function ShowOrDisappear
* @param {number} Start - Which X or Y value to start counting from
* @param {number} End - Which X or Y value to end counting on
* @param {number} Against - value to go 'against' the count (i.e. in Y if X is count, or vice versa)
* @param {boolean} Appear - true to make dots appear, false to disappear
* @param {boolean} Side - true to go up and down sides, false to go across top and bottom
*/
function ShowOrDisappear(Start: number, End: number, Against: number, Appear: boolean, Side: boolean) {
	// this used to be a simple for loop until we needed it to automatically count up AND DOWN
    let Count = Start
    while (((Start < End) && (Count <= End)) || ((Start >= End) && (Count >= End))) {
		// could simplify by assigning X1 Y1 X2 and Y2 values to plot 
        if (Appear) {
            if (Side) {
                led.plot(Against, 4 - Count)
                led.plot(4 - Against, Count)
            } else {
                led.plot(Count, Against)
                led.plot(4 - Count, 4 - Against)
            }
        } else {
            if (Side) {
                led.unplot(Against, 4 - Count)
                led.unplot(4 - Against, Count)
            } else {
                led.unplot(Count, Against)
                led.unplot(4 - Count, 4 - Against)
            }
        }
        basic.pause(100)
        if (Start < End) {
            Count++
        } else {
            Count--
        }
    }
}
