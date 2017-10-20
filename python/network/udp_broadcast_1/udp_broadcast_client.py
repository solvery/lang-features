import socket,sys

addr=('<broadcast>', 5556)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.sendto("hello from client",addr)

while 1:
     data, addr=s.recvfrom(1024)
     if not data:
        break
     print data


