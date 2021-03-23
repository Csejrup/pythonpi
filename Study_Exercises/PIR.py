import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN)

print('Starting up the PIR Module')
time.sleep(1)
print ('Ready')



def main():
    try:
        while True:
          if GPIO.input(23)==False:
            print("False")
          if GPIO.input(23)==True:
            print("True")
          if GPIO.input(23):
            print('Motion Detected')
          time.sleep(5)
    except KeyboardInterrupt:
        print("Program Terminated")
    finally:
        GPIO.cleanup()
#Runs Main Function
if __name__=="__main__":
    main()
    
