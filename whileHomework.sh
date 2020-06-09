#!/bin/bash

echo -n"Insert a, b, c or d for a message:"

valid=0

while
[ $valid == 0 ]
do 

	read ans 
	case $ans in 
	a|A	   )	echo "A for apple"
			valid=1
			;;
	b|B	   )	echo "B for banana"
			valid=1
			;;
	c|C	   )	echo "C for cat"
			valid=1
			;;
	d|D 	   )	echo "D for dog
			valid=1
			;;
	*	   )    echo Please enter a, b, c or d;;
	esac
done
