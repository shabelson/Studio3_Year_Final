#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python3.9

import rospy
from sensor_msgs.msg import Image 
import roslib
import cv2 as cv
import time
import datetime
import csv
import numpy as np


class ImageGrabber():
    def __init__(self):
        
        self.timeList = []
        self.matrixNumber = []
        self.LoadTime()
        self.t1 = self.timeList[0]
        self.t2 =self.timeList[1]
        self.image_sub = rospy.Subscriber("/ST3/overlay",Image,self.gotMsg,queue_size=None)
        
        
    def LoadTime(self):
        fname = "/media/shabelson/backup_vol1/st3/rosbag_t1/rec_full-ST3-Arduino_click.csv"
        with open(fname,'r',newline="\n") as locFile:
            reader = csv.reader(locFile)
            
            for line in reader:
                self.timeList.append(line[0])
                #t = datetime.datetime.strptime(line[1], '%Y/%m/%d/%H:%M:%S.%f').timestamp()
                
                self.matrixNumber.append(line[1])
        self.timeList.pop(0)
        self.matrixNumber.pop(0)
        self.timeList = list(map(lambda t: datetime.datetime.strptime(t, '%Y/%m/%d/%H:%M:%S.%f').timestamp(),self.timeList)        )
        print( self.timeList)
    def gotMsg(self,ros_data):
        if self.t1<ros_data.header.timestamp:
            np_arr = np.frombuffer(ros_data.data, 'uint8')
            np_arr.shape = (ros_data.height,ros_data.width,3)
            np_arr = cv.cvtColor(np_arr,cv.COLOR_BGR2RGB)
            self.rgbImg  = np_arr
        








if __name__ =="__main__":
    ig = ImageGrabber()
