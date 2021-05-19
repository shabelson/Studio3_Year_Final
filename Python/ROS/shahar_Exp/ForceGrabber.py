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



class GetCForce():
	def __init__(self):
		rospy.loginfo("Force Grabber init")
		self.pub_sensor = rospy.Publisher("/ST3/Tool_force",String,queue_size=1)
		self.mqttClient = client.Client("Tool Force Connect")
		self.mqttClient.connect(host=host,port=1883)
		self.mqttClient.subscribe("/ToolF")
		self.mqttClient.on_message = self.OnMsg
		
		print ("setup Done",self.mqttClient.is_connected())
	def OnMsg(self,client,userData,msg):
		print ("Got Msg %f"%(time.time()))
		try:
			val =  float(msg.payload)
		except Exception as e:
			print (e)
			return

		
	
		self.pub_sensor.publish(str(val))


if __name__ =="__main__":
	gc = GetCForce()	
	node = rospy.init_node("Force Sensor")
	try:
		rospy.loginfo("ForceSensor go To Loop")
		gc.mqttClient.loop_forever()
	except ValueError as e:
		print ("here")
		pass 
	except Exception as e:
		print (tb.print_exc())
	print ("WWWOWOWOWOWOW")
	print (e)
	rospy.logfatal(str(e)+" _ Force Sensor node",)
	gc.mqttClient.disconnect()
	gc.mqttClient.loop_stop()

