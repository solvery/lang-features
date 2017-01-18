import socket
import struct 
import time
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.2.28', 5555)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def print_hex(data):
    for d in data:
        print '%02x' % struct.unpack('B', d),
    print
    return

def hex2bin(data):
    data_bin_array=''
    for d in data:
        data_bin_array = data_bin_array + struct.pack('B', d)
    return data_bin_array


data_send1 = hex2bin([0x1b, 0x28, 0x53])

try:
    
    # Send data
    print_hex(data_send1)
    sock.sendall(data_send1)

    data = sock.recv(8192)
    print_hex(data)
    while True:
        time.sleep(50)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

