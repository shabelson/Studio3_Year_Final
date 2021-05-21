#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python
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
from GetLandMarks import LandMarkMaker as lmm
from copy import deepcopy


class skeleton_finder():
    def __init__(self):
        self.sub_rgbImg = rospy.Subscriber("/camera/rgb/image_raw",Image,callback=self.callback_rgbImg ,queue_size=1)
        self.sub_dImg = rospy.Subscriber("/camera/depth/image_raw",Image,callback=self.callback_dImg ,queue_size=1)
        self.pub_lmImg = rospy.Publisher("/ST3/lmImg",Image,queue_size=1)
        self.pub_pts = rospy.Publisher("/ST3/mp_pcl",PointCloud2,queue_size=1)
        self.pub_overlay = rospy.Publisher("/ST3/overlay",Image,queue_size=1) 
        self.lmm = lmm()
        self.dRGB = []
        self.ptField = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1)]
        self.overImg  = []
        self.cvbridge = cv_bridge.CvBridge()
    def callback_rgbImg(self,ros_data):
        np_arr = np.frombuffer(ros_data.data, 'uint8')
        np_arr.shape = (ros_data.height,ros_data.width,3)
        np_arr = cv.cvtColor(np_arr,cv.COLOR_BGR2RGB)
        self.rgbLmImg = deepcopy(np_arr)
        self.lmm.MakeLM(np_arr)
        self.pub_lmImg.publish(self.cvbridge.cv2_to_imgmsg(self.lmm.lmImg))
        """
        try:
            cv.imshow("t",self.lmm.lmImg)
            cv.imshow('t2',self.Img)
            cv.waitKey(2)
        except Exception as e:
            print (e)
        """
    def Overlay(self):
        alpha = 0.5
        beta = 1-alpha
        self.locd = np.asarray(self.dImg*255,dtype= np.uint8)
        self.overImg = cv.addWeighted(self.locd, alpha, self.lmm.lmImg, beta,0)

        
    def callback_dImg(self,ros_data):
        np_arr = np.frombuffer(ros_data.data, 'uint16')
        np_arr.shape = (ros_data.height,ros_data.width)
        norm = np_arr/np.max(np_arr)
        norm32 =  np.float32(norm)
        self.dImg = cv.cvtColor(norm32,cv.COLOR_GRAY2RGB)
        outPts = []
        
        for pt in self.lmm.pixels:
            if pt ==[]:continue
            
            newPt = [pt[0],pt[1],np_arr[pt[0],pt[1]]]
            outPts.append(newPt)
            self.dImg = dRGB
        
        self.Overlay()
        pc2 = point_cloud2.create_cloud(ros_data.header, self.ptField, outPts)
        self.pub_pts.publish(pc2)
        
        self.pub_overlay.publish(self.cvbridge.cv2_to_imgmsg(self.overImg))
        #cv.imshow("t3",self.overImg)
        #cv.imshow("rgb+mp",self.rgbLmImg)
        
    def GetLandMarks(self,img):
        pass

if __name__ == "__main__":
    loc_node = rospy.init_node("LandMark_Grabber")
    sk = skeleton_finder()
    rospy.spin()
    cv.waitKey(2)
    cv.destroyAllWindows()   
