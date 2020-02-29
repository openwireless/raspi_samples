#coding: utf-8

import sys
import time
import datetime
import cv2

image_path = '/home/pi/sample/images'

while True:
  now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
  cc = cv2.VideoCapture(0)    # Camera 0で撮影
  rr, img = cc.read()
  cv2.imwarite(now + ".jpg", img)
  cc.release()
  time.sleep(15)    # しばらく待つ
