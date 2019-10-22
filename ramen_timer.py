#coding: utf-8

import wiringpi as pi
import time
import sys

LED_PIN = 23
BUZZER_PIN = 22
SW_PIN = 24

pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.pinMode(BUZZER_PIN, pi.OUTPUT)
pi.pinMode(SW_PIN, pi.INPUT)
pi.pullUpDnControl(SW_PIN, pi.PUD_UP)

try:
    while True:
        if (pi.digitalRead(SW_PIN) == pi.LOW):
            # スイッチが押されたら、タイマを開始する（タイマが開始したことをLEDの点灯でユーザに知らせる仕様を追加）
            pi.digitalWrite(LED_PIN, pi.HIGH)
            time.sleep(10.0)
            # 180秒経過した！
            for i in range(15):
                pi.digitalWrite(LED_PIN, pi.HIGH)
                pi.digitalWrite(BUZZER_PIN, pi.HIGH)
                time.sleep(0.5)
                pi.digitalWrite(LED_PIN, pi.LOW)
                pi.digitalWrite(BUZZER_PIN, pi.LOW)
                time.sleep(0.5)
                if (pi.digitalRead(SW_PIN) == pi.LOW):
                    break   # スイッチが押されたらfor文を抜ける
            time.sleep(2.0)

except KeyboardInterrupt:
    # Ctrl-Cが押されたら、後始末をしてプログラムを終了する
    pi.digitalWrite(LED_PIN, pi.LOW)
    pi.digitalWrite(BUZZER_PIN, pi.LOW)
    sys.exit(0)  # Ctrl-Cが押されたら、後始末をしてプログラムを終了する
