import socket

#UDP_IP = "127.0.0.1"
UDP_IP = "192.168.2.7"
UDP_PORT = 514
MESSAGE = "Hello, Syslog!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
