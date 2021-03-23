
import time
import datetime
import adafruit_am2320
import board
import busio
import RPi.GPIO as GPIO
i2c = busio.I2C(board.SCL, board.SDA)
am2320 = adafruit_am2320.AM2320(i2c)

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW) #RED
GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW) #GREEN
GPIO.setwarnings(False)
#Global Variables
user_time = 0
user_mes  = 0
count = 0
time_stamp = 0
print("Logging temperature and humidity to log file")

initial_time = time.monotonic()

def user_input():
    global user_mes
    user_mes = input("Enter how many iterations the system should log: ")
    global user_time
    user_time = input("Enter how often to log data (seconds): ")

def restart():
    global user_mes
    user_mes = 0
    global user_time
    user_time = 0
    global count
    count = 0
    global time_stamp
    time_stamp = 0
    main()

def main():
    user_input()
    while user_mes != 0:
        try:
            global count
            while count <= int(user_mes):
               # print(user_mes)
                with open("datalogging.txt", "a") as sdc:
                    temperature = am2320.temperature
                    humidity = am2320.relative_humidity
                    current_time = time.monotonic()
                    global time_stamp
                    time_stamp = current_time - initial_time
                    now = datetime.datetime.now()
                    print("Seconds since current data log started:", int(time_stamp))
                    print("Date and Time:",now.strftime("%Y-%m-%d %H:%M:%S"))
                    print("Temperature:", temperature)
                    print("Humidity:", humidity)
                    print()
                    sdc.write("{},{}, {}, {}\n".format(
                        int(time_stamp),now.strftime("%Y-%m-%d %H:%M:%S"), temperature,
                        humidity)
                             )
                    GPIO.output(21,1)
                    time.sleep(int(user_time))
                    count = count + 1
            if(count >= int(user_mes)):
                GPIO.output(20,1)
                GPIO.output(21,0)
                print("System is no longer logging Data")
                end_input = input("Type RESTART to restart the Program or EXIT to exit the program: ")
                if(end_input == "RESTART"):
                    restart()
                elif(end_input == "EXIT"):
                   print("Program is terminated")
                   break 
        except OSError:
            pass
        except RuntimeError:
            pass
#Runs Main Function
if __name__=="__main__":
    main()

