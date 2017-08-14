#!/bin/bash

while getopts ":a:" opt
do
	case $opt  in
		a) 
			git add --all
			git remove *~
			git commit -m \"$optarg\"
			git push origin master
			;;
	esac
done
