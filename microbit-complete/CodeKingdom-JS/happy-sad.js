// When the BBC micro:bit runs.
function onStart(  ) {
	microbit.say("HAPPY / SAD");
	
}

function onPressA(  ) {
	microbit.draw(Pattern("01010.01010.00000.10001.01110"));
	
}

function onPressB(  ) {
	microbit.draw(Pattern("01010.01010.00000.01110.10001"));
	
}
