import RPi.GPIO as GPIO
import random
from time import sleep

led_pin=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setwarnings(False)
pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(100)

def main():
    try:
	while True:
            d=input("Enter Brightness (0 to 100: )")
	    duty=int(d)
	    pwm_led.ChangeDutyCycle(duty)
    except KeyboardInterrupt:
	print("program is terminated")
    finally:
	GPIO.cleanup()
#Runs Main Function
if __name__=="__main__":
    main()
