import RPi.GPIO as GPIO
import time as time

lower = 3.25
middle = 7.5
upper = 11.75
frequency = 50

class Servo:
	
        def __init__(self, channel):
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(channel, GPIO.OUT) 
                self.p = GPIO.PWM(channel, frequency)
                self.p.start(middle)

        def write(angle):
                dc = angle*(upper-lower)/180 + middle
                self.p.ChangeDutyCycle(dc)

        def stop():
                self.p.stop()  


