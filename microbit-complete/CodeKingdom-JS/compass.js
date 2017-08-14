/* When the BBC micro:bit runs        */
function onStart(  ) {
	microbit.calibrateCompass();
	while (true) {
		
		globals.myNumber = microbit.bearing / 40;
		if (globals.myNumber == 0) {
			
			microbit.draw(Pattern("00100.01110.10101.00100.00100"));
			
		}
		
		else if (globals.myNumber == 1) {
			
			microbit.draw(Pattern("01111.00011.00101.01001.10000"));
			
		}
		
		else if (globals.myNumber == 2) {
			
			microbit.draw(Pattern("00100.00010.11111.00010.00100"));
			
		}
		
		else if (globals.myNumber == 3) {
			
			microbit.draw(Pattern("10000.01001.00101.00011.01111"));
			
		}
		
		else if (globals.myNumber == 4) {
			
			microbit.draw(Pattern("00100.00100.10101.01110.00100"));
			
		}
		
		else if (globals.myNumber == 5) {
			
			microbit.draw(Pattern("00001.10010.10100.11000.11110"));
			
		}
		
		else if (globals.myNumber == 6) {
			
			microbit.draw(Pattern("00100.01000.11111.01000.00100"));
			
		}
		
		else if (globals.myNumber == 7) {
			
			microbit.draw(Pattern("11110.11000.10100.10010.00001"));
			
		}
		
		else if (globals.myNumber == 8) {
			
			microbit.draw(Pattern("00100.01110.10101.00100.00100"));
			
		}
		
		wait(100);
		
	}
	
	
}
