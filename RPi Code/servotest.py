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

        def write(self, angle):
                dc = angle*(upper-lower)/180 + middle
                self.p.ChangeDutyCycle(dc)

        def stop():
                self.p.stop()

GPIO.setmode(GPIO.BCM)

servoleg1m1 = Servo(18)
servoleg1m2 = Servo(23)
servoleg3m1 = Servo(24)
servoleg3m2 = Servo(25)
servoleg2m1 = Servo(4)
servoleg2m2 = Servo(17)
servoleg4m1 = Servo(27)
servoleg4m2 = Servo(22)

servoleg1m1.write(-0)
servoleg1m2.write(0)
servoleg2m1.write(0)
servoleg2m2.write(-0)
servoleg3m1.write(-0)
servoleg3m2.write(0)
servoleg4m1.write(0)
servoleg4m2.write(-0)

time.sleep(10)

GPIO.cleanup()




