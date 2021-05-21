import serial
import rospy
import codecs
from std_msgs.msg import String

s  = serial.Serial(port = "/dev/ttyACM0",baudrate= 115200)
rospy.init_node("Force_Sensor")
force_pub = rospy.Publisher("/ST3/Tool_force",String,queue_size=1)
rospy.Rate(15)
while True:
    b = s.readline()
    try:
        num = int(codecs.decode(b))
    except:
        continue
    print (str(num))
    force_pub.publish(str(num))
    




