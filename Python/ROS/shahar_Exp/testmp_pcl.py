#/home/shabelson/github/Studio3_Year_Final/ROS/env/tvenv/bin/ python3.9
import rospy
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2



def pclfunc(ros_data):
    print (type(ros_data))
    print (list(point_cloud2.read_points(ros_data)))


if __name__ =="__main__":
    node = rospy.init_node("pclT", anonymous=True)
    sub = rospy.Subscriber("/ST3/mp_pcl",PointCloud2,callback = pclfunc)
    rospy.spin()