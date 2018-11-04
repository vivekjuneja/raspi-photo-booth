from PIL import Image, ImageDraw, ImageFont
import picamera
import time

IMAGE_WIDTH      = 640
IMAGE_HEIGHT     = 480
SCREEN_WIDTH     = 640
SCREEN_HEIGHT    = 480
overlay_renderer = None


def addPreviewOverlay(camera, xcoord,ycoord,fontSize,overlayText):
    global overlay_renderer
    img = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.font = ImageFont.truetype(
                    "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",fontSize)
    draw.text((xcoord,ycoord), overlayText, (255, 20, 147))

    if not overlay_renderer:
        # Note: The call to add_overlay has changed since picamera v.1.10.
        # If you have a new version of picamera, then please change the
        # first parameter to:  img.tobytes()
        #
        overlay_renderer = camera.add_overlay(img.tobytes(),
                                              layer=3,
                                              size=img.size,
                                              alpha=128);
    else:
        overlay_renderer.update(img.tobytes())


'''
camera = picamera.PiCamera()
camera.start_preview()
addPreviewOverlay(150,200,100,"smile!   :)")
time.sleep(3)
camera.close()
'''
