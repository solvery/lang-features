import socket
import time

ANY = "0.0.0.0"
MCAST_ADDR = "224.168.2.9"
MCAST_PORT = 1600

#create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

sock.bind((ANY,MCAST_PORT))
#tell the kernel that we are a multicast socket
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
# add to a multicast group
status = sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_ADDR) + socket.inet_aton(ANY));

sock.setblocking(0)
ts = time.time()
while 1:
    try:
        data, addr = sock.recvfrom(1024)
    except socket.error, e:
        pass
    else:
        print "We got data!"
        print "FROM: ", addr
        print "DATA: ", data
