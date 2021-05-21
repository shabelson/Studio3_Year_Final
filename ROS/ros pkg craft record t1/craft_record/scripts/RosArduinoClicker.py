#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python


from time import sleep
import rospy
from sensor_msgs.msg import Image
import serial
import codecs
from  std_msgs.msg import String 
if __name__ =="__main__":
	counter = 0
	node = rospy.init_node("Arduino_clicker")
	pub_button = rospy.Publisher("/ST3/Arduino_click",String,queue_size=1)
	pub_place = rospy.Publisher("/ST3/Arduino_GridSample",String,queue_size=1)
	
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
			counter+=1
			pub_button.publish(str(out))
			pub_place.publish("recorded num %i"%counter)
			print ("ARD RECORD")
			sleep(0.1)
		else:
			pass	
		prev = out
        
