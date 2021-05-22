# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO
from time import sleep
import daemon


class Speedy:
    in1_left = 25
    in2_left = 24
    en_left = 23

    in1_right = 16
    in2_right = 20
    en_right = 21

    temp1 = 0

    p_left = None
    p_right = None

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1_left, GPIO.OUT)
        GPIO.setup(self.in1_right, GPIO.OUT)
        GPIO.setup(self.in2_left, GPIO.OUT)
        GPIO.setup(self.in2_right, GPIO.OUT)
        GPIO.setup(self.en_left, GPIO.OUT)
        GPIO.setup(self.en_right, GPIO.OUT)
        GPIO.output(self.in1_left, GPIO.LOW)
        GPIO.output(self.in1_right, GPIO.LOW)
        GPIO.output(self.in2_left, GPIO.LOW)
        GPIO.output(self.in2_right, GPIO.LOW)
        p_left = GPIO.PWM(self.en_left, 1000)
        p_right = GPIO.PWM(self.en_right, 1000)

        p_left.start(25)
        p_right.start(25)
        print("\n")
        print("The default speed & direction of motor is LOW & Forward.....")
        print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
        print("\n")

    def run(self):
        while True:
            print("Howdy!  Whoop!")
            sleep(10)


    def start(self):
        print("start")
        if (self.temp1 == 1):
            GPIO.output(self.in1_left, GPIO.HIGH)
            GPIO.output(self.in2_left, GPIO.LOW)
            GPIO.output(self.in1_right, GPIO.HIGH)
            GPIO.output(self.in2_right, GPIO.LOW)
            print("backward")
        else:
            GPIO.output(self.in1_left, GPIO.LOW)
            GPIO.output(self.in2_left, GPIO.HIGH)
            GPIO.output(self.in1_right, GPIO.LOW)
            GPIO.output(self.in2_right, GPIO.HIGH)
            print("forward")

    def stop(self):
        print("stop")
        GPIO.output(self.in1_left, GPIO.LOW)
        GPIO.output(self.in1_right, GPIO.LOW)
        GPIO.output(self.in2_left, GPIO.LOW)
        GPIO.output(self.in2_right, GPIO.LOW)

    def backward(self):
        print("backward")
        GPIO.output(self.in1_left, GPIO.HIGH)
        GPIO.output(self.in2_left, GPIO.LOW)
        GPIO.output(self.in1_right, GPIO.HIGH)
        GPIO.output(self.in2_right, GPIO.LOW)
        self.p_left.ChangeDutyCycle(50)
        self.p_right.ChangeDutyCycle(50)
        self.temp1 = 1

    def forward(self, speed=50):
        print("forward")
        GPIO.output(self.in1_left, GPIO.LOW)
        GPIO.output(self.in2_left, GPIO.HIGH)
        GPIO.output(self.in1_right, GPIO.LOW)
        GPIO.output(self.in2_right, GPIO.HIGH)
        self.p_left.ChangeDutyCycle(speed)
        self.p_right.ChangeDutyCycle(speed)
        self.temp1 = 0

    def low(self):
        print("low")
        self.p_left.ChangeDutyCycle(25)
        self.p_right.ChangeDutyCycle(25)

    def medium(self):
        print("medium")
        self.p_left.ChangeDutyCycle(50)
        self.p_right.ChangeDutyCycle(50)

    def high(self):
        print("high")
        self.p_left.ChangeDutyCycle(75)
        self.p_right.ChangeDutyCycle(75)

    def super_speed(self):
        print("SUPER SPEED!!!")
        self.p_left.ChangeDutyCycle(100)
        self.p_right.ChangeDutyCycle(100)

    def right(self):
        print("right")
        self.p_left.ChangeDutyCycle(15)
        self.p_right.ChangeDutyCycle(85)

    def left(self):
        print("left")
        self.p_left.ChangeDutyCycle(85)
        self.p_right.ChangeDutyCycle(15)

    def left_turn(self):
        print("left turn")
        GPIO.output(self.in1_left, GPIO.LOW)
        GPIO.output(self.in2_left, GPIO.HIGH)
        GPIO.output(self.in1_right, GPIO.HIGH)
        GPIO.output(self.in2_right, GPIO.LOW)
        self.p_left.ChangeDutyCycle(75)
        self.p_right.ChangeDutyCycle(75)

    def right_turn(self):
        print("right turn")
        GPIO.output(self.in1_left, GPIO.HIGH)
        GPIO.output(self.in2_left, GPIO.LOW)
        GPIO.output(self.in1_right, GPIO.LOW)
        GPIO.output(self.in2_right, GPIO.HIGH)
        self.p_left.ChangeDutyCycle(75)
        self.p_right.ChangeDutyCycle(75)

    def joystick(self, right, left):
        if right >= 0:
            GPIO.output(self.in1_right, GPIO.LOW)
            GPIO.output(self.in2_right, GPIO.HIGH)
        else:
            GPIO.output(self.in1_right, GPIO.HIGH)
            GPIO.output(self.in1_right, GPIO.LOW)
        if left >= 0:
            GPIO.output(self.in1_left, GPIO.LOW)
            GPIO.output(self.in2_left, GPIO.HIGH)
        else:
            GPIO.output(self.in1_left, GPIO.HIGH)
            GPIO.output(self.in2_left, GPIO.LOW)
        self.p_left.ChangeDutyCycle(abs(left))
        self.p_right.ChangeDutyCycle(abs(right))


    def exit(self):
        GPIO.cleanup()
        print("GPIO Clean up")

speedy = Speedy()

if __name__ == '__main__':
    with daemon.DaemonContext():
        speedy.run()