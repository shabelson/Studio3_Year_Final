#/home/shabelson/github/Studio3_Year_Final/ROS/env/tvenv/bin/python3.9
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



class skeleton_finder():
    def __init__(self):
        self.sub_rgbImg = rospy.Subscriber("/camera/rgb/image_rect_color",Image,callback=self.callback_rgbImg ,queue_size=1)
        self.sub_dImg = rospy.Subscriber("/camera/depth_registered/image",Image,callback=self.callback_dImg ,queue_size=1)
        self.pub_lmImg = rospy.Publisher("/ST3/lmImg",Image,queue_size=1)
        self.pub_pts = rospy.Publisher("/ST3/pcl",PointCloud2,queue_size=1)
        self.lmm = lmm()
        self.ptField = [PointField('x', 0, PointField.INT32, 1),
          PointField('y', 4, PointField.INT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1)]
         
    def callback_rgbImg(self,ros_data):
        np_arr = np.frombuffer(ros_data.data, 'uint8')
        np_arr.shape = (ros_data.height,ros_data.width,3)
        np_arr = cv.cvtColor(np_arr,cv.COLOR_BGR2RGB)
        self.lmm.MakeLM(np_arr)
        self.rgbImg  = np_arr
        
        
        
    def callback_dImg(self,ros_data):
        np_arr = np.frombuffer(ros_data.data, 'uint16')
        np_arr.shape = (ros_data.height,ros_data.width)
        norm = np_arr/np.max(np_arr)
        norm32 =  np.float32(norm)
        dRGB = cv.cvtColor(norm32,cv.COLOR_GRAY2RGB)
        outPts = []
        for pt in self.lmm.pixels:
            if pt ==[]:continue
            center = pt
            #center = (int(pt.x*ros_data.height),int(pt.y*ros_data.width))
            #pt =[int(pt.x*ros_data.height),int(pt.y*ros_data.width),np_arr[center[0],center[1]]]
            newPt = [pt[0],pt[1],np_arr[pt[0],pt[1]]]
            dRGB = cv.circle(dRGB,center,10,(150,150,150))
            print (type(pt[0]))
            outPts.append(newPt)

        pc2 = point_cloud2.create_cloud(ros_data.header, self.ptField, outPts)
        self.pub_pts.publish(pc2)
        cv.imshow("t",self.lmm.lmImg)
        cv.imshow('t2',dRGB)
        
        cv.waitKey(2)
    def GetLandMarks(self,img):
        pass

if __name__ == "__main__":
    loc_node = rospy.init_node("LandMark_Grabber")
    sk = skeleton_finder()
    rospy.spin()
    cv.waitKey(2)
    cv.destroyAllWindows()   
