import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #RED
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) #YELLOW
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) #GREEN

def turn_on_red():
    GPIO.output(16,1)

def turn_on_yellow():
    GPIO.output(20,1)

def turn_on_green():
    GPIO.output(21,1)

def switch_led(color):
    cases = {
	'red': lambda: GPIO.output(16,1),
	'yellow': lambda: GPIO.output(20,1),
	'green': lambda: GPIO.output(21,1),
	'stop': lambda: exit(),
    }
    cases[color]()
try:
    while True:
      # turn_on_red()
      # sleep(3)
      # turn_on_yellow()
      #	sleep(3)
      #	turn_on_green()
	input = raw_input("Insert red, yellow, green to light led or stop to stop program \n")
	switch_led(input)
except KeyboardInterrupt:
	print("Program is terminated!")
finally:
	GPIO.cleanup()	


