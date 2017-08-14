//ICON .0000010010.00000.01010.01010

function onStart() {
	_.say('A&B');
	$.gameOver = true;
}

function onPressAandB() {
	if ($.gameOver) {
		$.gameOver = false;
		$.ax = 1;
		$.bx = 3;
		$.score = 0;
		$.freeLine = true;
		_.clear();
		while (!$.gameOver) {
			// Draw the cars
			_.on($.ax, 4);
			_.on($.bx, 4);
			wait(100);
			if (!$.gameOver) {
				_.off($.ax, 4);
				_.off($.bx, 4);
				wait(100);
			}
			if (!$.gameOver) {
				// Move the obstacles
				for (var y = 4; y > 0; y = y - 1) {
					for (var x = 0; x < 5; x = x + 1) {
						if (_.isOn(x, y - 1)) {
							_.on(x, y);
						} else {
							_.off(x, y);
						}
					}
				}
				for (var x = 0; x < 5; x = x + 1) {
					_.off(x, 0);
				}
				checkCrash();
			}
			if (!$.gameOver) {
				$.score = $.score + 1;
				if ($.freeLine) {
					$.freeLine = false;
				} else {
					$.freeLine = true;
					var r = Random.number(0, 2);
					if (r != 2) {
						_.on(r, 0);
					}
					r = Random.number(2, 4);
					if (r != 2) {
						_.on(r, 0);
					}
				}
			}
		}
	}
}

function onPressA() {
	_.off($.ax, 4);
	$.ax = 1 - $.ax;
	checkCrash();
}

function onPressB() {
	_.off($.bx, 4);
	$.bx = 7 - $.bx;
	checkCrash();
}

function checkCrash() {
	if (_.isOn($.ax, 4) || _.isOn($.bx, 4)) {
		$.gameOver = true;
		microbit.say($.score);
	}
}