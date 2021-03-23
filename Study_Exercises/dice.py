import RPi.GPIO as GPIO
import random
from time import sleep
from threading import Timer

#GPIO Setups
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)

#Array of Pins 
pins=[18,23,24,16,20,12]
#Global Variable
i=1

#For loop that sets every pin to be an OUTPUT
for x in range(0, len(pins)):
	GPIO.setup(pins[x], GPIO.OUT, initial=GPIO.LOW)

#CallBack Function Executed, asynchronosly, when button is pressed
def my_callback(channel):
    x = random.randint(1,6)
    print(x)
    global i
    i = 2
    turn_on_led(x)

#Function that turns on 1 random LED and turns the rest off
def turn_on_led(number):
    cases = {
        1: lambda: [GPIO.output(18,1), GPIO.output(23,0), GPIO.output(24,0), GPIO.output(12,0), GPIO.output(16,0), GPIO.output(20,0)],
        2: lambda: [GPIO.output(18,1), GPIO.output(23,1), GPIO.output(24,0), GPIO.output(12,0), GPIO.output(16,0), GPIO.output(20,0)],
        3: lambda: [GPIO.output(18,1), GPIO.output(23,1), GPIO.output(24,1), GPIO.output(12,0), GPIO.output(16,0), GPIO.output(20,0)],
	4: lambda: [GPIO.output(18,1), GPIO.output(23,0), GPIO.output(24,1), GPIO.output(12,1), GPIO.output(16,1), GPIO.output(20,0)],
	5: lambda: [GPIO.output(18,1), GPIO.output(23,1), GPIO.output(24,1), GPIO.output(12,1), GPIO.output(16,1), GPIO.output(20,0)],
	6: lambda: [GPIO.output(18,1), GPIO.output(23,1), GPIO.output(24,1), GPIO.output(12,1), GPIO.output(16,1), GPIO.output(20,1)],
    }
    cases[number]()

#Event Detection on GPIO 21
GPIO.add_event_detect(21,GPIO.FALLING,callback=my_callback)

#Function that toggles between LEDs
def toggling_leds():
    while True:
        dice_no = random.randint(1,6)
	#t = Timer(5, turn_on_led, [dice_no])
	#t.start()
        turn_on_led(dice_no)
	print("You Rolled a: ",dice_no)
        sleep(1)
	if i > 1:
            sleep(2)
            break

#this is main function
def main():
    try:
        while True:
            toggling_leds()
    except KeyboardInterrupt:
        print("Program Terminated")
    finally:
        GPIO.cleanup()

#Runs Main Function
if __name__=="__main__":
    main()
    
