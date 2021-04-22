# Echo client program
import socket
import time
import struct
import codecs
HOST = "192.168.1.25" # The remote host
PORT_30003 = 30003

print ("Starting Program")

count = 0
home_status = 0
program_run = 0

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
            packet_8 = s.recv(48)
            packet_9 = s.recv(48)
            packet_10 = s.recv(48)
            packet_11 = s.recv(48)
            packet_12 = s.recv(8)
            #print (codecs.decode(packet_12,"utf-16"))
            #packet_12 = packet_12.encode("hex") #convert the data from \x hex notation to plain hex
            packet_12 = packet_12.hex()
            x = str(packet_12)
            x = struct.unpack('!d', codecs.decode(packet_12,'hex'))[0]
            print ("X = ", x * 1000)
            home_status = 1
            program_run = 0
            
        except socket.error as socketerror:
            s.close()
            print("Error: ", socketerror)
s.close()
print ("Program finish")
