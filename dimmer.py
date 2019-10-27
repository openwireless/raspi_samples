# dimmer.py

import wiringpi as pi
import mcp3008
import time

LED_PIN = 23
CH = 0
pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.softPwmCreate(LED_PIN, 0, 100)

while True:
    v = mcp3008.readAdcValue(CH) / 10
    pi.softPwmWrite(LED_PIN, int(v))  
    time.sleep(0.1)

