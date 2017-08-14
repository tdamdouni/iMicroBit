//ICON 00110.01100.00001.11101.10111

# LET %MAX = 4

var x = 0;
var y = 0;
var i = 0;
var isLine = false;
var blockType = 0;
var y2 = 0;

function onStart() {
	$.gameOver = false;
	$.score = 0;
# FOR %N = 0 TO %MAX
	$.blockCount = 0;
	$.block%NX = 0;
	$.testBlock%NX = 0;
	$.block%NY = 0;
	$.testBlock%NY = 0;
# NEXT %N
	newBlock();
	while (!$.gameOver) {
		for (i = 0; i < 5; i = i + 1) {
			showBlock();
			wait(50);
			hideBlock();
			wait(50);
		}
# FOR %N = 0 TO %MAX
		$.testBlock%NX = $.block%NX;
		$.testBlock%NY = $.block%NY + 1;
# NEXT %N
		moveBlock();
		if (!$.movedOK) {
			showBlock();
			checkLines();
			newBlock();
		} else {
			$.twiceCentreY = $.twiceCentreY + 2;
		}
	}
}

function newBlock() {
	blockType = Random.number(0, 7);
	if (blockType == 0) {
		// L
		$.blockCount = 3;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.testBlock1X = 2;
		$.testBlock1Y = 1;
		$.testBlock2X = 3;
		$.testBlock2Y = 1;
		$.twiceCentreX = 5;
		$.twiceCentreY = 1;
	}
	if (blockType == 1) {
		// J
		$.blockCount = 3;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.testBlock1X = 2;
		$.testBlock1Y = 1;
		$.testBlock2X = 1;
		$.testBlock2Y = 1;
		$.twiceCentreX = 5;
		$.twiceCentreY = 1;
	}
	if (blockType == 2) {
		// .
		$.blockCount = 1;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.twiceCentreX = 4;
		$.twiceCentreY = 0;
	}
	if (blockType == 3) {
		// -
		$.blockCount = 2;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.testBlock1X = 3;
		$.testBlock1Y = 0;
		$.twiceCentreX = 4;
		$.twiceCentreY = 0;
	}
	if (blockType == 4) {
		// |
		$.blockCount = 2;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.testBlock1X = 2;
		$.testBlock1Y = 1;
		$.twiceCentreX = 4;
		$.twiceCentreY = 0;
	}
	if (blockType == 5) {
		// []
		$.blockCount = 4;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.testBlock1X = 2;
		$.testBlock1Y = 1;
		$.testBlock2X = 3;
		$.testBlock2Y = 0;
		$.testBlock3X = 3;
		$.testBlock3Y = 1;
		$.twiceCentreX = 5;
		$.twiceCentreY = 1;
	}
	if (blockType == 6) {
		// upside-down L
		$.blockCount = 3;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.testBlock1X = 2;
		$.testBlock1Y = 1;
		$.testBlock2X = 3;
		$.testBlock2Y = 0;
		$.twiceCentreX = 5;
		$.twiceCentreY = 1;
	}
	if (blockType == 7) {
		// upside-down J
		$.blockCount = 3;
		$.testBlock0X = 2;
		$.testBlock0Y = 0;
		$.testBlock1X = 2;
		$.testBlock1Y = 1;
		$.testBlock2X = 1;
		$.testBlock2Y = 0;
		$.twiceCentreX = 5;
		$.twiceCentreY = 1;
	}
	moveBlock();
	if (!$.movedOK) {
		gameOver();
	}
}

function onPressA() {
	hideBlock();
# FOR %N = 0 TO %MAX
	$.testBlock%NX = $.block%NX - 1;
	$.testBlock%NY = $.block%NY;
# NEXT %N
	moveBlock();
	if ($.movedOK) {
		$.twiceCentreX = $.twiceCentreX - 2;
	}
}

function onPressB() {
	hideBlock();
# FOR %N = 0 TO %MAX
	$.testBlock%NX = $.block%NX + 1;
	$.testBlock%NY = $.block%NY;
# NEXT %N
	moveBlock();
	if ($.movedOK) {
		$.twiceCentreX = $.twiceCentreX + 2;
	}
}

function onPressAandB() {
	$.movedOK = false;
	hideBlock();
	while (!$.movedOK) {
# FOR %N = 0 TO %MAX
		$.testBlock%NX = ($.twiceCentreX + (2 * $.block%NY) - $.twiceCentreY) / 2;
		$.testBlock%NY = ($.twiceCentreY - (2 * $.block%NX) + $.twiceCentreX) / 2;
# NEXT %N
		moveBlock();
	}
}

function moveBlock() {
	$.movedOK = true;
# FOR %N = 0 TO %MAX
	if (%N < $.blockCount) {
		if (($.testBlock%NX < 0) ||
			($.testBlock%NX > 4) ||
			//($.testBlock%NY < 0) ||
			($.testBlock%NY > 4) ||
			_.isOn($.testBlock%NX, $.testBlock%NY)) {
				$.movedOK = false;
		}
	}
# NEXT %N
	if ($.movedOK) {
# FOR %N = 0 TO %MAX
		$.block%NX = $.testBlock%NX;
		$.block%NY = $.testBlock%NY;
# NEXT %N
	}
}

function gameOver() {
	$.blockCount = 0;
	$.gameOver = true;
	for (y = 4; y >= 0; y = y - 1) {
		for (x = 4; x >= 0; x = x - 1) {
			_.on(x, y);
		}
		wait(50);
	}
	_.draw(Pattern("11111.11111.11111.11111.11111"));
	wait(500);
	_.say($.score);
}

function showBlock() {
# FOR %N = 0 TO %MAX
	if (%N < $.blockCount) {
		_.on($.block%NX, $.block%NY);
	}
# NEXT %N
}

function hideBlock() {
# FOR %N = 0 TO %MAX
	if (%N < $.blockCount) {
		_.off($.block%NX, $.block%NY);
	}
# NEXT %N
}

function checkLines() {
	for (y = 4; y >= 0; y = y - 1) {
		isLine = true;
		for (x = 4; x >= 0; x = x - 1) {
			if (!_.isOn(x, y)) {
				isLine = false;
			}
		}
		if (isLine) {
			for (y2 = y; y2 > 0; y2 = y2 - 1) {
				for (x = 4; x >= 0; x = x - 1) {
					if (_.isOn(x, y2 - 1)) {
						_.on(x, y2);
					} else {
						_.off(x, y2);
					}
				}
			}
			y = y + 1;
			$.score = $.score + 1;
		}
	}
}

