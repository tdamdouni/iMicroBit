function onStart() {
	globals.inMazeX = 0;
	globals.inMazeY = 0;
	globals.isWall = false;
	globals.x = 6;
	globals.y = 7;
	globals.dx = -1;
	globals.dy = 0;
	globals.inMazeX = globals.x + globals.dy;
	globals.inMazeY = globals.y - globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var a = globals.isWall;
	globals.inMazeX = globals.x + globals.dy + globals.dx;
	globals.inMazeY = globals.y - globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var b = globals.isWall;
	globals.inMazeX = globals.x + globals.dx;
	globals.inMazeY = globals.y + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var c = globals.isWall;
	globals.inMazeX = globals.x - globals.dy + globals.dx;
	globals.inMazeY = globals.y + globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var d = globals.isWall;
	globals.inMazeX = globals.x - globals.dy;
	globals.inMazeY = globals.y + globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var e = globals.isWall;
	microbit.clear();
	if (a) {
		microbit.on(0, 0);
		microbit.on(0, 4);
	}
	if (b && !a) {
		microbit.on(0, 1);
		microbit.on(0, 3);
	}
	if (!b && !a) {
		microbit.on(0, 2);
	}
	if (a || b || c) {
		microbit.on(1, 1);
		microbit.on(1, 3);
	}
	if (c) {
		microbit.on(2, 1);
		microbit.on(2, 3);
	}
	if (!c) {
		microbit.on(2, 2);
	}
	if (e) {
		microbit.on(4, 0);
		microbit.on(4, 4);
	}
	if (d && !e) {
		microbit.on(4, 1);
		microbit.on(4, 3);
	}
	if (!d && !e) {
		microbit.on(4, 2);
	}
	if (e || d || c) {
		microbit.on(3, 1);
		microbit.on(3, 3);
	}
	if (a && (!b || c)) {
		microbit.on(1, 2);
	}
	if (!a && !b) {
		microbit.on(1, 2);
	}
	if (!a && b && !c) {
		microbit.on(1, 2);
	}
	if (e && (!d || c)) {
		microbit.on(3, 2);
	}
	if (!e && !d) {
		microbit.on(3, 2);
	}
	if (!e && d && !c) {
		microbit.on(3, 2);
	}
}

function onPressA() {
	var dx = globals.dx;
	globals.dx = globals.dy;
	globals.dy = 0 - dx;
	globals.inMazeX = globals.x + globals.dy;
	globals.inMazeY = globals.y - globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var a = globals.isWall;
	globals.inMazeX = globals.x + globals.dy + globals.dx;
	globals.inMazeY = globals.y - globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var b = globals.isWall;
	globals.inMazeX = globals.x + globals.dx;
	globals.inMazeY = globals.y + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var c = globals.isWall;
	globals.inMazeX = globals.x - globals.dy + globals.dx;
	globals.inMazeY = globals.y + globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var d = globals.isWall;
	globals.inMazeX = globals.x - globals.dy;
	globals.inMazeY = globals.y + globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var e = globals.isWall;
	microbit.clear();
	if (a) {
		microbit.on(0, 0);
		microbit.on(0, 4);
	}
	if (b && !a) {
		microbit.on(0, 1);
		microbit.on(0, 3);
	}
	if (!b && !a) {
		microbit.on(0, 2);
	}
	if (a || b || c) {
		microbit.on(1, 1);
		microbit.on(1, 3);
	}
	if (c) {
		microbit.on(2, 1);
		microbit.on(2, 3);
	}
	if (!c) {
		microbit.on(2, 2);
	}
	if (e) {
		microbit.on(4, 0);
		microbit.on(4, 4);
	}
	if (d && !e) {
		microbit.on(4, 1);
		microbit.on(4, 3);
	}
	if (!d && !e) {
		microbit.on(4, 2);
	}
	if (e || d || c) {
		microbit.on(3, 1);
		microbit.on(3, 3);
	}
	if (a && (!b || c)) {
		microbit.on(1, 2);
	}
	if (!a && !b) {
		microbit.on(1, 2);
	}
	if (!a && b && !c) {
		microbit.on(1, 2);
	}
	if (e && (!d || c)) {
		microbit.on(3, 2);
	}
	if (!e && !d) {
		microbit.on(3, 2);
	}
	if (!e && d && !c) {
		microbit.on(3, 2);
	}
}

