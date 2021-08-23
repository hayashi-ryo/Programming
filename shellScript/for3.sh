#!/bin/sh

for file in $(ls -l)
do
	echo $file
done

echo

for file in `ls`
do
	echo $file
done
