#!/bin/bash

rm *scriptcleaned
for i in `seq 1 10`
do
	cat $i'script' | python extract_clean.py > $i'scriptcleaned'
done