function onPressB() {
	var dx = globals.dx;
	globals.dx = 0 - globals.dy;
	globals.dy = dx;
	globals.inMazeX = globals.x + globals.dy;
	globals.inMazeY = globals.y - globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var a = globals.isWall;
	globals.inMazeX = globals.x + globals.dy + globals.dx;
	globals.inMazeY = globals.y - globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var b = globals.isWall;
	globals.inMazeX = globals.x + globals.dx;
	globals.inMazeY = globals.y + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var c = globals.isWall;
	globals.inMazeX = globals.x - globals.dy + globals.dx;
	globals.inMazeY = globals.y + globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var d = globals.isWall;
	globals.inMazeX = globals.x - globals.dy;
	globals.inMazeY = globals.y + globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var e = globals.isWall;
	microbit.clear();
	if (a) {
		microbit.on(0, 0);
		microbit.on(0, 4);
	}
	if (b && !a) {
		microbit.on(0, 1);
		microbit.on(0, 3);
	}
	if (!b && !a) {
		microbit.on(0, 2);
	}
	if (a || b || c) {
		microbit.on(1, 1);
		microbit.on(1, 3);
	}
	if (c) {
		microbit.on(2, 1);
		microbit.on(2, 3);
	}
	if (!c) {
		microbit.on(2, 2);
	}
	if (e) {
		microbit.on(4, 0);
		microbit.on(4, 4);
	}
	if (d && !e) {
		microbit.on(4, 1);
		microbit.on(4, 3);
	}
	if (!d && !e) {
		microbit.on(4, 2);
	}
	if (e || d || c) {
		microbit.on(3, 1);
		microbit.on(3, 3);
	}
	if (a && (!b || c)) {
		microbit.on(1, 2);
	}
	if (!a && !b) {
		microbit.on(1, 2);
	}
	if (!a && b && !c) {
		microbit.on(1, 2);
	}
	if (e && (!d || c)) {
		microbit.on(3, 2);
	}
	if (!e && !d) {
		microbit.on(3, 2);
	}
	if (!e && d && !c) {
		microbit.on(3, 2);
	}
}

function onPressAandB() {
	globals.inMazeX = globals.x + globals.dx;
	globals.inMazeY = globals.y + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	if (!globals.isWall) {
		globals.x = globals.inMazeX;
		globals.y = globals.inMazeY;
	globals.inMazeX = globals.x + globals.dy;
	globals.inMazeY = globals.y - globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var a = globals.isWall;
	globals.inMazeX = globals.x + globals.dy + globals.dx;
	globals.inMazeY = globals.y - globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var b = globals.isWall;
	globals.inMazeX = globals.x + globals.dx;
	globals.inMazeY = globals.y + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var c = globals.isWall;
	globals.inMazeX = globals.x - globals.dy + globals.dx;
	globals.inMazeY = globals.y + globals.dx + globals.dy;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var d = globals.isWall;
	globals.inMazeX = globals.x - globals.dy;
	globals.inMazeY = globals.y + globals.dx;
	if ((globals.inMazeY < 0) || (globals.inMazeY > 10) || (globals.inMazeY < 0) || (globals.inMazeY > 14)) {
		globals.isWall = false;
	} else { if ((globals.inMazeX == 0) || (globals.inMazeX == 14)) {
		globals.isWall = true;
	} else { if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else { if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else { if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else { if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 5) && (globals.inMazeX != 11);
	} else { if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else { if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else { if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else { if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else { if (globals.inMazeY == 10) {
		globals.isWall = true;
	} else {
		globals.isWall = false;
	}}}}}}}}}}}}
	var e = globals.isWall;
	microbit.clear();
	if (a) {
		microbit.on(0, 0);
		microbit.on(0, 4);
	}
	if (b && !a) {
		microbit.on(0, 1);
		microbit.on(0, 3);
	}
	if (!b && !a) {
		microbit.on(0, 2);
	}
	if (a || b || c) {
		microbit.on(1, 1);
		microbit.on(1, 3);
	}
	if (c) {
		microbit.on(2, 1);
		microbit.on(2, 3);
	}
	if (!c) {
		microbit.on(2, 2);
	}
	if (e) {
		microbit.on(4, 0);
		microbit.on(4, 4);
	}
	if (d && !e) {
		microbit.on(4, 1);
		microbit.on(4, 3);
	}
	if (!d && !e) {
		microbit.on(4, 2);
	}
	if (e || d || c) {
		microbit.on(3, 1);
		microbit.on(3, 3);
	}
	if (a && (!b || c)) {
		microbit.on(1, 2);
	}
	if (!a && !b) {
		microbit.on(1, 2);
	}
	if (!a && b && !c) {
		microbit.on(1, 2);
	}
	if (e && (!d || c)) {
		microbit.on(3, 2);
	}
	if (!e && !d) {
		microbit.on(3, 2);
	}
	if (!e && d && !c) {
		microbit.on(3, 2);
	}
		wait(100);
		if (globals.y < 0) {
			wait(200);
			microbit.draw(Pattern("01010.01010.00000.10001.01110"));
		}
	}
}
