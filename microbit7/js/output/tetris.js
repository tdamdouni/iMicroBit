function onStart() {
var x = 0;
var y = 0;
var i = 0;
var isLine = false;
var blockType = 0;
var y2 = 0;
	globals.gameOver = false;
	globals.score = 0;
	globals.blockCount = 0;
	globals.block0X = 0;
	globals.testBlock0X = 0;
	globals.block0Y = 0;
	globals.testBlock0Y = 0;
	globals.blockCount = 0;
	globals.block1X = 0;
	globals.testBlock1X = 0;
	globals.block1Y = 0;
	globals.testBlock1Y = 0;
	globals.blockCount = 0;
	globals.block2X = 0;
	globals.testBlock2X = 0;
	globals.block2Y = 0;
	globals.testBlock2Y = 0;
	globals.blockCount = 0;
	globals.block3X = 0;
	globals.testBlock3X = 0;
	globals.block3Y = 0;
	globals.testBlock3Y = 0;
	blockType = Random.number(0, 7);
	if (blockType == 0) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 3;
		globals.testBlock2Y = 1;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 1) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 1;
		globals.testBlock2Y = 1;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 2) {
		globals.blockCount = 1;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.twiceCentreX = 4;
		globals.twiceCentreY = 0;
	}
	if (blockType == 3) {
		globals.blockCount = 2;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 3;
		globals.testBlock1Y = 0;
		globals.twiceCentreX = 4;
		globals.twiceCentreY = 0;
	}
	if (blockType == 4) {
		globals.blockCount = 2;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.twiceCentreX = 4;
		globals.twiceCentreY = 0;
	}
	if (blockType == 5) {
		globals.blockCount = 4;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 3;
		globals.testBlock2Y = 0;
		globals.testBlock3X = 3;
		globals.testBlock3Y = 1;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 6) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 3;
		globals.testBlock2Y = 0;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 7) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 1;
		globals.testBlock2Y = 0;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	globals.movedOK = true;
	if (0 < globals.blockCount) {
		if ((globals.testBlock0X < 0) ||
			(globals.testBlock0X > 4) ||
			(globals.testBlock0Y > 4) ||
			microbit.isOn(globals.testBlock0X, globals.testBlock0Y)) {
				globals.movedOK = false;
		}
	}
	if (1 < globals.blockCount) {
		if ((globals.testBlock1X < 0) ||
			(globals.testBlock1X > 4) ||
			(globals.testBlock1Y > 4) ||
			microbit.isOn(globals.testBlock1X, globals.testBlock1Y)) {
				globals.movedOK = false;
		}
	}
	if (2 < globals.blockCount) {
		if ((globals.testBlock2X < 0) ||
			(globals.testBlock2X > 4) ||
			(globals.testBlock2Y > 4) ||
			microbit.isOn(globals.testBlock2X, globals.testBlock2Y)) {
				globals.movedOK = false;
		}
	}
	if (3 < globals.blockCount) {
		if ((globals.testBlock3X < 0) ||
			(globals.testBlock3X > 4) ||
			(globals.testBlock3Y > 4) ||
			microbit.isOn(globals.testBlock3X, globals.testBlock3Y)) {
				globals.movedOK = false;
		}
	}
	if (globals.movedOK) {
		globals.block0X = globals.testBlock0X;
		globals.block0Y = globals.testBlock0Y;
		globals.block1X = globals.testBlock1X;
		globals.block1Y = globals.testBlock1Y;
		globals.block2X = globals.testBlock2X;
		globals.block2Y = globals.testBlock2Y;
		globals.block3X = globals.testBlock3X;
		globals.block3Y = globals.testBlock3Y;
	}
	if (!globals.movedOK) {
	globals.blockCount = 0;
	globals.gameOver = true;
	for (y = 4; y >= 0; y = y - 1) {
		for (x = 4; x >= 0; x = x - 1) {
			microbit.on(x, y);
		}
		wait(50);
	}
	microbit.draw(Pattern("11111.11111.11111.11111.11111"));
	wait(500);
	microbit.say(globals.score);
	}
	while (!globals.gameOver) {
		for (i = 0; i < 5; i = i + 1) {
	if (0 < globals.blockCount) {
		microbit.on(globals.block0X, globals.block0Y);
	}
	if (1 < globals.blockCount) {
		microbit.on(globals.block1X, globals.block1Y);
	}
	if (2 < globals.blockCount) {
		microbit.on(globals.block2X, globals.block2Y);
	}
	if (3 < globals.blockCount) {
		microbit.on(globals.block3X, globals.block3Y);
	}
			wait(50);
	if (0 < globals.blockCount) {
		microbit.off(globals.block0X, globals.block0Y);
	}
	if (1 < globals.blockCount) {
		microbit.off(globals.block1X, globals.block1Y);
	}
	if (2 < globals.blockCount) {
		microbit.off(globals.block2X, globals.block2Y);
	}
	if (3 < globals.blockCount) {
		microbit.off(globals.block3X, globals.block3Y);
	}
			wait(50);
		}
		globals.testBlock0X = globals.block0X;
		globals.testBlock0Y = globals.block0Y + 1;
		globals.testBlock1X = globals.block1X;
		globals.testBlock1Y = globals.block1Y + 1;
		globals.testBlock2X = globals.block2X;
		globals.testBlock2Y = globals.block2Y + 1;
		globals.testBlock3X = globals.block3X;
		globals.testBlock3Y = globals.block3Y + 1;
	globals.movedOK = true;
	if (0 < globals.blockCount) {
		if ((globals.testBlock0X < 0) ||
			(globals.testBlock0X > 4) ||
			(globals.testBlock0Y > 4) ||
			microbit.isOn(globals.testBlock0X, globals.testBlock0Y)) {
				globals.movedOK = false;
		}
	}
	if (1 < globals.blockCount) {
		if ((globals.testBlock1X < 0) ||
			(globals.testBlock1X > 4) ||
			(globals.testBlock1Y > 4) ||
			microbit.isOn(globals.testBlock1X, globals.testBlock1Y)) {
				globals.movedOK = false;
		}
	}
	if (2 < globals.blockCount) {
		if ((globals.testBlock2X < 0) ||
			(globals.testBlock2X > 4) ||
			(globals.testBlock2Y > 4) ||
			microbit.isOn(globals.testBlock2X, globals.testBlock2Y)) {
				globals.movedOK = false;
		}
	}
	if (3 < globals.blockCount) {
		if ((globals.testBlock3X < 0) ||
			(globals.testBlock3X > 4) ||
			(globals.testBlock3Y > 4) ||
			microbit.isOn(globals.testBlock3X, globals.testBlock3Y)) {
				globals.movedOK = false;
		}
	}
	if (globals.movedOK) {
		globals.block0X = globals.testBlock0X;
		globals.block0Y = globals.testBlock0Y;
		globals.block1X = globals.testBlock1X;
		globals.block1Y = globals.testBlock1Y;
		globals.block2X = globals.testBlock2X;
		globals.block2Y = globals.testBlock2Y;
		globals.block3X = globals.testBlock3X;
		globals.block3Y = globals.testBlock3Y;
	}
		if (!globals.movedOK) {
	if (0 < globals.blockCount) {
		microbit.on(globals.block0X, globals.block0Y);
	}
	if (1 < globals.blockCount) {
		microbit.on(globals.block1X, globals.block1Y);
	}
	if (2 < globals.blockCount) {
		microbit.on(globals.block2X, globals.block2Y);
	}
	if (3 < globals.blockCount) {
		microbit.on(globals.block3X, globals.block3Y);
	}
	for (y = 4; y >= 0; y = y - 1) {
		isLine = true;
		for (x = 4; x >= 0; x = x - 1) {
			if (!microbit.isOn(x, y)) {
				isLine = false;
			}
		}
		if (isLine) {
			for (y2 = y; y2 > 0; y2 = y2 - 1) {
				for (x = 4; x >= 0; x = x - 1) {
					if (microbit.isOn(x, y2 - 1)) {
						microbit.on(x, y2);
					} else {
						microbit.off(x, y2);
					}
				}
			}
			y = y + 1;
			globals.score = globals.score + 1;
		}
	}
	blockType = Random.number(0, 7);
	if (blockType == 0) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 3;
		globals.testBlock2Y = 1;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 1) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 1;
		globals.testBlock2Y = 1;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 2) {
		globals.blockCount = 1;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.twiceCentreX = 4;
		globals.twiceCentreY = 0;
	}
	if (blockType == 3) {
		globals.blockCount = 2;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 3;
		globals.testBlock1Y = 0;
		globals.twiceCentreX = 4;
		globals.twiceCentreY = 0;
	}
	if (blockType == 4) {
		globals.blockCount = 2;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.twiceCentreX = 4;
		globals.twiceCentreY = 0;
	}
	if (blockType == 5) {
		globals.blockCount = 4;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 3;
		globals.testBlock2Y = 0;
		globals.testBlock3X = 3;
		globals.testBlock3Y = 1;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 6) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 3;
		globals.testBlock2Y = 0;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	if (blockType == 7) {
		globals.blockCount = 3;
		globals.testBlock0X = 2;
		globals.testBlock0Y = 0;
		globals.testBlock1X = 2;
		globals.testBlock1Y = 1;
		globals.testBlock2X = 1;
		globals.testBlock2Y = 0;
		globals.twiceCentreX = 5;
		globals.twiceCentreY = 1;
	}
	globals.movedOK = true;
	if (0 < globals.blockCount) {
		if ((globals.testBlock0X < 0) ||
			(globals.testBlock0X > 4) ||
			(globals.testBlock0Y > 4) ||
			microbit.isOn(globals.testBlock0X, globals.testBlock0Y)) {
				globals.movedOK = false;
		}
	}
	if (1 < globals.blockCount) {
		if ((globals.testBlock1X < 0) ||
			(globals.testBlock1X > 4) ||
			(globals.testBlock1Y > 4) ||
			microbit.isOn(globals.testBlock1X, globals.testBlock1Y)) {
				globals.movedOK = false;
		}
	}
	if (2 < globals.blockCount) {
		if ((globals.testBlock2X < 0) ||
			(globals.testBlock2X > 4) ||
			(globals.testBlock2Y > 4) ||
			microbit.isOn(globals.testBlock2X, globals.testBlock2Y)) {
				globals.movedOK = false;
		}
	}
	if (3 < globals.blockCount) {
		if ((globals.testBlock3X < 0) ||
			(globals.testBlock3X > 4) ||
			(globals.testBlock3Y > 4) ||
			microbit.isOn(globals.testBlock3X, globals.testBlock3Y)) {
				globals.movedOK = false;
		}
	}
	if (globals.movedOK) {
		globals.block0X = globals.testBlock0X;
		globals.block0Y = globals.testBlock0Y;
		globals.block1X = globals.testBlock1X;
		globals.block1Y = globals.testBlock1Y;
		globals.block2X = globals.testBlock2X;
		globals.block2Y = globals.testBlock2Y;
		globals.block3X = globals.testBlock3X;
		globals.block3Y = globals.testBlock3Y;
	}
	if (!globals.movedOK) {
	globals.blockCount = 0;
	globals.gameOver = true;
	for (y = 4; y >= 0; y = y - 1) {
		for (x = 4; x >= 0; x = x - 1) {
			microbit.on(x, y);
		}
		wait(50);
	}
	microbit.draw(Pattern("11111.11111.11111.11111.11111"));
	wait(500);
	microbit.say(globals.score);
	}
		} else {
			globals.twiceCentreY = globals.twiceCentreY + 2;
		}
	}
}

