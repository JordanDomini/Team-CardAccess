#!/usr/bin/env python
import RPi.GPIO as GPIO           # import RPi.GPIO module
import time
import DataLayer as dl
from mfrc522 import SimpleMFRC522


GPIO.setmode(GPIO.BOARD)            # choose BCM or BOARD
GPIO.setup(26, GPIO.OUT)           # set a port/pin as an output
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

reader = SimpleMFRC522()
i = 0
GPIO.output(26, 1)
future = time.monotonic() + 1


def Main():
    try:
        while True:  # making an infinite loop
            id, text = reader.read()  # waiting for id to be scanned
            while time.monotonic() < future:
                if reader.read():
                    if time.monotonic() < future:
                        id, string = reader.read()
                        break
                    else:
                        future = time.monotonic() + 1
            if dl.check_usr(str(id).strip()) or dl.check_lvl(str(id).strip()) is not 0:  # if id is correct
                if i == 0:  # check if the system is off
                    print("\nTurning on.")
                    GPIO.output(26, 0)
                    GPIO.output(29, 0)
                    i = 1
                elif i == 1:  # check if the system is on
                    print("\nTurning off.")
                    GPIO.output(26, 1)
                    GPIO.output(29, 1)
                    i = 0
                else:
                    GPIO.output(31, 1)
                time.sleep(1)
                future = time.monotonic() + 1
    except:
        GPIO.cleanup()


if __name__ == "__main__":
    Main()