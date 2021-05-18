"""import roslibpy
client = roslibpy.Ros(host = "192.168.10.186",port = 9090)
client.run()
print (client.is_connected)
client.terminate()
"""




from __future__ import print_function
import roslibpy
import time
import rospy 
from std_msgs.msg import String

class pubber():
    def __init__(self):
        self.node = rospy.init_node("tracker_point")
        self.pub = rospy.Publisher("/trackers",String,queue_size=1)
    def roslib_callback(self,data):
        self.pub.publish(data['data'])
        print ("got and sent")

if __name__ =="__main__":
    
    client = roslibpy.Ros(host="192.168.10.186", port=9090)
    client.run()
    node_pubber = pubber()
    listener = roslibpy.Topic(client, '/LHR_478352EA', 'std_msgs/String')
    listener.subscribe(node_pubber.roslib_callback)

    try:
        while True:
            pass
            #print (time.time())
    except KeyboardInterrupt:
        client.terminate()