import socket,sys

addr=('localhost', 10000)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("hello from client",addr)

while 1:
     data=s.recvfrom(1024)
     if not data:
        break
     print data


