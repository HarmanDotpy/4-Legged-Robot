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


leg1m1 = Servo(18)
leg1m2 = Servo(23)
leg3m1 = Servo(24)
leg3m2 = Servo(25)
leg2m1 = Servo(4)
leg2m2 = Servo(17)
leg4m1 = Servo(27)
leg4m2 = Servo(22)

leg1m1.write(-0)
leg1m2.write(0)
leg2m1.write(0)
leg2m2.write(-0)
leg3m1.write(-0)
leg3m2.write(0)
leg4m1.write(0)
leg4m2.write(-0)
time.sleep(2)

angs1 = [0 for x in range(100)]
angs2 = [0 for x in range(100)]

f = open("tilt_8.txt","r")
for t in range(100):
    str =  f.readline()
    val = str.split()
    angs1[t] = float(val[0])
    angs2[t] = float(val[1])

ang1 = [0 for x in range(100)]
ang2 = [0 for x in range(100)]
f2 = open("16_5.txt","r")
for t in range(100):
    str =  f2.readline()
    val = str.split()
    ang1[t] = float(val[0])
    ang2[t] = float(val[1])      

while(True):
    for t in range(25):
        leg1m1.write(ang1[t])
        leg1m2.write(180+ang2[t])
        leg2m1.write(-ang1[(t+50)%100])
        leg2m2.write(-180-ang2[(t+50)%100])
        leg3m1.write(angs1[(t+75)%100])
        leg3m2.write(180+angs2[(t+75)%100])
        leg4m1.write(-ang1[(t+25)%100])
        leg4m2.write(-180-ang2[(t+25)%100])
        time.sleep(0.02)
        
    while(1):
        t = 25
        leg1m1.write(ang1[t])
        leg1m2.write(180+ang2[t])
        leg2m1.write(-ang1[(t+50)%100])
        leg2m2.write(-180-ang2[(t+50)%100])
        leg3m1.write(angs1[(t+75)%100])
        leg3m2.write(180+angs2[(t+75)%100])
        leg4m1.write(-ang1[(t+25)%100])
        leg4m2.write(-180-ang2[(t+25)%100])

GPIO.cleanup()



