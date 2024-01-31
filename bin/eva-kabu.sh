#!/bin/bash
DATE=$(date '+%Y%m%d-%H%M%S')
source ~/.eva-kabu.pwd
python3.10 /home/evakichi/eva-kabu/py/dailycheck.py 2>&1 |tee /var/log/eva-kabu/${DATE}.log
