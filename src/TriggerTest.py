import RPi.GPIO as GPIO           # import RPi.GPIO module
import keyboard                   # using module keyboard
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD
GPIO.setup(7, GPIO.OUT)           # set a port/pin as an output
GPIO.setwarnings(False)
i = 0

while True:                       # making a loop
    try:                          # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed(' '):  # if key 'q' is pressed
            if i == 0:
                GPIO.output(7, 1)       # set port/pin value to 1/GPIO.HIGH/True
                i = 1
                break             # finishing the loop
            else:
                GPIO.output(7, 0)  # set port/pin value to 0/GPIO.LOW/False
                i = 0
                break             # finish the loop
        else:
            pass
    except:
        break                     # if user pressed a key other than the given key the loop will break