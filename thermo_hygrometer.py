# thermo_hygrometer.py

import wiringpi as pi
import time
import dht11
import i2c_lcd

pi.wiringPiSetupGpio()
i2c_lcd.lcd_init() 
sensor = dht11.DHT11(pin=4)

while True:
    result = sensor.read()
    if result.is_valid():
        i2c_lcd.lcd_clear() 
        line1 = "Temp: %d C" % result.temperature
        i2c_lcd.lcd_string(line1, i2c_lcd.LCD_LINE_1) 
        line2 = "Hum: %d %%" % result.humidity
        i2c_lcd.lcd_string(line2, i2c_lcd.LCD_LINE_2) 
    time.sleep(10)

