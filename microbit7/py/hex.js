fs = require('fs')

fs.readFile('python-tetris.hex', (err, data) => {
	if (err) throw err;

	data.toString().split('\n').forEach((line, i) => {
		if (line[0] != ':') return;
		console.log(
			i + ':\t' +

			line.substr(1)

			+ '\t' +

			line.substr(9).trim()
				.split(/(<?..)/)
				.map(pair => pair && String.fromCharCode(parseInt(pair, 16)))
				.join('')
				.replace(/\s/g, '•'))
	});

});