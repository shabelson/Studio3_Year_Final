import cv2
import time
import os  # store finger reference images
import HandTrackingModule as htm  # <-- insert module

##########################################
wCam, hCam = 640, 480
##########################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)  # Import images

print(len(overlayList))

detector = htm.handDetector(detectionCon=0.7)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)  # <-- insert module
    lmList = detector.findPosition(img, draw=False)  # <-- insert module
    # print(lmList)

    # Check the finger close or not ( for example the height of ID8(Index_finger_tip) < ID6(Index_finger_pip)
    if len(lmList) != 0:

        ## Apply the specfic finger
        # if lmList[8][2] < lmList[6][2]: # top of height = 0
        #     print("Index finger open")

        ## Apply to all the fingers
        fingers = []

        # Thumb
        for id in range(1, 5):
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # 4 fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            print(fingers)
            totalFingers = fingers.count(1)  # Counting how many open fingers are
            # print(totalFingers)

            # Using [] to slice the specfic image
            h, w, c = overlayList[totalFingers - 1].shape
            img[0:h, 0:w] = overlayList[totalFingers - 1]

            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)

    # Mark FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)