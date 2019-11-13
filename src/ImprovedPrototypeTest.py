#!/usr/bin/env python
import RPi.GPIO as GPIO           # import RPi.GPIO module
import time
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BOARD)            # choose BCM or BOARD
GPIO.setup(26, GPIO.OUT)           # set a port/pin as an output
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

reader = SimpleMFRC522()
i = 0
future = time.time() + 2
time.sleep(2)

try:
    while True:                       # making an infinite loop
        id, text = reader.read()      # waiting for id to be scanned
        while time.time() < future:
            if reader.read():
                future = time.time() + 2
        if '470495939090' in str(id):        # if id is correct
            if i == 0:                # check if the system is off
                print("\nTurning on.")
                GPIO.output(26, 0)       # set port/pin value to 1/GPIO.HIGH/True
                GPIO.output(29, 0)
                i = 1
            elif i == 1:             # check if the system is on
                print("\nTurning off.")
                GPIO.output(26, 1)  # set port/pin value to 0/GPIO.LOW/False
                GPIO.output(29, 1)
                i = 0
            else:
                GPIO.output(31, 1)
        future = time.time()
except:
    GPIO.cleanup()