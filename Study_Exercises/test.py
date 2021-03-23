import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

com= raw_input("input command")
if com=="ON":
    GPIO.output(21,True)
else:
    GPIO.output(21,False)


