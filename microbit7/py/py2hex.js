#!/usr/bin/env node
'use strict';

var fs = require('fs');

var fn = process.argv[2],
	outFn = fn.replace(/(\.py)?$/, '.hex');

var py = fs.readFileSync(fn).toString(),
	tpl = fs.readFileSync(__dirname + '/python.hex').toString().split('\n'),
	// Standard Micropython code:
	hex = tpl.slice(0, 13306);

// Add in boilerplate code if required
if (process.argv[3])
	py = fs.readFileSync(process.argv[3]).toString().replace(/^\#\%.*$/m, py);
// blank out comments to save RAM - but keep the empty line because
// it's just one byte and the line numbers in error messages are useful
py = py.replace(/^\s*\#.*$/gm, '');
fs.writeFileSync('.' + fn, py);

// Your script ar bytes:
var bytes = py.split('').map(char => char.charCodeAt(0));
// dummy length header
bytes.unshift(0x4D, 0x50, 0x00, 0x00);
// pad data to integer number of lines with at least one trailing null character
bytes.push(0x00);
while (bytes.length % 16)
	bytes.push(0x00);
// overwrite real length header
bytes[3] = (py.length >> 8) & 0xFF;
bytes[2] = py.length & 0xFF;

// Write it as hex:
var addr = 0xE00000;
for (let i = 0; i < bytes.length; ) {
	// data length
	var line = [ 0x10 ];
	// address
	for (let p = 16; p >= 0; p -= 8)
		line.push((addr >> p) & 0xFF);
	// data
	for (let n = 0; n < 16; ++n)
		line.push(bytes[i++]);
	// checksum
	line.push(-line.reduce((a, b) => ~~(a + b)) & 0xFF);
	hex.push(':' + line.map(x => (x < 0x10 ? '0' : '') + x.toString(16)).join('').toUpperCase());
	addr += 0x1000;
}

// mystery footer!
hex.push(tpl[13316]);
// EOF marker
hex.push(tpl[13317]);

fs.writeFileSync(outFn, hex.join('\n') + '\n');