#!/bin/bash
#Bash script to be run for new machine
#The purpose of this script is to automatically set up the pi on the new unit
ssh pi@$1
sudo apt-get update
sudo apt-get upgrade
echo "dtparam=spi=on" >> /boot/config.txt #writes to file to enable spi
sudo apt-get install python3
sudo apt-get install python3-pip
pip install object-mapper
pip install SQLAlchemy
static ip_address=$1/24


