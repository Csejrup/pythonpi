import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#RIGHT SIDE
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #RED
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) #YELLOW
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) #GREEN
#LEFT SIDE
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #RED
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) #YELLOW
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) #GREEN

try:
    while True:
        GPIO.output(18,1)
	GPIO.output(16,1)
        sleep(1)
	GPIO.output(16,0)
	GPIO.output(20,1)
	sleep(1)
	GPIO.output(20,0)
	GPIO.output(21,1)
	sleep(5)
	GPIO.output(21,0)
	GPIO.output(20,1)
	sleep(1)
	GPIO.output(20,0)
	GPIO.output(16,1)
	sleep(1)
	GPIO.output(18,0)
	GPIO.output(23,1)
	sleep(1)
	GPIO.output(23,0)
	GPIO.output(24,1)
	sleep(5)
	GPIO.output(24,0)
	GPIO.output(23,1)
	sleep(1)
	GPIO.output(23,0)
except KeyboardInterrupt:
	print "Program is Terminated"
finally:
    GPIO.cleanup()
    