function onPressA() {
var x = 0;
var y = 0;
var i = 0;
var isLine = false;
var blockType = 0;
var y2 = 0;
	if (0 < globals.blockCount) {
		microbit.off(globals.block0X, globals.block0Y);
	}
	if (1 < globals.blockCount) {
		microbit.off(globals.block1X, globals.block1Y);
	}
	if (2 < globals.blockCount) {
		microbit.off(globals.block2X, globals.block2Y);
	}
	if (3 < globals.blockCount) {
		microbit.off(globals.block3X, globals.block3Y);
	}
	globals.testBlock0X = globals.block0X - 1;
	globals.testBlock0Y = globals.block0Y;
	globals.testBlock1X = globals.block1X - 1;
	globals.testBlock1Y = globals.block1Y;
	globals.testBlock2X = globals.block2X - 1;
	globals.testBlock2Y = globals.block2Y;
	globals.testBlock3X = globals.block3X - 1;
	globals.testBlock3Y = globals.block3Y;
	globals.movedOK = true;
	if (0 < globals.blockCount) {
		if ((globals.testBlock0X < 0) ||
			(globals.testBlock0X > 4) ||
			(globals.testBlock0Y > 4) ||
			microbit.isOn(globals.testBlock0X, globals.testBlock0Y)) {
				globals.movedOK = false;
		}
	}
	if (1 < globals.blockCount) {
		if ((globals.testBlock1X < 0) ||
			(globals.testBlock1X > 4) ||
			(globals.testBlock1Y > 4) ||
			microbit.isOn(globals.testBlock1X, globals.testBlock1Y)) {
				globals.movedOK = false;
		}
	}
	if (2 < globals.blockCount) {
		if ((globals.testBlock2X < 0) ||
			(globals.testBlock2X > 4) ||
			(globals.testBlock2Y > 4) ||
			microbit.isOn(globals.testBlock2X, globals.testBlock2Y)) {
				globals.movedOK = false;
		}
	}
	if (3 < globals.blockCount) {
		if ((globals.testBlock3X < 0) ||
			(globals.testBlock3X > 4) ||
			(globals.testBlock3Y > 4) ||
			microbit.isOn(globals.testBlock3X, globals.testBlock3Y)) {
				globals.movedOK = false;
		}
	}
	if (globals.movedOK) {
		globals.block0X = globals.testBlock0X;
		globals.block0Y = globals.testBlock0Y;
		globals.block1X = globals.testBlock1X;
		globals.block1Y = globals.testBlock1Y;
		globals.block2X = globals.testBlock2X;
		globals.block2Y = globals.testBlock2Y;
		globals.block3X = globals.testBlock3X;
		globals.block3Y = globals.testBlock3Y;
	}
	if (globals.movedOK) {
		globals.twiceCentreX = globals.twiceCentreX - 2;
	}
}

