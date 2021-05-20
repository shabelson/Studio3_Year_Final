import csv
import sys
import os
from numpy.core.fromnumeric import shape
import pandas as pd
import time
import numpy as np
import datetime as dt
import math
tol = 0.3
dirName = "D:\\st3\\rosbag_t3\\combined\\org"
os.chdir(dirName)
baseNames = ["tool_force","tracker","watch1vector","mp_string"]
prefix ="org_"
newpref = "stamped_"

gridsFile = os.path.join(dirName,prefix+"grid_samp"+".csv")

gridsFile = np.asarray(pd.read_csv(gridsFile))

arrays = {}
np.set_printoptions(suppress=True,formatter={'float_kind':'{:16.3f}'.format}, linewidth=130)
for name in baseNames:
    path = os.path.join(dirName,prefix+name+".csv")
    df = np.asarray(pd.read_csv(path))

    arrays.update({name:df})

for name in baseNames:
    stampCouter = 0
   
    curStamp = gridsFile[stampCouter,:]
    #print (curStamp)
    curMat = arrays[name]
    #print (curMat.shape,"SHPAE")
    newMat = np.zeros((1,curMat.shape[1]+1))
    prevDelta = 0
    curDelta = 0
    print (name)
    
    for line in curMat:
        print (line)
        curDelta = curStamp[0]-line[0] 
        curStamp = gridsFile[stampCouter,:]
        if abs(curDelta)<tol:
            line = list(line[:])
            line.append(curStamp[1])
            #rint (line,curStamp[1])
            line = np.asarray(line)
            line.shape = (1,line.shape[0])
            
            newMat = np.vstack((newMat,line))
            
        if curDelta<0:
            stampCouter+=1
            if stampCouter>gridsFile.shape[0]-1:break
            curStamp = curStamp = gridsFile[stampCouter,:]
    newMat =np.round(newMat,8)
    np.savetxt(name+"_stamped.csv",newMat, delimiter=",")
    