#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python




global host
host = "192.168.1.10"

import paho.mqtt as mqtt
from paho.mqtt import client

from time import sleep
import rospy
from sensor_msgs.msg import Image
import codecs
from  std_msgs.msg import String 
import traceback as tb
import time



class GetClicks():
	def __init__(self):
		rospy.loginfo("Clicker init")
		self.pub_button = rospy.Publisher("/ST3/Arduino_click",String,queue_size=1)
		self.pub_place = rospy.Publisher("/ST3/Arduino_GridSample",String,queue_size=1)
		self.prev = 0
		self.out = 0
		self.counter = 0
		self.mqttClient = client.Client("Clicker Connect")
		self.mqttClient.connect(host=host,port=1883)
		self.mqttClient.subscribe("/ArdClick")
		self.mqttClient.on_message = self.OnMsg
		
		print ("setup Done",self.mqttClient.is_connected())
	def OnMsg(self,client,userData,msg):
		print ("Got Msg %f"%(time.time()))
		try:
			val =  int(msg.payload)
		except Exception as e:
			print (e)
			return
		self.prev = self.out
		self.out = val
		
		
		if self.out ==1 and self.prev ==0:
			self.counter+=1
			print ("ARD RECORD")
	
		self.pub_button.publish(str(self.out))
		self.pub_place.publish("recorded num %i"%self.counter)
		

		












if __name__ =="__main__":
	gc = GetClicks()	
	node = rospy.init_node("Arduino_clicker")
	try:
		rospy.loginfo("Clicker go To Loop")
		gc.mqttClient.loop_forever()
	except ValueError as e:
		print ("here")
		pass 
	except Exception as e:
		print (tb.print_exc())
	print ("WWWOWOWOWOWOW")
	print (e)
	rospy.logfatal(str(e)+" _ ArdClick node",)
	gc.mqttClient.disconnect()
	gc.mqttClient.loop_stop()

