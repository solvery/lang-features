import socket
import datetime
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
log_filename="log_"+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d.%H.%M.%S.%f')
logging.basicConfig( filename=log_filename, filemode="a", format=formatter, level=logging.INFO);

# to console
formatter = logging.Formatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_addr = sys.argv[1]
server_address = (ip_addr, 5555)
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

def data_recv():
    while True:  
        data = ''
        for i in range(1,10):
            time.sleep(0.2)
            data = sock.recv(8192)
            count = len(data)
            if count != 0:
                if data != '':
                    logging.info("recv: " + (" ".join(("%02x" % struct.unpack('B', n)) for n in data)))

def send_cmd(cmd):
    sock.sendall(cmd)
    logging.info("")
    logging.info("send: ")
    print_hex(cmd)
    time.sleep(0.1)  

data_send1 = 'hello'

def main():  
    t = threading.Thread(target=data_recv)
    t.setDaemon(True)
    t.start()
    try:
        while True:  
            #ser.write('hello')
            cmd = bytearray(random_package())
            send_cmd(cmd)
            cmd = bytearray([0x1b, 0x28, 0x53])
            send_cmd(cmd)
            cmd = bytearray([0x1b, 0x5b, 0x41])
            send_cmd(cmd)
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

         
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if sock != None:  
            sock.close()


