import csv
import sys
import os
from numpy.core.fromnumeric import shape
import pandas as pd
import time
import numpy as np
import datetime as dt

def trackerspliter(cell):
    tstamp = cell[0]
    nums  =cell[1]
    nums = nums.split(":")
    empRow = []
    for num in nums:
        empRow.append(num.split(" "))
    empRow = [s for m in empRow for s in m ]
    out = []
    for t in empRow:
        try:
            t = float(t)
        except:
            continue
        out.append(t)
    out.insert(0,tstamp)
    print (out)
    return out
def reduceSizeGridSamp(mat):
    print (mat.shape)
    
    newArry = np.asarray(mat[0,:])
    print(newArry)
    
    sample = 0
    for line in mat[:]:
        
        if sample!= line[1]:
            line = np.asarray(line)
            
            newArry = np.vstack((newArry,line))
            print (newArry)
            sample = line[1]
    return (newArry)
    

def gridsampSpliter(cell):
    num = cell.split(" ")[-1]
    return int(num)
def mpSpliter(line):
    #print (line)
    mps = line[1]
    date =line[0]

    pts ,tStamp = mps.split("++")
    
    #print (pts)
    pts = pts.split("||")
    print ([ len(pt.split(",")) for pt in pts])
    pts = [pt.split(",") for pt in pts]
    pts = [s for m in pts for s in m ]
    #print (pts)


    line =[date] +  pts + [tStamp]
    return np.asarray(line)


def TimeToEpoch(csvFile,name):
    t = np.asarray(csvFile)

    
    shifter = lambda x: dt.datetime.strptime(x, '%Y/%m/%d/%H:%M:%S.%f').timestamp()
    t[:,0] = np.asarray([shifter(cell) for cell in t[:,0]])
    if name =="grid_samp":
        t[:,1] = np.asarray([gridsampSpliter(cell) for cell in t[:,1]])
        t = reduceSizeGridSamp(t)
        print (t)
        return t 
    if name =="mp_string":
        #print (t.shape[0])
        newT = np.zeros((t.shape[0],14)) 
        for i in range(t.shape[0]):
            newT[i,:] = mpSpliter(t[i,:])
        return newT
 
    if name =="tracker":
        newT = np.zeros((t.shape[0],7))
        for i in range(t.shape[0]):
            newT[i,:] = trackerspliter(t[i,:])
        return newT
    return(t)
        





dirName = "D:/st3/rosbag_t3/combined/comb"
baseNames = ["ard_click","grid_samp","tool_force","tracker","watch1vector","mp_string"]
baseNames = ["mp_string"]

prefix = "_combined_csv.csv"
fileNames = [os.path.join(dirName,t+prefix) for t in baseNames ]
for name,file in zip(baseNames,fileNames):
    locCsv = pd.read_csv(file)
    locCsv = TimeToEpoch(locCsv,name)
    print (locCsv)
    np.savetxt("org_%s.csv"%(name), locCsv, delimiter=",")
    

