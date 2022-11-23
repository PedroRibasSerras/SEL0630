from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.hflip = True

#Foto
camera.start_preview(alpha = 200)
camera.annotate_text = "Grupo master blaster Boy, Drinker e Mussattinho\n11234328, 11299978 e 11234245"
sleep(10)
camera.capture('./img_grupo.jpg')
camera.stop_preview()


#Video
camera.start_preview()
camera.start_recording('./video_grupo.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
