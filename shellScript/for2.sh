#!/bin/sh

for i in {1..10}
do
	echo " $i 回目のループです."
done

echo

for (( i = 0 ; i < 10 ; i++ ))
do
	echo " $i 回目のループです."
done
