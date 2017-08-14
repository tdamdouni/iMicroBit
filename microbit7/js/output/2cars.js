function onStart() {
	microbit.say('A&B');
	globals.gameOver = true;
}

function onPressAandB() {
	if (globals.gameOver) {
		globals.gameOver = false;
		globals.ax = 1;
		globals.bx = 3;
		globals.score = 0;
		globals.freeLine = true;
		microbit.clear();
		while (!globals.gameOver) {
			microbit.on(globals.ax, 4);
			microbit.on(globals.bx, 4);
			wait(100);
			if (!globals.gameOver) {
				microbit.off(globals.ax, 4);
				microbit.off(globals.bx, 4);
				wait(100);
			}
			if (!globals.gameOver) {
				for (var y = 4; y > 0; y = y - 1) {
					for (var x = 0; x < 5; x = x + 1) {
						if (microbit.isOn(x, y - 1)) {
							microbit.on(x, y);
						} else {
							microbit.off(x, y);
						}
					}
				}
				for (var x = 0; x < 5; x = x + 1) {
					microbit.off(x, 0);
				}
	if (microbit.isOn(globals.ax, 4) || microbit.isOn(globals.bx, 4)) {
		globals.gameOver = true;
		microbit.say(globals.score);
	}
			}
			if (!globals.gameOver) {
				globals.score = globals.score + 1;
				if (globals.freeLine) {
					globals.freeLine = false;
				} else {
					globals.freeLine = true;
					var r = Random.number(0, 2);
					if (r != 2) {
						microbit.on(r, 0);
					}
					r = Random.number(2, 4);
					if (r != 2) {
						microbit.on(r, 0);
					}
				}
			}
		}
	}
}

function onPressA() {
	microbit.off(globals.ax, 4);
	globals.ax = 1 - globals.ax;
	if (microbit.isOn(globals.ax, 4) || microbit.isOn(globals.bx, 4)) {
		globals.gameOver = true;
		microbit.say(globals.score);
	}
}

function onPressB() {
	microbit.off(globals.bx, 4);
	globals.bx = 7 - globals.bx;
	if (microbit.isOn(globals.ax, 4) || microbit.isOn(globals.bx, 4)) {
		globals.gameOver = true;
		microbit.say(globals.score);
	}
}
