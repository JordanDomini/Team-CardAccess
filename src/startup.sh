#!/bin/bash
#Bash script to be run on startup
#The purpose of this script is to automatically update and start our program when the raspberry pi is rebooted

git pull https://github.com/JordanDomini/Team-CardAccess

sudo python3 ~\Team-CardAccess\src\ImprovedPrototypeTest.py