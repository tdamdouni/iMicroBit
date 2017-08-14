/* When the BBC micro:bit runs     */
function onStart(  ) {
	microbit.say("SHAKE ME!");
	
}

function onShake(  ) {
	microbit.say(Random.number(1, 6));
	
}
