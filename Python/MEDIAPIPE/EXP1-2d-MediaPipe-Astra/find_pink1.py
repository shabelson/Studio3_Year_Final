import cv2
import imutils
import numpy as np


class PinkDetector():
    def __init__(self):
        self.pinkDict = {}
        self.lower = np.array([17, 15, 100],dtype = "uint8")
        self.upper = np.array([50, 100, 200],dtype= "uint8")
    def ImgaeProc(self,image):
        mask = cv2.inRange(image, self.lower, self.upper)
        print (np.average(mask))
        output = cv2.bitwise_and(image, image, mask = mask)
        return  output
if __name__ =="__main__":
    det = PinkDetector()
    cap =  cv2.VideoCapture(0)
    while True:
        b,im = cap.read()
        #im = cv2.cvtColor(im,cv2.COLOR_RGB2BGR)
        im = det.ImgaeProc(im)
        
        cv2.imshow("n",im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    cap.release()
    cv2.destroyAllWindows()   
    