from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.hflip = True

#Fotos
#camera.start_preview(alpha = 200)
#for i in range (5):
#    sleep(2)
#    camera.capture('./img_teste{i}.jpg'.format(i = i))
#
#camera.stop_preview()


#Video
camera.start_preview()
camera.start_recording('./video_teste.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
