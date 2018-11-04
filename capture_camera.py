from time import sleep
from picamera import PiCamera
import sys
import subprocess
image_file_name = "img"
fileName="final_image.jpg"
import overlay_text

def capture_image(camera, img):
	# Explicitly open a new file called my_image.jpg
	my_file = open((image_file_name+img+".jpg"), 'wb')
	camera.capture(my_file)
	my_file.close()


camera = PiCamera()
camera.start_preview()
for i in range(0,4):
	overlay_text.addPreviewOverlay(camera, 150,200,100,"smile!   :)")
	sleep(2)
	capture_image(camera, str(i))
camera.stop_preview()
camera.close()
subprocess.call(["montage",
                    image_file_name+"0.jpg", image_file_name+"1.jpg",image_file_name+"2.jpg",image_file_name+"3.jpg",
                     "-geometry", "+2+2",
                     fileName])


