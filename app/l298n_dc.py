# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
from time import sleep

in1_left = 25
in2_left = 24
en_left = 23

in1_right = 16
in2_right = 20
en_right = 21

temp1 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1_left, GPIO.OUT)
GPIO.setup(in1_right, GPIO.OUT)
GPIO.setup(in2_left, GPIO.OUT)
GPIO.setup(in2_right, GPIO.OUT)
GPIO.setup(en_left, GPIO.OUT)
GPIO.setup(en_right, GPIO.OUT)
GPIO.output(in1_left, GPIO.LOW)
GPIO.output(in1_right, GPIO.LOW)
GPIO.output(in2_left, GPIO.LOW)
GPIO.output(in2_right, GPIO.LOW)
p_left = GPIO.PWM(en_left, 1000)
p_right = GPIO.PWM(en_right, 1000)

p_left.start(25)
p_right.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while (1):

    x = raw_input()

    if x == 'r':
        print("run")
        if (temp1 == 1):
            GPIO.output(in1_left, GPIO.HIGH)
            GPIO.output(in2_left, GPIO.LOW)
            GPIO.output(in1_right, GPIO.HIGH)
            GPIO.output(in2_right, GPIO.LOW)
            print("backward")
            x = 'z'
        else:
            GPIO.output(in1_left, GPIO.LOW)
            GPIO.output(in2_left, GPIO.HIGH)
            GPIO.output(in1_right, GPIO.LOW)
            GPIO.output(in2_right, GPIO.HIGH)
            print("forward")
            x = 'z'


    elif x == 's':
        print("stop")
        GPIO.output(in1_left, GPIO.LOW)
        GPIO.output(in1_right, GPIO.LOW)
        GPIO.output(in2_left, GPIO.LOW)
        GPIO.output(in2_right, GPIO.LOW)
        x = 'z'

    elif x == 'b':
        print("backward")
        GPIO.output(in1_left, GPIO.HIGH)
        GPIO.output(in2_left, GPIO.LOW)
        GPIO.output(in1_right, GPIO.HIGH)
        GPIO.output(in2_right, GPIO.LOW)
        p_left.ChangeDutyCycle(50)
        p_right.ChangeDutyCycle(50)
        temp1 = 1
        x = 'z'

    elif x == 'f':
        print("forward")
        GPIO.output(in1_left, GPIO.LOW)
        GPIO.output(in2_left, GPIO.HIGH)
        GPIO.output(in1_right, GPIO.LOW)
        GPIO.output(in2_right, GPIO.HIGH)
        p_left.ChangeDutyCycle(50)
        p_right.ChangeDutyCycle(50)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        p_left.ChangeDutyCycle(25)
        p_right.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'm':
        print("medium")
        p_left.ChangeDutyCycle(50)
        p_right.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'h':
        print("high")
        p_left.ChangeDutyCycle(75)
        p_right.ChangeDutyCycle(75)
        x = 'z'

    elif x == 'ss':
        print("SUPER SPEED!!!")
        p_left.ChangeDutyCycle(100)
        p_right.ChangeDutyCycle(100)
        x = 'z'

    elif x == 'turbo':
        print("TURBO SPEED!!!")
        p_left.ChangeDutyCycle(150)
        p_right.ChangeDutyCycle(150)
        x = 'z'

    elif x == 'rr':
        print("right")
        p_left.ChangeDutyCycle(15)
        p_right.ChangeDutyCycle(85)
        x = 'z'

    elif x == 'll':
        print("left")
        p_left.ChangeDutyCycle(85)
        p_right.ChangeDutyCycle(15)
        x = 'z'

    elif x == 'lt':
        print("left turn")
        GPIO.output(in1_left, GPIO.LOW)
        GPIO.output(in2_left, GPIO.HIGH)
        GPIO.output(in1_right, GPIO.HIGH)
        GPIO.output(in2_right, GPIO.LOW)
        p_left.ChangeDutyCycle(75)
        p_right.ChangeDutyCycle(75)
        x = 'z'


    elif x == 'rt':
        print("right turn")
        GPIO.output(in1_left, GPIO.HIGH)
        GPIO.output(in2_left, GPIO.LOW)
        GPIO.output(in1_right, GPIO.LOW)
        GPIO.output(in2_right, GPIO.HIGH)
        p_left.ChangeDutyCycle(75)
        p_right.ChangeDutyCycle(75)
        x = 'z'


    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")