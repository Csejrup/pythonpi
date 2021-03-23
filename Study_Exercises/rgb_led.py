import RPi.GPIO as GPIO
import random
import threading
from time import sleep

#GPIO Setups
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
R=17
G=21
B=12
pins=[R,G,B] #B, G ; R



# Set all pins to output mode
def initialize_gpio_pins():
    for x in range(0, len(pins)):
	GPIO.setup(pins[x], GPIO.OUT, initial=GPIO.LOW)


def color_test(channel, frequency, speed, step):
    p = GPIO.PWM(channel, frequency)
    p.start(0)
    while True:
        for dutyCycle in range(0, 101, step):
            p.ChangeDutyCycle(dutyCycle)
            sleep(speed)
        for dutyCycle in range(100, -1, -step):
            p.ChangeDutyCycle(dutyCycle)
            sleep(speed)
 
 
def color_test_thread():
    threads = []
    threads.append(threading.Thread(target=color_test, args=(R, 500, 0.5, 3)))
    threads.append(threading.Thread(target=color_test, args=(G, 500, 0.5, 3)))
    threads.append(threading.Thread(target=color_test, args=(B, 500, 0.5, 3)))
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()

#this is main function
def main():
    try:
        while True:
	    initialize_gpio_pins()
	    color_test_thread()
    except KeyboardInterrupt:
        print("Program Terminated")
    finally:
        GPIO.cleanup()

#Runs Main Function
if __name__=="__main__":
    main()
    

