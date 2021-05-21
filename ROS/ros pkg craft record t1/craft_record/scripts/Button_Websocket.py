#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python

from __future__ import print_function
import roslibpy
import time
import rospy 
from std_msgs.msg import String

class pubber():
	def __init__(self):
		self.node = rospy.init_node("Arduino_button_socket")
		self.pub = rospy.Publisher("/ST3/Button_Click",String,queue_size=1)
		self.prev = 0
		self.out = 0
	def roslib_callback(self,message):
		self.pub.publish(message['data'])
		print ("got and sent")
    
		try :
			x = codecs.decode(bts)
			out = int(x)
		except:
			return
		if out ==1 and prev ==0:
			pub_button.publish(str(out))
			print ("ARD RECORD")
			sleep(0.1)
		else:
			pass	
		prev = out


if __name__ =="__main__":
	client = roslibpy.Ros(host="192.168.10.170", port=9090)
	client.run()
	node_pubber = pubber()
	listener = roslibpy.Topic(client, '/button', 'std_msgs/String')
	listener.subscribe(node_pubber.roslib_callback)

	try:
		while True:
			pass
	except KeyboardInterrupt:
	    client.terminate()


"""
if __name__ =="__main__":
	node = rospy.init_node("Arduino_clicker")
	pub_button = rospy.Publisher("/ST3/Arduino_click",String,queue_size=1)
	connect = False
	while connect==False:
		try:
			ardReader = serial.Serial("/dev/ttyACM0",115200)
			connect = True
			print ("Ard Click Connected")

			
		except:
			sleep(0.1)
			print ("Ard Click Not connected")
	prev = 0
	out = 0
	while True:
		bts = ardReader.readline()
        
		try :
			x = codecs.decode(bts)
			out = int(x)
		except:
			continue
		if out ==1 and prev ==0:
			pub_button.publish(str(out))
			print ("ARD RECORD")
			sleep(0.1)
		else:
			pass	
		prev = out

"""