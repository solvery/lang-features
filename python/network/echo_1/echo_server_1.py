
import socket

HOST = '192.168.0.138'
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()

