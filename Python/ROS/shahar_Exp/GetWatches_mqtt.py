#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python


import paho.mqtt as mqtt
from  paho.mqtt import client
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3Stamped,Vector3,Pose
import traceback as tb


global host
host = "192.168.1.10"
class watch():
    def __init__(self,ind):
        self.name = ind
        self.x = [0,False]    
        self.y = [0,False]
        self.z = [0,False]
    def RosMsg(self):
        #msg =Pose()
        #msg.position.x = 0 
        #msg.position.y = 0 
        #msg.position.z = 0 
        msg = Vector3()
        msg.x = self.x[0]
        msg.y = self.y[0]
        msg.z = self.z[0]
        self.x[1] = False
        self.x[1] = False
        self.x[1] = False
        rospy.loginfo("watch %i sent vector"%(self.name))
        return msg
    def checkUpdate(self):
        return self.x[1] and self.y[1] and self.z[1]
        
            
    
    
class WatchGrabber():
    def __init__(self):
        print ("wg init")
        subtopics = ['X','Y','Z']
        top1 = [("/watch1/"+ s,0)  for s in subtopics]
        top2 = [("/watch2/"+ s,0)  for s in subtopics]
        top3 = [("/watch3/"+ s,0)  for s in subtopics]
        #top4 = ["/ArdClick"]
        #top5 = ["/ToolF"]
        self.wathces = { "watch1":watch(1),"watch2":watch(2),"watch3":watch(3)}
        #self.watch1,self.watch2,self.watch3 = watch(),watch(),watch()
        self.mqClient = client.Client("main_frame")
        self.mqClient.connect(host, port=1883) 
        self.mqClient.subscribe(top1+top2+top3)
        self.mqClient.on_message = self.MqttMsg
        self.publishers = {
        "watch1": rospy.Publisher("watch1Vector",Vector3,queue_size=1),
        "watch2": rospy.Publisher("watch1Vector",Vector3,queue_size=1),
        "watch2": rospy.Publisher("watch1Vector",Vector3,queue_size=1)}
        print ('wg finish')
    def MqttMsg(self,client, userdata, msg ):
        print ("got msg mqtt")
        watchName = msg.topic.split('/')[1]
        watchAtr = msg.topic.split('/')[2]
        try: 
            val = float(msg.payload)
        except:
            return
        setattr(self.wathces[watchName],watchAtr.lower(),[val,True])
        if self.wathces[watchName].checkUpdate():
            self.publishers[watchName].publish(self.wathces[watchName].RosMsg())
    def on_disconnect(self,client, userdata,rc=0):
        print ("DISCONECK")
        self.mqClient.loop_stop()
if __name__=="__main__":
    wg =WatchGrabber()
    rospy.init_node("Wearable_Data")
    try:
         
        wg.mqClient.loop_forever()
    except ValueError as e:
        print ("here")
        pass 
    except Exception as e:
        print (tb.print_exc())
        print ("WWWOWOWOWOWOW")
        print (e)
        rospy.logfatal(str(e)+" _ watch node",)
        wg.mqClient.disconnect()
        wg.mqClient.loop_stop()
        

        
