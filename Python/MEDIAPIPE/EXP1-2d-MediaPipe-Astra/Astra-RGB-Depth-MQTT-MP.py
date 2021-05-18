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
exposure = 1000

# ======= Smoothing Parameters =======
# How much smoothing (and latency) you want
# 0 --> no smoothing, no latency
# 0.9 --> lots of smoothing, lots of latency
easingParam = 0

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
import serial
import re
import URDataGrabber as ur
import find_pink1
"""


while True:
    for c in ser.read():
        line.append(c)
        if c == '\n':
            print("Line: " + ''.join(line))
            line = []
            break



"""
f = open("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/Robo.csv",'w')
f.close()
f = open("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/hands.csv",'w')
f.close()
prevBool  = 0
curBool = 0
ser = serial.Serial(port='COM4',baudrate=115200, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)

print("connected to: " + ser.portstr)
counter = 0
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
    time.sleep(2)

# Main loop
lastUpdateTime = time.time()
bPrevData = False
px = 0
py = 0
pz = 0
detector = handDetector()
pink = find_pink1.PinkDetector()
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
    img2 = None
    avgDist = np.average(depthPix)
    colorPix = np.array(colorPix)
    RGB_Save = np.array(colorPix)
    colorPix = detector.findHands(colorPix,draw = True)
    lmList= detector.findPosition(colorPix,draw =  True)
    pinkImg = pink.ImgaeProc(colorPix)
    
    
    zs = []
    xs = []
    ys = []    
    pts = []

    lmInds = [0,5,8]
    for i,lm in enumerate(lmList):
        #print (depthPix.shape,colorPix.shape,lm)
        
        if lm[1]>=depthPix.shape[0]:
            lm[1] = depthPix.shape[0]-2
        if lm[2]>=depthPix.shape[1]:
            lm[2]=depthPix.shape[1]-2

        #print (lm)
        locz = depthPix[lm[1]][lm[2]]
        #print (locz)
        x,y,z = openni2.convert_depth_to_world(depth_stream,lm[1],lm[2],locz)
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
        pts.append(",".join(map(str,[lm[1],lm[2],locz])))       
        #client.publish("LM/%i"%(i),"%i:%f_%f_%f"%(i,px,py,pz))
    
    bs = ser.read_all()
    bs =  str(bs)
    nums = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",bs)
    prevBool = curBool
    boolOut = sum(map(int,nums))
    if boolOut>0:
        curBool = 1
    else:
        curBool = 0
    
    outMsg = "No Marks\n"

    if len(xs)>0:
        midX = max(xs)
        midY = max(ys)
        midZ = sum(zs)/len(zs)
        #print (midY,midX)
        cv2.putText(colorPix, str(int(midZ)), (midX,midY), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255),3)
        outMsg=  "|".join(pts)+"="+str(curBool)
        #print (outMsg)
        client.publish("/LM",outMsg)
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(colorPix, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)
    cv2.imshow("1",depthPix)
    cv2.imshow("2",colorPix)
    cv2.imshow("3",pinkImg)
    cv2.waitKey(34)
    
    if curBool ==1 :#and prevBool == 0:
        counter+=1
        print("SAVE")
        Dic = ur.GrabData([12,8])
        Dic[12].insert(0,"TCP")
        Dic[8].insert(0,"JOINTS")
        outString =[str(counter)] + Dic[12]+Dic[8]+["\n"]
        outString = map(str,outString)
        outMsg = "%i_%s\n"%(counter,outMsg)

        outString = ",".join(outString)          
        cv2.imwrite("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/pics/d/%i_depth.jpg"%(counter),depthPix)
        cv2.imwrite("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/pics/rgb/%i_RGB.jpg"%(counter),colorPix)
        cv2.imwrite("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/pics/rgb/%i_RGB_org.jpg"%(counter), RGB_Save)
        
        with open("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/Robo.csv",'a') as fileName:
            fileName.write(outString)
        with open("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/Hands.csv",'a') as fileName:
            fileName.write(outMsg)
  
openni2.unload()
ser.close()
