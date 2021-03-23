import RPi.GPIO as GPIO
import time

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
BEEP = 21
TRIG = 23
ECHO = 24
BUTTON = 25
GREEN = 16
RED = 20
GPIO.setup(BEEP,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(GREEN,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(RED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(TRIG, False)


#Global Variables
minimum_height = 0

#User Input Function
def user_input():
    global minimum_height
    minimum_height = 0
    minimum_height = input("Enter a Minimum Height ")
    print("Minimum Height entered is: "+str(minimum_height))

#Callback Function for Reset of Program
#def reset_callback(channel):
#    global minimum_height
#    minimum_height = 0 
#    user_input()

#Height Check Function
def height_check():
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time() 
    pulse_duration = pulse_end - pulse_start
    customer_height = pulse_duration * 17150
    customer_height = round(customer_height, 2)   
    if(customer_height <  minimum_height):
	GPIO.output(BEEP,1)
	GPIO.output(RED,1)
	time.sleep(0.5)
	GPIO.output(BEEP,0)
	GPIO.output(RED,0)
	print"Height is under minimum: "+str(minimum_height)+"cm"
    elif(customer_height >= minimum_height):
	GPIO.output(GREEN,1)
	print"Height: "+str(customer_height)+"cm"
	time.sleep(0.5)
	GPIO.output(GREEN,0)

#GPIO.add_event_detect(BUTTON,GPIO.FALLING,callback=reset_callback)

#Main Function    
def main():
    try:
	while True:
	    user_input()
	    while minimum_height is not None:
	        height_check()
		if(GPIO.input(BUTTON) == GPIO.HIGH):
		    print("Button was Pushed,Program will Reset")
		    user_input()
    except KeyboardInterrupt:
	 print "Program terminated"
    finally:
	GPIO.cleanup()

#First Function to be Called in the Program
if __name__ == "__main__":
    main()    
