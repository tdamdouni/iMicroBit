'use strict';

var fs = require('fs');

fs.readdirSync('/Users/andrew/Downloads').forEach(fn => {
	if (!/\.hex$/.test(fn)) return;
	let lines = fs.readFileSync('/Users/andrew/Downloads/' + fn).toString().split('\n'),
		lineCount = lines.length - 13309,
		len = lines[13306].substr(9, 8);
	console.log(len, lineCount * 16, parseInt(len.substr(6) + len.substr(4, 2), 16), fn);
});