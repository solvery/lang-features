from socket import *

server = "localhost"
#server = "192.168.2.9"
port = 514
buf = 8192*4
addr = (server,port)

TCPSock = socket(AF_INET,SOCK_DGRAM)
TCPSock.bind(addr)

while 1:
    data,addr = TCPSock.recvfrom(buf)
    if not data:
        print ("No response from systems!")
        break
    else:
        print (data)
        #print ("Message: ", data, file=db, flush=True)

TCPSock.close()
