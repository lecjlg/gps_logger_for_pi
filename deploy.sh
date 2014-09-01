#!/bin/bash

#Script to create directories and install packages required for the GPS PI logger
cd /home/pi
mkdir -p /opt/scripts
mkdir -p /home/pi/gpslog

#install packages vim gpsd and gpsd-clients 
apt-get install -y vim gpsd gpsd gpsd-clients minicom screen ntpdate 

#Grab sirfdump from git make and create a symlink to in /usr/bin

git clone https://github.com/illarionov/sirfdump
cd sirfdump
make
sudo ln -sf /home/pi/sirfdump/sirfdump /usr/bin/sirfdump











