# Echo client program
# For Packet explanation see https://s3-eu-west-1.amazonaws.com/ur-support-site/16496/Client_InterfacesV3.14andV5.9.xlsx
import socket
import time
import struct
import codecs
import math

HOST = "192.168.1.25" # The remote host
PORT_30003 = 30003

print ("Starting Program")

count = 0
home_status = 0
program_run = 0
def ByteUnpacHex(packet):
     packet = packet.hex()
     x = struct.unpack('!d', codecs.decode(packet,'hex'))[0]
     return (x)


while (True):
    if program_run == 0:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((HOST, PORT_30003))
            #time.sleep(1.00)
            print ("")
            packet_1 = s.recv(4)
            packet_2 = s.recv(8)
            packet_3 = s.recv(48)
            packet_4 = s.recv(48)
            packet_5 = s.recv(48)
            packet_6 = s.recv(48)
            packet_7 = s.recv(48) 
            packet_j1 = s.recv(8) #packet num 8 
            
            
            packet_j2 = s.recv(8) #packet num 8 
            packet_j3 = s.recv(8) #packet num 8 
            packet_j4 = s.recv(8) #packet num 8 
            packet_j5 = s.recv(8) #packet num 8 
            packet_j6 = s.recv(8) #packet num 8         
            j1 = ByteUnpacHex(packet_j1)
            j2 = ByteUnpacHex(packet_j2)
            j3 = ByteUnpacHex(packet_j3)
            j4 = ByteUnpacHex(packet_j4)
            j5 = ByteUnpacHex(packet_j5)
            j6 = ByteUnpacHex(packet_j6)
            jz = map(math.degrees,[j1,j2,j3,j4,j5,j6])
            print ("_".join(map(str,jz)))
            packet_9 = s.recv(48)
            packet_10 = s.recv(48)
            packet_11 = s.recv(48)
            packet_12 = s.recv(8)

            home_status = 1
            program_run = 0
            
        except socket.error as socketerror:
            s.close()
            print("Error: ", socketerror)
s.close()
print ("Program finish")
