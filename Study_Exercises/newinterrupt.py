import RPi.GPIO as GPIO
import random
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW) #RED
GPIO.setup(23,GPIO.OUT,initial=GPIO.LOW) #YELLOW
GPIO.setup(24,GPIO.OUT,initial=GPIO.LOW) #GREEN
GPIO.setwarnings(False)

i=1

def my_callback(channel):
    x = random.randint(1,3)
    print(x)
    global i
    i=2
    turn_on_led(x)

def turn_on_led(number):
    cases = {
        1: lambda: [GPIO.output(18,1), GPIO.output(23,0), GPIO.output(24,0)],
        2: lambda: [GPIO.output(23,1), GPIO.output(18,0), GPIO.output(24,0)],
        3: lambda: [GPIO.output(24,1), GPIO.output(18,0), GPIO.output(23,0)],
   }
    cases[number]()

GPIO.add_event_detect(21,GPIO.FALLING,callback=my_callback)

def toggling_leds():
   while True:
	GPIO.output(18,1)
	sleep(1)
	GPIO.output(23,1)
	sleep(1)
	GPIO.output(24,1)
	sleep(1)
	GPIO.output(18,0)
	sleep(1)
	GPIO.output(23,0)
	sleep(1)
	GPIO.output(24,0)
	sleep(1)
	if i > 1:
	    break
def main():
    try:
	while True:
	    toggling_leds()
    except KeyboardInterrupt:
	print("program terminated")
    finally:
	GPIO.cleanup()
if __name__=="__main__":
    main()
