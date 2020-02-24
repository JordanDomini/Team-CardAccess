#!/usr/bin/env python
import RPi.GPIO as GPIO           # import RPi.GPIO module
import time
import DataLayer as dl
from mfrc522 import SimpleMFRC522


red_led = 10
green_led = 12
relay = 40
GPIO.setmode(GPIO.BOARD)            # choose BCM or BOARD
GPIO.setup(relay, GPIO.OUT)           # set a port/pin as an output
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT)


reader = SimpleMFRC522()
i = 0
GPIO.output(relay, 0)
GPIO.output(red_led, 1)
GPIO.output(green_led, 0)
future = time.monotonic() + 1


def Main():
    global future, i
    try:
        while True:  # making an infinite loop
            id, text = reader.read()  # waiting for id to be scanned
            while time.monotonic() < future:
                if reader.read():
                    if time.monotonic() > future:
                        id, string = reader.read()
                        GPIO.output(red_led, 0)
                        GPIO.output(green_led, 0)
                        break
                    else:
                        future = time.monotonic() + 1
            if reader.read():
                id, string = reader.read()
            if dl.check_usr(str(id).strip()) or dl.check_lvl(str(id).strip()) is True:  # if id is correct
                if i == 0:  # check if the system is off
                    print("\nTurning on.")
                    GPIO.output(relay, 1)
                    GPIO.output(green_led, 1)
                    GPIO.output(red_led, 0)
                    i = 1
                elif i == 1:  # check if the system is on
                    print("\nTurning off.")
                    GPIO.output(relay, 0)
                    GPIO.output(red_led, 1)
                    GPIO.output(green_led, 0)
                    i = 0
                else:
                    GPIO.output(31, 1)
                time.sleep(1)
                future = time.monotonic() + 1
    except:
        GPIO.cleanup()


if __name__ == "__main__":
    Main()