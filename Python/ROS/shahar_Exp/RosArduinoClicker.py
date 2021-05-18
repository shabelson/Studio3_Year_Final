
#/home/shabelson/github/Studio3_Year_Final/ROS/env/tvenv/bin/ python3.9
import rospy
from sensor_msgs.msg import Image
import serial
import codecs
from  std_msgs.msg import String 
if __name__ =="__main__":
    node = rospy.init_node("Arduino_clicker")
    pub_button = rospy.Publisher("/Arduino/click",String,queue_size=1)
    ardReader = serial.Serial("/dev/ttyACM0",115200)
    out = 0
    while True:
        bts = ardReader.readline()
        
        try :
            x = codecs.decode(bts)
            out = int(x)
        except:
            pass
        
        pub_button.publish(str(out))
        
