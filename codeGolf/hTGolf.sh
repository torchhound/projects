#!/bin/bash
#written for http://codegolf.stackexchange.com/questions/78886/hackertyper-net/78892
#http://stackoverflow.com/questions/6883363/read-input-in-bash-inside-a-while-loop
while read -r;do #conflicting reads
read -rsn1 d
if [ -n "$d" ]; then 
echo "$REPLY"
fi
done