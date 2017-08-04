import socket
import logging
import random
import threading
import struct 
import time
import sys
import os

# logging
formatter="%(asctime)s %(levelname)-12s %(message)s"

# to file
log_filename="uart.log"
logging.basicConfig( filename=log_filename, filemode="a", format=formatter, level=logging.INFO);

# to console
formatter = logging.Formatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.2.38', 5555)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def random_package():
    len = random.randint(100,255)
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    rand_list = [0x1b, c1, c2, len]
    for i in range(len):
        rand_list +=[random.randint(1,255)]
    return rand_list

def print_hex(data):
    logging.info(" ".join(("%02x" % n) for n in data))

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin

def send_cmd(cmd):
    sock.sendall(cmd)
    logging.info("")
    logging.info("send: ")
    print_hex(cmd)
    time.sleep(1.1)  
    data = sock.recv(8192)
    print_hex(bytearray(data))


data_send1 = 'hello'

try:
    
    # Send data
    while True:
        cmd = bytearray(random_package())
        send_cmd(cmd)
        cmd = bytearray([0x1b, 0x28, 0x53])
        send_cmd(cmd)
        cmd = bytearray([0x1b, 0x5b, 0x41])
        send_cmd(cmd)

        time.sleep(1.3)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

