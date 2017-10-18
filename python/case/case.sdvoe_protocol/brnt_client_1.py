import socket
import sys
import struct
import time

bc_addr=('<broadcast>', 6969)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin


data=hex2bin([0x07, 0x13, 0x03, 0x03, 0x01, 0x13, 0x97, 0x08, 0x01, 0x00] + [0x08, 0x00, 0x27, 0x65, 0xad, 0xf3] + [0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00])
s.sendto(data, bc_addr)
time.sleep(0.5)
s.sendto(data, bc_addr)
time.sleep(0.5)
s.sendto(data, bc_addr)
time.sleep(0.5)
data,addr=s.recvfrom(1024)
print "got data from",addr,len(data)
print " ".join(("%02x" % struct.unpack('B', n)) for n in data)

