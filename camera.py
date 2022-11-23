from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.hflip = True


camera.start_preview(alpha = 200)
for i in range (5):
    sleep(2)
    camera.capture('./img_teste{i}.jpg'.format(i = i))

camera.stop_preview()

