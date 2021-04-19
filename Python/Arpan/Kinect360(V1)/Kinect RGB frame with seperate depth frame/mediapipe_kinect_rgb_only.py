import mediapipe as mp
import cv2 as cv
import paho.mqtt.client as mqtt
import freenect
import numpy as np
import json

#import socket


# function to get RGB image from kinect
def get_video():
    array, _ = freenect.sync_get_video()
    array = cv.cvtColor(array, cv.COLOR_RGB2BGR)
    return array


# function to get depth image from kinect
def get_depth():
    array, _ = freenect.sync_get_depth()
    #array = array.astype(np.uint8)
    return array



mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_drawing.DrawingSpec(color=(0,0,255),thickness= 2,circle_radius=2)
#mp.drawing.draw_landmarks()



#while cap.isOpened():
#    ret, frame = cap.read()
#    #cv.imshow('Camera Feed', frame)

#    if cv.waitKey(10) & 0XFF == ord('q'):
#        break

#cap.release()
#cv.destroyWindow()
counter = 0

#cap = cv.VideoCapture(0)
depth = get_depth()

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while True:
        #ret, frame = cap.read()
        frame = get_video()
        print(type(frame))


        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        results = holistic.process(frame)
        #print(results)


        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        # 4. Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        #props = dir(results.pose_landmarks)
        #print((results.pose_landmarks.landmark[17]))
        right_waist = results.pose_landmarks.landmark[24]
        right_shoulder = results.pose_landmarks.landmark[12]
        right_elbow = results.pose_landmarks.landmark[14]
        right_wrist = results.pose_landmarks.landmark[16]


        #try:
        #    print ("\n\n\n\n\n\n")
        #    print ((results.pose_landmarks.landmark[0]))
        #    counter+=1
        #except Exception as e:
        #    print (e)
        #    pass
        #"""
        #for attr in props:
        #    print(attr,"\n\n\n")
        #    print("_________\n\n\n")

        #    if hasattr(getattr(results.pose_landmarks,attr),"__call__") : continue
        #"""         #   print(value)
         #   continue
        message = cv.imshow('Detection feed', image)
        #depth = get_depth()
        #depth_cam = cv.imshow('Depth feed', depth)
        client = mqtt.Client()
        client.connect("test.mosquitto.org", 1883)
        client.publish("/right/waist", str(right_waist));
        client.publish("/right/shoulder", str(right_shoulder));
        client.publish("/right/elbow", str(right_elbow));
        client.publish("/right/wrist", str(right_wrist));

        if cv.waitKey(10) & 0XFF == ord('q') or counter>3:
            break