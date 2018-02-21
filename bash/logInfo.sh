#!/bin/bash

touch log
date -u | tee -a log
who | tee -a log
uptime | tee -a log

exit 0