function onPressB() {
var x = 0;
var y = 0;
var i = 0;
var isLine = false;
var blockType = 0;
var y2 = 0;
	if (0 < globals.blockCount) {
		microbit.off(globals.block0X, globals.block0Y);
	}
	if (1 < globals.blockCount) {
		microbit.off(globals.block1X, globals.block1Y);
	}
	if (2 < globals.blockCount) {
		microbit.off(globals.block2X, globals.block2Y);
	}
	if (3 < globals.blockCount) {
		microbit.off(globals.block3X, globals.block3Y);
	}
	globals.testBlock0X = globals.block0X + 1;
	globals.testBlock0Y = globals.block0Y;
	globals.testBlock1X = globals.block1X + 1;
	globals.testBlock1Y = globals.block1Y;
	globals.testBlock2X = globals.block2X + 1;
	globals.testBlock2Y = globals.block2Y;
	globals.testBlock3X = globals.block3X + 1;
	globals.testBlock3Y = globals.block3Y;
	globals.movedOK = true;
	if (0 < globals.blockCount) {
		if ((globals.testBlock0X < 0) ||
			(globals.testBlock0X > 4) ||
			(globals.testBlock0Y > 4) ||
			microbit.isOn(globals.testBlock0X, globals.testBlock0Y)) {
				globals.movedOK = false;
		}
	}
	if (1 < globals.blockCount) {
		if ((globals.testBlock1X < 0) ||
			(globals.testBlock1X > 4) ||
			(globals.testBlock1Y > 4) ||
			microbit.isOn(globals.testBlock1X, globals.testBlock1Y)) {
				globals.movedOK = false;
		}
	}
	if (2 < globals.blockCount) {
		if ((globals.testBlock2X < 0) ||
			(globals.testBlock2X > 4) ||
			(globals.testBlock2Y > 4) ||
			microbit.isOn(globals.testBlock2X, globals.testBlock2Y)) {
				globals.movedOK = false;
		}
	}
	if (3 < globals.blockCount) {
		if ((globals.testBlock3X < 0) ||
			(globals.testBlock3X > 4) ||
			(globals.testBlock3Y > 4) ||
			microbit.isOn(globals.testBlock3X, globals.testBlock3Y)) {
				globals.movedOK = false;
		}
	}
	if (globals.movedOK) {
		globals.block0X = globals.testBlock0X;
		globals.block0Y = globals.testBlock0Y;
		globals.block1X = globals.testBlock1X;
		globals.block1Y = globals.testBlock1Y;
		globals.block2X = globals.testBlock2X;
		globals.block2Y = globals.testBlock2Y;
		globals.block3X = globals.testBlock3X;
		globals.block3Y = globals.testBlock3Y;
	}
	if (globals.movedOK) {
		globals.twiceCentreX = globals.twiceCentreX + 2;
	}
}

