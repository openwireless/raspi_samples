# hello.py

import wiringpi as pi
import time
import i2c_lcd

pi.wiringPiSetupGpio()

i2c_lcd.lcd_init()
i2c_lcd.lcd_string("Hello, world!", i2c_lcd.LCD_LINE_1)
i2c_lcd.lcd_string(" with Ras-pi", i2c_lcd.LCD_LINE_2)
time.sleep(30)
i2c_lcd.lcd_clear()

