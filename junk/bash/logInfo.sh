#!/bin/bash

touch log
date -u | tee log
who | tee log
uptime | tee log

exit 0