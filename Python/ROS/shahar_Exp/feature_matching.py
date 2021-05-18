






import rospy
import numpy as np
import roslib
import cv_bridge 
import mediapipe as mp
import cv2 as cv
import std_msgs
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2,PointField,Image
import cv_bridge
import sys

sys.path.append("..")



class skeleton_finder():
    def __init__(self):
        self.sub_rgbImg = rospy.Subscriber("/camera/rgb/image_raw",Image,callback=self.callback_rgbImg ,queue_size=1)
        self.sub_dImg = rospy.Subscriber("/camera/depth/image_raw",Image,callback=self.callback_dImg ,queue_size=1)
        self.dImg = None
        self.rgbCollected = False
        self.rgbImg = None       
    def callback_rgbImg(self,ros_data):
        np_arr = np.frombuffer(ros_data.data, 'uint8')
        np_arr.shape = (ros_data.height,ros_data.width,3)
        np_arr = cv.cvtColor(np_arr,cv.COLOR_BGR2RGB)
        self.rgbImg = np_arr
        self.rgbCollected = True
        
    def callback_dImg(self,ros_data):
        np_arr = np.frombuffer(ros_data.data, 'uint16')
        np_arr.shape = (ros_data.height,ros_data.width)
        norm = np_arr/np.max(np_arr)
        norm32 =  np.float32(norm)
        self.dImg = cv.cvtColor(norm32,cv.COLOR_GRAY2RGB)
        
        if self.rgbCollected ==True:
            self.Overlay()
            #self.GetFeatures()
            cv.imshow("t",self.dImg)
            cv.imshow('t2',self.rgbImg)
            cv.imshow('t3',self.overImg)
            cv.imshow('t4',self.locd)
            
            cv.waitKey(2)
    def Overlay(self):
        alpha = 0.5
        beta = 1-alpha
        print (type(self.dImg.astype(int)[0,0,0]),type(self.rgbImg[0,0,0]))
        print (np.average(self.dImg))
        self.locd = np.asarray(self.dImg*255,dtype= np.uint8)
        self.overImg = cv.addWeighted(self.locd, alpha, self.rgbImg, beta,0)

    def GetFeatures(self):
        gray1 = cv.cvtColor(self.rgbImg,cv.COLOR_RGB2GRAY)
        corners1 = cv.goodFeaturesToTrack(gray1,25,0.01,10)
        corners1 = np.int0(corners1)
        print (self.dImg.shape)
        gray2 = cv.cvtColor(self.dImg,cv.COLOR_RGB2GRAY)
        corners2= cv.goodFeaturesToTrack(gray2,25,0.01,10)
        corners2 = np.int0(corners2)
        r1,r2 = cv.findFundamentalMat(corners1,corners2,cv.FM_RANSAC,3,0.99)
        """
        mat1 = cv.stereoRectifyUncalibrated(corners1,corners2,r1,[640,480])[1]
        mat2 = cv.stereoRectifyUncalibrated(corners2,corners1,r1,[640,480])[1]
        """
        for i,t in zip(corners1,corners2):
            x1,y1 = i.ravel()
            x2,y2 = t.ravel()
        
            cv.circle(self.rgbImg,(x1,y1),3,255,-1)
            cv.circle(self.rgbImg,(x2,y2),3,[0,150,0],-1)
 
        for i in corners2:
            x,y = i.ravel()
            cv.circle(self.dImg,(x,y),3,255,-1)
        """
        self.rgbImg = cv.warpPerspective(self.rgbImg,mat1,[640,480])
        self.dImg = cv.warpPerspective(self.dImg,mat2,[640,480])
        """
        #print (res)

        

if __name__ == "__main__":
    loc_node = rospy.init_node("feature_matcher")
    sk = skeleton_finder()
    rospy.spin()
    cv.waitKey(2)
    cv.destroyAllWindows()   
