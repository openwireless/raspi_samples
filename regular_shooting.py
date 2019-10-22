# regular_shooting.py

import picamera
import datetime
from time import sleep
from PIL import Image, ImageDraw, ImageFont

camera = picamera.PiCamera()
image_root = "/home/pi/camera/image/"
font_file = "/home/pi/camera/OpenSans-Light.ttf"

for i in range(60*60*1):
    sleep(10.0)
    file_name = "{0:08}.jpg".format(i)
    print(file_name)
    camera.capture(image_root + file_name)
    font = ImageFont.truetype(font_file, 12)
    image = Image.open(image_root + file_name, 'r')
    draw = ImageDraw.Draw(image)
    draw.text((10, 10),str(datetime.datetime.now()), font=font , fill='#F00')
    image.save(image_root + file_name)

