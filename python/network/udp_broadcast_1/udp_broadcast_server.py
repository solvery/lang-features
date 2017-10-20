import socket
import struct

host=''
port=5556

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((host,port))

while 1:
    try:
        data,addr=s.recvfrom(1024)
        print "got data from",addr
        print " ".join(("%02x" % struct.unpack('B', n)) for n in data)
        #s.sendto("broadcasting",addr)
    except KeyboardInterrupt:
        raise
