
import mediapipe as mp
import cv2 as cv
import paho.mqtt.client as mqtt
import copy
import json
import socket



mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_drawing.DrawingSpec(color=(0,0,255),thickness= 2,circle_radius=2)
#mp.drawing.draw_landmarks()

cap = cv.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

#while cap.isOpened():
#    ret, frame = cap.read()
#    #cv.imshow('Camera Feed', frame)

#    if cv.waitKey(10) & 0XFF == ord('q'):
#        break

#cap.release()
#cv.destroyWindow()
counter = 0

#cap = cv.VideoCapture(0)
print(cap.isOpened())
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        # Mirror display
        if not ret:
            break
        frame = cv.flip(frame, 1)  # Mirror display
        debug_image = copy.deepcopy(frame)

        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        results = holistic.process(image)
        #print(results)


        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        print (image)
        # 1. Draw face landmarks
        #mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
        #                          mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
        #                          mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1)
        #                          )

        # 2. Right hand
        # mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        #                          mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
        #                          mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
        #                          )

        # 3. Left Hand
        # mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        #                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
        #                          mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2)
        #                          )

        # 4. Pose Detections
        try:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

            props = dir(results.pose_landmarks)
            # print((results.pose_landmarks.landmark[17]))
            right_waist = results.pose_landmarks.landmark[24]
            right_shoulder = results.pose_landmarks.landmark[12]
            right_elbow = results.pose_landmarks.landmark[14]
            right_wrist = results.pose_landmarks.landmark[16]
        except:
            right_waist = 0
            right_shoulder = 0
            right_elbow = 0
            right_wrist = 0

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
        client = mqtt.Client()
        client.connect("test.mosquitto.org", 1883)
        client.publish("/right/waist", str(right_waist));
        client.publish("/right/shoulder", str(right_shoulder));
        client.publish("/right/elbow", str(right_elbow));
        client.publish("/right/wrist", str(right_wrist));


        if cv.waitKey(10) & 0XFF == ord('q') or counter>3:
            break