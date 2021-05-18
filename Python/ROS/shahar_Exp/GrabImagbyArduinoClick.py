#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python3.9

import rospy
from sensor_msgs.msg import Image 
import roslib
import cv2 as cv
import time
import datetime
import csv

class ImageGrabber():
    def __init__(self):
        
        self.timeList = []
        self.matrixNumber = []
        self.LoadTime()
        #self.image_sub = rospy.Subscriber("/ST3/overlay",Image,self.gotMsg,queue_size=None)
        
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



if __name__ =="__main__":
    ig = ImageGrabber()