function onPressAandB() {
var x = 0;
var y = 0;
var i = 0;
var isLine = false;
var blockType = 0;
var y2 = 0;
	globals.movedOK = false;
	if (0 < globals.blockCount) {
		microbit.off(globals.block0X, globals.block0Y);
	}
	if (1 < globals.blockCount) {
		microbit.off(globals.block1X, globals.block1Y);
	}
	if (2 < globals.blockCount) {
		microbit.off(globals.block2X, globals.block2Y);
	}
	if (3 < globals.blockCount) {
		microbit.off(globals.block3X, globals.block3Y);
	}
	while (!globals.movedOK) {
		globals.testBlock0X = (globals.twiceCentreX + (2 * globals.block0Y) - globals.twiceCentreY) / 2;
		globals.testBlock0Y = (globals.twiceCentreY - (2 * globals.block0X) + globals.twiceCentreX) / 2;
		globals.testBlock1X = (globals.twiceCentreX + (2 * globals.block1Y) - globals.twiceCentreY) / 2;
		globals.testBlock1Y = (globals.twiceCentreY - (2 * globals.block1X) + globals.twiceCentreX) / 2;
		globals.testBlock2X = (globals.twiceCentreX + (2 * globals.block2Y) - globals.twiceCentreY) / 2;
		globals.testBlock2Y = (globals.twiceCentreY - (2 * globals.block2X) + globals.twiceCentreX) / 2;
		globals.testBlock3X = (globals.twiceCentreX + (2 * globals.block3Y) - globals.twiceCentreY) / 2;
		globals.testBlock3Y = (globals.twiceCentreY - (2 * globals.block3X) + globals.twiceCentreX) / 2;
	globals.movedOK = true;
	if (0 < globals.blockCount) {
		if ((globals.testBlock0X < 0) ||
			(globals.testBlock0X > 4) ||
			(globals.testBlock0Y > 4) ||
			microbit.isOn(globals.testBlock0X, globals.testBlock0Y)) {
				globals.movedOK = false;
		}
	}
	if (1 < globals.blockCount) {
		if ((globals.testBlock1X < 0) ||
			(globals.testBlock1X > 4) ||
			(globals.testBlock1Y > 4) ||
			microbit.isOn(globals.testBlock1X, globals.testBlock1Y)) {
				globals.movedOK = false;
		}
	}
	if (2 < globals.blockCount) {
		if ((globals.testBlock2X < 0) ||
			(globals.testBlock2X > 4) ||
			(globals.testBlock2Y > 4) ||
			microbit.isOn(globals.testBlock2X, globals.testBlock2Y)) {
				globals.movedOK = false;
		}
	}
	if (3 < globals.blockCount) {
		if ((globals.testBlock3X < 0) ||
			(globals.testBlock3X > 4) ||
			(globals.testBlock3Y > 4) ||
			microbit.isOn(globals.testBlock3X, globals.testBlock3Y)) {
				globals.movedOK = false;
		}
	}
	if (globals.movedOK) {
		globals.block0X = globals.testBlock0X;
		globals.block0Y = globals.testBlock0Y;
		globals.block1X = globals.testBlock1X;
		globals.block1Y = globals.testBlock1Y;
		globals.block2X = globals.testBlock2X;
		globals.block2Y = globals.testBlock2Y;
		globals.block3X = globals.testBlock3X;
		globals.block3Y = globals.testBlock3Y;
	}
	}
}
