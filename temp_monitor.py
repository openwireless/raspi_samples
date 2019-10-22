# temp_monitor.py

import wiringpi as pi
import time
import sys
import dht11
import requests
import ambient

pi.wiringPiSetupGpio()
dht11 = dht11.DHT11(pin=4)
am = ambient.Ambient(****, ‘'**********’) 

try:
    while True:
        r = dht11.read()
        if r.is_valid():
            r = am.send({"d1": r.temperature, "d2": r.humidity})
        time.sleep(10)
except KeyboardInterrupt:
    sys.exit(0)

