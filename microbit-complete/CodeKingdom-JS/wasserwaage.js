function onStart(  ) {
	globals.actX = microbit.tiltX;
	globals.actY = microbit.tiltY;
	globals.oldX = globals.actX;
	globals.oldY = globals.actY;
	while (true) {
		globals.actX = microbit.tiltX;
		globals.actY = microbit.tiltY;
		microbit.on(globals.actX, globals.actY);
		if (( globals.oldX != globals.actX ) || ( globals.oldY != globals.actY )) {
			microbit.off(globals.oldX, globals.oldY);
		}
		globals.oldX = globals.actX;
		globals.oldY = globals.actY;
		wait(40);
	}
}

