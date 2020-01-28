#!/bin/bash
apt update
apt-get install vnstat vnstati
vnstat -u -i eth0
/etc/init.d/vnstat start
wget https://raw.githubusercontent.com/4D4937/traffic/master/traffic.py
echo "*/30 * * * * root python /root/traffic.py" >> /etc/crontab
