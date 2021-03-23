import board
import busio
import adafruit_am2320
import time

i2c = busio.I2C(board.SCL, board.SDA)
while True:
  sensor = adafruit_am2320.AM2320(i2c)

  print('Humidity: {0}%'.format(sensor.relative_humidity))
  print('Temperature: {0}C'.format(sensor.temperature))
  time.sleep(1)

