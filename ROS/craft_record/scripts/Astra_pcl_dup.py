#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python


import rospy
import numpy as np
import roslib
import std_msgs
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2,PointField,Image
import sys
from copy import deepcopy



class Astra_dup():
    def __init__(self):
        self.sub_pcl = rospy.Subscriber("/camera/depth_registered/points",PointCloud2,self.callback_pcl,queue_size=1)
        self.pub_pcl = rospy.Publisher("/ST3/camera/depth_registered/points",PointCloud2,queue_size=1)
        self.sub_rRGB = rospy.Subscriber("/camera/depth/image",Image,self.callback_rRGB,queue_size=1)
        self.pub_rRGB = rospy.Publisher("/ST3/camera/depth/image",Image,queue_size=1)
        self.sub_rD = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback_rD,queue_size=1)
        self.pub_rD = rospy.Publisher("/ST3/camera/rgb/image",Image,queue_size=1)

    def callback_pcl(self,ros_data):
        self.pub_pcl.publish(ros_data)
    def callback_rRGB(self,ros_data):
        self.pub_rRGB.publish(ros_data)
    def callback_rD(self,ros_data):
        self.pub_rD.publish(ros_data)

if __name__ == "__main__":
    loc_node = rospy.init_node("Astra_Resender")
    AD = Astra_dup()
    rospy.spin()
    


