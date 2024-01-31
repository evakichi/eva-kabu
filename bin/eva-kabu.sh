#!/bin/bash
DATE=$(date '+%Y%m%d-%H%M%S')
source ~/.eva-kabu.passwd
python3.10 ${HOME}/eva-kabu/py/dailycheck.py 2>&1 |tee /var/log/eva-kabu/${DATE}.log
