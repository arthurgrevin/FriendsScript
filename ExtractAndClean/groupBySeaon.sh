#!/bin/bash

for i in  `seq 1 10`;
do 
	if [ $i -lt 10 ]
	then cat 0$i*.html > $i'script'
	else cat $i*.html > $i'script'
	fi
done
