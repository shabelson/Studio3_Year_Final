# Echo client program
import socket
import time
import struct

HOST = "192.168.0.9" # The remote host
PORT_30003 = 30003

print "Starting Program"

count = 0
home_status = 0
program_run = 0

while (True):
    if program_run == 0:
        try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((HOST, PORT_30003))
        time.sleep(1.00)
        print ""
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
        packet_12 = packet_12.encode("hex") #convert the data from \x hex notation to plain hex
        x = str(packet_12)
        x = struct.unpack('!d', packet_12.decode('hex'))[0]
        print "X = ", x * 1000
        packet_13 = s.recv(8)
        packet_13 = packet_13.encode("hex") #convert the data from \x hex notation to plain hex
        y = str(packet_13)
        y = struct.unpack('!d', packet_13.decode('hex'))[0]
        print "Y = ", y * 1000
        packet_14 = s.recv(8)
        packet_14 = packet_14.encode("hex") #convert the data from \x hex notation to plain hex
        z = str(packet_14)
        z = struct.unpack('!d', packet_14.decode('hex'))[0]
        print "Z = ", z * 1000
        packet_15 = s.recv(8)
        packet_15 = packet_15.encode("hex") #convert the data from \x hex notation to plain hex
        Rx = str(packet_15)
        Rx = struct.unpack('!d', packet_15.decode('hex'))[0]
        print "Rx = ", Rx
        packet_16 = s.recv(8)
        packet_16 = packet_16.encode("hex") #convert the data from \x hex notation to plain hex
        Ry = str(packet_16)
        Ry = struct.unpack('!d', packet_16.decode('hex'))[0]
        print "Ry = ", Ry
        packet_17 = s.recv(8)
        packet_17 = packet_17.encode("hex") #convert the data from \x hex notation to plain hex
        Rz = str(packet_17)
        Rz = struct.unpack('!d', packet_17.decode('hex'))[0]
        print "Rz = ", Rz
        home_status = 1
        program_run = 0
        s.close()
        except socket.error as socketerror:
    print("Error: ", socketerror)
print "Program finish"
