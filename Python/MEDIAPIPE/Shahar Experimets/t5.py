import cv2 as cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    t = cap.read()
    
    print (t)
    cv2.imshow("name",t)
    cv2.waitKey(34)
