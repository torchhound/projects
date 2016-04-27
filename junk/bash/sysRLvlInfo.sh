#!/bin/bash

echo $HOME
echo $TERM
echo "Enter a run level to display: "
read runlvl
ls /etc/rc$runlvl.d/*
exit 0