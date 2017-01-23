import socket

HOST = 'localhost'
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'hello socket')
data = s.recv(1024)
print('Received', repr(data))
s.close()

