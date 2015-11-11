#!/bin/bash
echo "Enter path to folder: "
read folder
cd folder
for file in *.csv
do
	set lineCount = wc -l < $file
	lineCount - 1
	for line in lineCount
	do
		awk -F, -v OFS=, '{$9 = ",,"};1' $file 
	done
done