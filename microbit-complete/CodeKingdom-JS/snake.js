function onStart(  ) {
	/* create variables to keep track of the:
	   the player's score, called score (should start at 1000)
	   the player's x-position, called posX (should start at 0)
	   the player's y-position, called posY (should start at 4)
	   the apple's x-position, called appleX (should start at 4)
	   the apple's y-position, called appleY (should start at 3)
	   the current level of the game, called level (should start at 0)
	   */
	globals.score = 1000;
	globals.posX = 0;
	globals.posY = 4;
	globals.appleX = 4;
	globals.appleY = 3;
	globals.level = 0;
	// create a while loop which checks whether the current level of the game is less than 10
	while (globals.level < 10) {
		
		// make the player's dot flash by turning it on, off and on again (with small pauses inbetween)
		// (remember the x and y coordinate of the player's dot is stored in posX and posY
		// and you can turn a single LED off by using microbit.on and microbit.off!)
		microbit.on(globals.posX, globals.posY);
		wait(100);
		microbit.off(globals.posX, globals.posY);
		wait(100);
		microbit.on(globals.posX, globals.posY);
		// display the apple on the screen (remember the apple's position is stored in appleX and appleY)
		microbit.on(globals.appleX, globals.appleY);
		/* create an if chunk that checks whether the player's X position (stored in posX)
		   is equal to the apple's X position (appleX) and the same for their Y positions.
		   You can check if two things are equal inside a condition by using '=='
		   */
		if (globals.posX == globals.appleX) {
			
			// if the condition is true, that means the player has collected the apple,
			// so draw a happy face on the screen for a short amount of time (e.g., 300ms)
			// increase the game level by one
			microbit.draw(Pattern("01010.01010.00000.10001.01110"));
			wait(300);
			globals.level = globals.level + 1;
			// set the apple's x- and y-position to a random number between 0 and 4
			//appleX = microbit.random(0, 4)
			globals.appleX = Random.number(0, 4);
			globals.appleY = Random.number(0, 4);
			// clear the screen
			microbit.clear();
			
		}
		
		/* create an if chunk to see if the micro:bit is being tilted to the right
		   AND that the player's dot is at x-position 1 or more (i.e., not at the edge)
		   */
		if (( microbit.tiltX > 2 ) && ( globals.posX >= 1 )) {
			
			// turn off the player's dot
			// update the player dot's x-position to be 1 less
			microbit.off(globals.posX, globals.posY);
			globals.posX = globals.posX - 1;
			
		}
		
		/* create an if chunk to see if the micro:bit is being tilted to the left
		   AND that the player's dot is at x-position 3 or less (i.e., not at the edge)
		   */
		if (( microbit.tiltX < 2 ) && ( globals.posX <= 3 )) {
			
			// turn off the player's dot
			// update the player dot's x-position to be 1 more
			microbit.off(globals.posX, globals.posY);
			globals.posX = globals.posX + 1;
			
		}
		
		/* create an if chunk to see if the micro:bit is being tilted down
		   AND that the player's dot is at y-position 1 or more (i.e., not at the edge)
		   */
		if (( microbit.tiltY < 2 ) && ( globals.posY >= 1 )) {
			
			// turn off the player's dot
			// update the player dot's y-position to be 1 less
			microbit.off(globals.posX, globals.posY);
			globals.posY = globals.posY - 1;
			
		}
		
		/* create an if chunk to see if the micro:bit is being tilted up
		   AND that the player's dot is at y-position 3 or less (i.e., not at the edge)
		   */
		if (( microbit.tiltY > 2 ) && ( globals.posY <= 3 )) {
			
			// turn off the player's dot
			// update the player dot's y-position to be 1 more
			microbit.off(globals.posX, globals.posY);
			globals.posY = globals.posY + 1;
			
		}
		
		// at the end of the loop, decrease the player's score by 1
		globals.score = globals.score - 1;
		
	}
	
	// out of the loop so the game is over! display the player's score to the screen
	microbit.say(globals.score);
	
}
