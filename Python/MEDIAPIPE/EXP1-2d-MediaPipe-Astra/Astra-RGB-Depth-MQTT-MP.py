bViewFeed = True
frameRate = 30		# frames per second
width = 640 		# Width of image
height = 480		# height of image
minIntensity = 200

minDepth = 10
maxDepth = 3000

bZeroMask = True
nErosions = 3

bAutoExposure = False
exposure = 100

# ======= Smoothing Parameters =======
# How much smoothing (and latency) you want
# 0 --> no smoothing, no latency
# 0.9 --> lots of smoothing, lots of latency
easingParam = 0.3

# Import modules of interest
import cv2
import numpy as np
from primesense import openni2
from primesense import _openni2 as c_api
import time
import imutils
from pythonosc import osc_message_builder
from pythonosc import udp_client
import ctypes
import paho.mqtt as mqtt
from paho.mqtt import client
from HandTrackingModule import handDetector
import math


client = client.Client()
client.connect("test.mosquitto.org", 1883)
pTime = time.time()
#Utils
def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray.astype(np.uint8)

# Initialize OpenNI with its libraries
openni2.initialize() #The OpenNI2 Redist folder

# Open a device
dev = openni2.Device.open_any()
# Check to make sure it's not None

# Open two streams: one for color and one for depth
depth_stream = dev.create_depth_stream()
depth_stream.start()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = width, resolutionY = height, fps = frameRate))

color_stream = dev.create_color_stream()
color_stream.start()
color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = width, resolutionY = height, fps = frameRate))

# Register both streams so they're aligned
dev.set_image_registration_mode(c_api.OniImageRegistrationMode.ONI_IMAGE_REGISTRATION_DEPTH_TO_COLOR);
# Set exposure settings
if (color_stream.camera != None):
    color_stream.camera.set_auto_exposure(bAutoExposure)
    color_stream.camera.set_exposure(exposure)
    # Wait for these settings to take effect
    time.sleep(1)

# Main loop
lastUpdateTime = time.time()
bPrevData = False
px = 0
py = 0
pz = 0
detector = handDetector()
while True:
    
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    depthPix = np.frombuffer(frame_data, dtype=np.uint16)
    depthPix.shape = (height, width)
    frame = color_stream.read_frame()
    frame_data = frame.get_buffer_as_uint8()
    colorPix = np.frombuffer(frame_data, dtype=np.uint8)
    colorPix.shape = (height, width, 3)
    colorPix = np.flip(colorPix, 2)
    ret,thresh = cv2.threshold(grayPix, minIntensity, 255,cv2.THRESH_BINARY)
    img2 = None
    avgDist = np.average(depthPix)
    colorPix = np.array(colorPix)
    
    colorPix = detector.findHands(colorPix,draw = True)
    lmList= detector.findPosition(colorPix,draw =  True)
    
    
    
    zs = []
    xs = []
    ys = []    
    pts = []
    for i,lm in enumerate(lmList):
        
        x,y,z = openni2.convert_depth_to_world(depth_stream,lm[1],lm[2],avgDist)
        z /= 10.0
        if not bPrevData:
            bPrevData = True
            px = x
            py = y
            pz = z
            x = x*(1.0-easingParam) + px*easingParam
            y = y*(1.0-easingParam) + py*easingParam
            z = z*(1.0-easingParam) + pz*easingParam
        # now, x,y,z are all in mm
        px = x
        py = y
        pz = z
        
        xs.append(lm[1])
        ys.append(lm[2])   
        zs.append(z)   
        pts.append(",".join(map(str,[x,y,z])))       
        #client.publish("LM/%i"%(i),"%i:%f_%f_%f"%(i,px,py,pz))
    if len(xs)>0:
        midX = max(xs)
        midY = max(ys)
        midZ = sum(zs)/len(zs)
        print (midY,midX)
        cv2.putText(colorPix, str(int(midZ)), (midX,midY), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255),3)


    client.publish("/LM","|".join(pts))
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(colorPix, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)
    
    cv2.imshow("1",depthPix)
    cv2.imshow("2",colorPix)
    cv2.waitKey(34)
  
openni2.unload()