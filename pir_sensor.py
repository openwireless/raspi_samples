# pir_sensor.py

import wiringpi as pi
import time

PIR_PIN = 18
pi.wiringPiSetupGpio()
pi.pinMode(PIR_PIN, pi.INPUT)

while True:
    if (pi.digitalRead(PIR_PIN) == pi.HIGH):
        print("A person was detected.")
        time.sleep(15)
    else:
         time.sleep(3) 

