#!/usr/bin/env python
import RPi.GPIO as GPIO           # import RPi.GPIO module
import time
import DataLayer as dl
from mfrc522 import SimpleMFRC522

fo = open("/home/pi/Mach_Number.txt")
mach_num = fo.read().strip()
mach_id = int(mach_num.replace("Mach", ""))
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
id = ""
prev_id=""
GPIO.output(relay, GPIO.LOW)
GPIO.output(red_led, GPIO.HIGH)
GPIO.output(green_led, GPIO.LOW)
future = time.monotonic() + 1


def blinkRed():
    GPIO.output(red_led, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.HIGH)


def blinkGreen():
    GPIO.output(red_led, GPIO.HIGH)
    GPIO.output(green_led, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(red_led, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(green_led, GPIO.HIGH)


def Main():
    global future, i, id, prev_id
    try:
        while True:  # making an infinite loop
            id, text = reader.read()  # waiting for id to be scanned
            while time.monotonic() < future:
                if reader.read():
                    if time.monotonic() > future:
                        id, string = reader.read()
                        GPIO.output(red_led, GPIO.LOW)
                        GPIO.output(green_led, GPIO.LOW)
                        break
                    else:
                        future = time.monotonic() + 1
            if dl.check_usr(str(id).strip()) or dl.check_lvl(str(id).strip()) is True:  # if id is correct
                if i == 0 and (dl.mach_used(int(id.strip())) or dl.check_lvl(str(id).strip())):  # check if the system is off
                    print("\nTurning on.")
                    GPIO.output(relay, GPIO.HIGH)
                    GPIO.output(green_led, GPIO.HIGH)
                    GPIO.output(red_led, GPIO.LOW)
                    prev_id = id
                    dl.use_mach(mach_id, str(id).strip())
                    id = ""
                    i = 1
                elif i == 1 and (id == prev_id or dl.check_lvl(str(id).strip())):  # check if the system is on
                    print("\nTurning off.")
                    GPIO.output(relay, GPIO.LOW)
                    GPIO.output(red_led, GPIO.HIGH)
                    GPIO.output(green_led, GPIO.LOW)
                    dl.use_mach(mach_id, None)
                    id = ""
                    i = 0
                elif i == 1:
                    blinkGreen()
                elif i == 0:
                    blinkRed()
                future = time.monotonic() + 1
            elif i == 1:
                blinkGreen()
                future = time.monotonic() + 1
            elif i == 0:
                blinkRed()
                future = time.monotonic() + 1

    except:
        GPIO.cleanup()


if __name__ == "__main__":
    Main()