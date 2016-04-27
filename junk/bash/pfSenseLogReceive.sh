#!/bin/bash

touch pfSenseLog
echo "Enter port: "
read port
nc -lp $port > pfSenseLog
exit 0