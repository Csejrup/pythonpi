import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

y=input("Flash time: ")
x=input("Enter a Sleeping Time: ")

try:
    while True:	
        GPIO.output(18,GPIO.HIGH)
	GPIO.output(23,GPIO.LOW)
        sleep(y)
        GPIO.output(18,GPIO.LOW)
	GPIO.output(23,GPIO.HIGH)
        sleep(x)
except KeyboardInterrupt:
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
finally:
    GPIO.cleanup()     
