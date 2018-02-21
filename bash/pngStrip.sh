#!/bin/bash
echo "Enter complete path to folder: "
read folder
cd $folder
for file in *.png
do
	convert -strip $file
done

exit 0