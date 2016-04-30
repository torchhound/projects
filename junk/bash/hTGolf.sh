#!/bin/bash
#written for http://codegolf.stackexchange.com/questions/78886/hackertyper-net/78892
#http://stackoverflow.com/questions/6883363/read-input-in-bash-inside-a-while-loop
while read -r;do
read -rsn1 inp #conflicting reads
if ; then #need a way to check if anything is in inp
echo "$REPLY"
fi
done