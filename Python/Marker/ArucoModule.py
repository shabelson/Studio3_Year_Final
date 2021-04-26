# ArUco markers generator_https://chev.me/arucogen/
# [OpenCV_Detection of ArUco Markers] https://docs.opencv.org/master/d5/dae/tutorial_aruco_detection.html
# Use "opencv-contrib-python" rather than "opencv-python"_pip install opencv-contrib-python ( * remember remove "opencv-python")

import cv2
import cv2.aruco as aruco
import numpy as np
import os # to assist to find out the markers.
import copy

def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):  # totalMarkers means How many markers are available.
    # Go to Grayscale
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Detect the format whether are you looking for or not
    key=getattr(aruco,f'DICT_{markerSize}X{markerSize}_{totalMarkers}') # Using f-string for controlling parameters ( python3.6版後的新特性: f-string，方便在字串內放變數)
    arucoDict=aruco.Dictionary_get(key)
    arucoParam=aruco.DetectorParameters_create()
    bboxs,ids,rejected=aruco.detectMarkers(imgGray,arucoDict,parameters=arucoParam)

    # print(ids)

    if draw:
        aruco.drawDetectedMarkers(img,bboxs)

    return [bboxs,ids]

def augmentAruco(bbox,id,img,imgAug,drawId=True):

    # Extract the BoundingBox 4 points
    tl = bbox[0][0][0], bbox[0][0][1]
    tr = bbox[0][1][0], bbox[0][1][1]
    br = bbox[0][2][0], bbox[0][2][1]
    bl = bbox[0][3][0], bbox[0][3][1]

    h,w,c=imgAug.shape
    pts1=np.array([tl,tr,br,bl])
    pts2=np.float32([[0,0],[w,0],[w,h],[0,h]])
    matrix,_=cv2.findHomography(pts2,pts1)
    imgOut=cv2.warpPerspective(imgAug,matrix,(img.shape[1],img.shape[0]))
    cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
    imgOut=img+imgOut

    return imgOut




def main():
    cap=cv2.VideoCapture(0)
    imgAug=cv2.imread("Markers/IAAC.png")


    while True:
        success,img = cap.read()
        # # Mirror display
        # if not success:
        #     break
        # img = cv2.flip(img, 1)  # Mirror display
        # debug_image = copy.deepcopy(img)
        arucoFound=findArucoMarkers(img)

        #Loop through all the markers and augment each one.
        if len(arucoFound[0])!=0: # bbox=0; id=1.
            for bbox,id in zip(arucoFound[0],arucoFound[1]):
                # print(bbox)
                img=augmentAruco(bbox,id,img,imgAug)

        cv2.imshow("Image",img)
        cv2.waitKey(1)




if __name__ == "__main__":
    main()



#------- References ------- #

## Markers and Dictionaries
# An ArUco marker is a synthetic square marker composed by a wide black border and a inner binary matrix which determines its identifier (id).
# The black border facilitates its fast detection in the image and the binary codification allows its identification and the application of error detection and correction techniques.
# The marker size determines the size of the internal matrix. (For instance a marker size of 4x4 is composed by 16 bits.)



