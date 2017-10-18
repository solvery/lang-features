import socket
import struct
import time

host=''
port=6969

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin

try:
    data,addr=s.recvfrom(1024)
    resp=hex2bin([0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00])
    s.sendto(resp,('169.254.118.202', 6969))
    print "got data from",addr,len(data)
    print " ".join(("%02x" % struct.unpack('B', n)) for n in data)
    print "send: ", " ".join(("%02x" % struct.unpack('B', n)) for n in resp)
    time.sleep(0.2)

    data,addr=s.recvfrom(1024)
    resp=hex2bin([0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x12, 0x00])
    s.sendto(resp,('169.254.118.202', 6969))
    print "got data from",addr,len(data)
    print " ".join(("%02x" % struct.unpack('B', n)) for n in data)
    print "send: ", " ".join(("%02x" % struct.unpack('B', n)) for n in resp)

    data,addr=s.recvfrom(1024)
    print "got data from",addr,len(data)
    print " ".join(("%02x" % struct.unpack('B', n)) for n in data)
except KeyboardInterrupt:
    raise
