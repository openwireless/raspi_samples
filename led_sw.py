# led_sw.py

import wiringpi as pi
import time

LED_PIN = 23
SW_PIN = 24
pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.pinMode(SW_PIN, pi.INPUT)
pi.pullUpDnControl(SW_PIN, pi.PUD_UP)

while True:
    if (pi.digitalRead(SW_PIN) == pi.LOW):
        pi.digitalWrite(LED_PIN, pi.HIGH)
    else:
        pi.digitalWrite(LED_PIN, pi.LOW) 
    time.sleep(0.1)

