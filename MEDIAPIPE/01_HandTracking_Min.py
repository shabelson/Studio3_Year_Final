import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) # Webcam ID
# cap.set(3,320)
# cap.set(4,240)

mpHands=mp.solutions.hands
hands=mpHands.Hands() # Press Ctrl to call out hands.py
mpDraw=mp.solutions.drawing_utils

# # Set up Frame-rate
pTime=0 # Previous time is equal to Zero.
cTime=0 # Current time


# # Video is a sequence of images, so we need a while loop
while True:
    success,img = cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # print(results.multi_hand_landmarks) # Detect have hand or not

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # extract the information of each hand.
            for id, lm in enumerate(handLms.landmark):
                print(id,lm)
                # transfer the pixel ratio to position
                h,w,c=img.shape  # height,width,channel
                cx,cy =int(lm.x*w),int(lm.y*h) # position of center
                # print(id,cx,cy)
                # print(id, lm)
                if id==0:
                    cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    # Display FPS information
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3) # (img,FPS number,position,fonttype,size,color,thickness)

    cv2.imshow("Image",img)
    cv2.waitKey(1)



