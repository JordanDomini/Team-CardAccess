import RPi.GPIO as GPIO           # import RPi.GPIO module
import keyboard                   # using module keyboard
import time
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD
GPIO.setup(24, GPIO.OUT)           # set a port/pin as an output
i = 0
time.sleep(1)
try:
    while True:                       # making a loop
        if keyboard.is_pressed('o'):  # if o is pressed
            print("\nTurning on.")
            if i == 0:
                GPIO.output(24, 1)       # set port/pin value to 1/GPIO.HIGH/True
                i = 1
                time.sleep(1)
            else:
                GPIO.output(24, 0)  # set port/pin value to 0/GPIO.LOW/False
                i = 0
                time.sleep(1)
except:
    GPIO.cleanup()