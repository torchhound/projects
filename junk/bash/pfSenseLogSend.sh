#!/bin/bash

echo "Enter IP: "
read IP
echo "Enter port: "
read port
clog var/log/filter.log > nc -u $IP $port
exit 0
