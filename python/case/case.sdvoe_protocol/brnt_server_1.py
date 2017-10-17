import socket
import struct

host=''
port=6969

sock_bc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_bc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock_bc.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock_bc.bind((host,port))

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin

while 1:
    try:
        data,addr=sock_bc.recvfrom(1024)
        print "bc got data from",addr
        print " ".join(("%02x" % struct.unpack('B', n)) for n in data)

    except KeyboardInterrupt:
        raise
