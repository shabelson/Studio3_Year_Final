import codecs
import sys
import serial
import URDataGrabber as UR
import re
import os
import time

class ArdClick():
    def __init__(self):
        print ("init")
        self.prevBool  = 0
        self.counter = 0
        self.curBool = 0
        self.ser = serial.Serial(port='COM8',baudrate=115200, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
        print("connected to: " + self.ser.portstr)
    def CheckClick(self):
        #print ('__')
        #msg = 'f'
        self.bs = self.ser.readline()
        #print (self.bs)
        try:
            msg = self.bs.decode()
            #msgs = [t.decode() for t in self.bs]
            print ("got msg",msg)
        except Exception as e:
            print ("error com")
            return 
        if msg =='' or msg == ' ':
            print ("emtp msgy")
            return
        self.prevBool = self.curBool
        self.curBool = msg
        print ((self.curBool),(self.prevBool))
        if self.curBool=="1":
            print ("GOT !************************************************")
        if self.prevBool == 0 and self.curBool ==1:
            print ("rab")
            raise Exception ("yes!")
            self.counter+=1
            print (self.counter)
            print (UR.GrabData([8]))

if __name__ == "__main__":
    #print (os.path.exists("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/"))
    now = time.time()
    f = open("Robo_%f.csv"%(now),'w')
    f.close()
    obj = ArdClick()
    with open("Robo_%f.csv"%(now),'a') as file:
        while True:
            
            obj.CheckClick()
            #print (time.time())
