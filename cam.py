#!/usr/bin/python

print ('Start')

import time
import picamera

from instapush.instapush import Instapush, App
app = App(appid='55a77921a4c48ae561c2f8d5', secret='09708f9b77f3e8c1f7e13a16aeb9510b')
app.notify(event_name='catch',trackers={ 'got': 'A mouse is in the trap'})





with picamera.PiCamera() as camera:
        camera.led = False
        camera.resolution = (800,600)
        camera.vflip = True
        camera.hflip = False
#       camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
#       camera.capture('image.jpg')

	
        camera.capture('/tmp/image.jpg', quality=55)
#       camera.stop_preview()
# convert -pointsize 20 -fill yellow -draw "text 270,460 \"`date`\"" image.jpg
# exec(open(/root/cam.py).read())
print('Ready')

