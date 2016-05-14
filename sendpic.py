#!/usr/bin/python

import smtplib
import os
import socket

socket.setdefaulttimeout(10)

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

fromaddr = ('your mail')
toaddrs = ('destination mail')
attachment = '/tmp/image.jpg'

# Add the From: and To: headers at the start!
msg = MIMEMultipart()
msg['Subject'] = 'Got It !!!!!'
msg['From'] = 'RaspiTrap'
msg['To'] = 'Alain'

text = MIMEText("Check the Picture, we got a Mouse")
msg.attach(text)

fp = open(attachment, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', 'image.jpg')
img.add_header('Content-Disposition' , 'inline' , filename='image.jpg')
img.add_header('Content-Type', 'image/jpg')
msg.attach(img)

server = smtplib.SMTP('smtp-server')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
