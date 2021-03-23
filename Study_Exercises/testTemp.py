import board
import busio
import adafruit_am2320
import time

i2c=busio.I2C(board.SCL,board.SDA)

def sensor_read():
    sensor = adafruit_am2320.AM2320(i2c)
    print("Humidity {0}%".format(sensor.relative_humidity))
    print("Temperature: {0}C".format(sensor.temperature))
    for x in range(11):
        print(x)
        time.sleep(1)
    

def main():
    try:
        while True:
            sensor_read()
    except KeyboardInterrupt:
        print("program terminated")
    finally:
        print("yes terminated")
	

#Runs Main Function
if __name__=="__main__":
    main()
