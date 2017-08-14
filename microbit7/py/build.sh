#!/usr/bin/env sh

cd games

for f in *.py
do
	if [ "$f" != "global.py" ]
	then
		echo "Processing $f file..."
		../py2hex.js $f ../global.py
		echo "Done."
	fi
done

cd ..