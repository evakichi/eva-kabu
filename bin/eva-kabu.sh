#!/bin/bash
DATE=$(date '+%Y%m%d-%H%M%S')
export NUM_OF_THREADS=$(grep processor /proc/cpuinfo | wc -l)
source  ${HOME}/.eva-kabu.passwd
time python3 ${HOME}/eva-kabu/py/dailycheck.py 2>&1 |tee /var/log/eva-kabu/${DATE}.log
