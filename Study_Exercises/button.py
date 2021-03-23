import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
	if GPIO.input(21)==1:
	    print"Button Is Pressed"
	else:
	   print"Button is not pressed"
except keyboardInterrupt:
   print"program is now terminated"
finally:
   GPIO.cleanup()
