__author__ = "Shahar Abelson"
# Echo client program
# For Packet explanation see https://s3-eu-west-1.amazonaws.com/ur-support-site/16496/Client_InterfacesV3.14andV5.9.xlsx
import socket
import time
import struct
import codecs
import math

def ByteUnpacHex(packet):
    
    
    try:
        tempPack = packet.hex()
        x = struct.unpack('!d', codecs.decode(tempPack,'hex'))[0]
    except:
        x = int.from_bytes(packet,"big")
    return (x)

def GetDataRange(DataInds):
    dataDict = {1:[1,4],
    2:[1,8],
    3:[6,48],
    4:[6,48],
    5:[6,48],
    6:[6,48],
    7:[6,48],
    8:[6,48],
    9:[6,48],
    10:[6,48],
    11:[6,48],
    12:[6,48],
    13:[6,48],
    14:[6,48],
    15:[6,48],
    16:[6,48],
    17:[1,8],
    18:[6,48],
    19:[1,8],
    20:[1,8],
    21:[1,8],
    22:[6,48],
    23:[1,8],
    24:[6,48],
    25:[3,24],
    26:[6,48],
    27:[1,8],
    28:[1,8],
    29:[1,8],
    30:[1,8],
    31:[1,8],
    32:[1,8],
    33:[1,8],
    34:[6,48],
    35:[1,8],
    36:[1,8],
    37:[3,24],
    38:[3,24],
    39:[1,8]}
    DataRange = []
    for i in dataDict.keys():
        if not i in DataInds:
            DataRange.append([dataDict[i][1],False,-1])
        else:    
            valNum = int(dataDict[i][0])
            val  = int(dataDict[i][1]/dataDict[i][0])
            for b in range(valNum):
                DataRange.append([val,True,i])
    
    deadBytes = 0
    outPacks = []
    for bPack in DataRange:
        if bPack[1]==False:
            deadBytes+=bPack[0]
        else:
            if deadBytes>0:
                outPacks.append([deadBytes,False,-1])
            outPacks.append(bPack)
            deadBytes = 0
   
    return outPacks
            
def GrabData(DataInds,HOST = "192.168.1.25",PORT_30003 = 30003):

    print ("Starting Program")
    count = 0
    home_status = 0
    program_run = 0
    outPacks = GetDataRange(DataInds)
    OutDict = {}
    if program_run == 0:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((HOST, PORT_30003))
            #time.sleep(1.00)
            print ("")
            for bPack in outPacks:
                
                locPacket =s.recv(bPack[0])
                if bPack[1]==True:
                    locPacket = ByteUnpacHex(locPacket)
                    if bPack[2] in list(OutDict.keys()):
                        OutDict[bPack[2]].append(locPacket)
                    else:
                        OutDict.update({bPack[2]:[locPacket]})
            home_status = 1
            program_run = 0

        except socket.error as socketerror:
            s.close()
            print("Error: ", socketerror)
    s.close()
    return(OutDict)
    print ("Program finish")
if __name__ =="__main__":
    while True:
        print (GrabData([12])) # 12 - TCP, 8 - Joint Orientation