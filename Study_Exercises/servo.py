import RPi.GPIO as GPIO
servo_pin=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm_servo=GPIO.PWM(servo_pin,50)
pwm_servo.start(2.5)

def servo_duty():
    d=input("enter %")
    duty=int(d)
    pwm_servo.ChangeDutyCycle(duty)

#this is main function
def main():
    try:
        while True:
	    d=input("enter %: ")
	    duty=int(d)
	    pwm_servo.ChangeDutyCycle(duty)
            servo_duty()
    except KeyboardInterrupt:
        print("Program Terminated")
    finally:
	pwm_servo.stop()
        GPIO.cleanup()

#Runs Main Function
if __name__=="__main__":
    main()
