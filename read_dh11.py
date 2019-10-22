# read_dht11.py

import wiringpi as pi
import time
import dht11

pi.wiringPiSetupGpio()
sensor = dht11.DHT11(pin=4) 

while True:
    result = sensor.read()
    if result.is_valid():
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
    time.sleep(1)

