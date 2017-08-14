//ICON 01111.01001.00001.01001.00011

# LET %MAX = 15
// When the BBC micro:bit runs.
function onStart() {
	_.say("A&B");
	while (true) {
		$.x = 2;
		$.y = 5;
		$.dx = 0;
		$.dy = -1;
		$.length = 2;
		$.headPointer = 0;
		$.appleX = 2;
		$.appleY = 4;
		$.score = -1;
		$.movedThisGo = false;
		$.nextMove = 0;
		/* The BBC micro:bit's Javascript does not support arrays,
		so we have to declare a lot of variables: */
# FOR %N = 0 TO %MAX
		$.oldX%N = -1;
		$.oldY%N = -1;
# NEXT %N
		$.gameOver = false;
		$.gameStarted = false;
		while (!$.gameStarted) {
			wait(50);
		}
		_.clear();
		while (!$.gameOver) {
			if ($.nextMove == 1) {
				turnLeft();
			}
			if ($.nextMove == 2) {
				turnRight();
			}
			$.nextMove = 0;
			$.movedThisGo = false;
			for (var i = 0; i < 4; i = i + 1) {
				_.off(globals.appleX, globals.appleY);
				wait(35);
				_.on(globals.appleX, globals.appleY);
				wait(35);
			}
			$.x = $.x + $.dx;
			$.y = $.y + $.dy;
			if (($.appleX == $.x) && ($.appleY == $.y)) {
				$.score = $.score + 1;
				while (true) {
					$.appleX = Random.number(0, 4);
					$.appleY = Random.number(0, 4);
					if (!_.isOn($.appleX, $.appleY)) {
						break;
					}
				}
				_.on($.appleX, $.appleY);
				if ($.length < %MAX) {
					$.length = $.length + 1;
				}
			} else {
				if (_.isOn($.x, $.y)) {
					$.gameOver = true;
				}
			}
			if (($.x < 0) || ($.y < 0) || ($.x > 4) || ($.y > 4)) {
				$.gameOver = true;
			}
			_.on($.x, $.y);
			/* Again, we have to do a lot of "if"s to simulate an array: */
# FOR %N = 0 TO %MAX
			if ($.headPointer == %N) {
				$.oldX%N = $.x;
				$.oldY%N = $.y;
			}
# NEXT %N
			var tailPointer = Math.mod($.headPointer + $.length, %MAX);
# FOR %N = 0 TO %MAX
			if (tailPointer == %N) {
				_.off($.oldX%N, $.oldY%N);
			}
# NEXT %N
			if ($.headPointer == 0) {
				$.headPointer = %MAX;
			}
			$.headPointer = $.headPointer - 1;
		}
		_.say($.score);
	}
}

function onPressA() {
	if ($.movedThisGo) {
		$.nextMove = 1;
	} else {
		turnLeft();
	}
}

function onPressB() {
	if ($.movedThisGo) {
		$.nextMove = 2;
	} else {
		turnRight();
	}
}

function turnLeft() {
	var oldDx = $.dx;
	$.dx = $.dy;
	$.dy = 0 - oldDx;
	$.movedThisGo = true;
}

function turnRight() {
	var oldDx = $.dx;
	$.dx = 0 - $.dy;
	$.dy = oldDx;
	$.movedThisGo = true;
}

function onPressAandB() {
	$.gameStarted = true;
}

