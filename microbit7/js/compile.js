#!/usr/bin/env node

// The old version of the microbit compiler allowed custom functions.
// The new one does not so this is a workaround.
var inlineFunctions = true;

var nativeFunctions = [
	'onStart',
	'onPressA', 'onPressB', 'onPressAandB',
	'onReleaseA', 'onReleaseB',
	'onShake',
	'onPressPin0', 'onPressPin1', 'onPressPin2',
	'onDeviceRing', 'onDeviceSMS', 'onDeviceShake',
	'onDeviceScreenOn', 'onDeviceScreenOff'
];

var fs = require('fs');
fs.readdir('templates', function (err, data) {
	if (err)
		return console.err(err);
	data.forEach(function (fn) {
		if (/\.js$/.test(fn)) fs.readFile('templates/' + fn, function (err, text) {
			if (err)
				return console.err(err);
			var functions = {
					'': []
				},
				currentFunction = functions[''],
				input = text.toString().split('\n'),
				vars = {
					'\\$': 'globals',
					'_': 'microbit'
				},
				fors = {},
				loops = [],
				inComment = false;
			for (var i = 0; i < input.length; ++i) {
				var line = input[i];

				// console.log(line)

				if (/^\s*\/\*.*\*\/\s*$/.test(line))
					continue;

				if (/^\s*\/\*/.test(line)) {
					inComment = true;
					continue;
				}
				if (inComment) {
					if (/\*\/\s*$/.test(line))
						inComment = false;
					continue;
				}

				if (/^\s*$/.test(line) || /^\s*\/\//.test(line))
					continue;

				if (/^function .*\(\) \{$/.test(line)) {
					var func = line.substr(9, line.length - 13);
					currentFunction = functions[func] = [];
					continue;
				}
				if (line == '}') {
					currentFunction = functions[''];
					continue;
				}

				for (var sub in vars)
					line = line.replace(new RegExp(sub, 'g'), vars[sub]);
				if (!/^#/.test(line)) {
					currentFunction.push(line);
				} else {
					var parts = line.split(' ').filter(function (part) {
						return part;
					});
					switch (parts[1]) {
						// TODO - check if loops with negative steps work OK
						case 'FOR':
							fors[parts[2]] = {
								to: parseInt(parts[6], 10),
								line: i,
								step: parts[8] ? parseInt(parts[8], 10) : 1
							};
							loops.push(parts[2]);
						case 'LET':
							vars[parts[2]] = parseInt(parts[4], 10);
							break;
						case 'NEXT':
							var loop = loops.pop();
							vars[loop] += fors[loop].step;
							if (vars[loop] != fors[loop].to) {
								loops.push(loop);
								i = fors[loop].line;
							} else {
								delete vars[loop];
								delete fors[loop];
							}
							break;
					}
				}
			}

			var out = [];
			// console.log(Object.keys(functions));

			// pushFuncContents('');

			for (var func in functions)
				if (!inlineFunctions || (nativeFunctions.indexOf(func) >= 0)) {
					out.push('function ' + func + '() {');
					pushFuncContents('');
					pushFuncContents(func);
					out.push('}');
					out.push('');
				}
			fs.writeFile('output/' + fn, out.join('\n'));

			function pushFuncContents(func) {
				functions[func].forEach(function(line) {
					if (inlineFunctions) {
						var func = line.replace(
							/^\s*([a-z0-9$_]+)\(\);\s*$/i,
							'$1');
						if ((func == line) || !functions[func])
							out.push(line);
						else
							pushFuncContents(func);
					} else
						out.push(line);
				});
			}
		});
	})
});