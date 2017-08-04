# -*- coding: utf-8 -*  
import sys
import serial  
import struct
import time  
import logging
import random
import threading
import struct

serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 115200)

# logging
formatter="%(asctime)s %(levelname)-12s %(message)s"

# to file
log_filename="log_"+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d.%H.%M.%S.%f')
logging.basicConfig( filename=log_filename, filemode="a", format=formatter, level=logging.INFO);

# to console
formatter = logging.Formatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def uart_recv():
    logging.info("uart read")
    while True:  
        data = ''
        for i in range(1,10):
            time.sleep(0.3)
            count = ser.inWaiting()
            if count != 0:
                buf = ser.read(count)
                data += buf
                if data != '':
                    logging.info("recv: " + (" ".join(("%02x" % struct.unpack('B', n)) for n in data)))

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
    ser.write(cmd)
    logging.info("")
    logging.info("send: ")
    print_hex(cmd)
    time.sleep(1.1)  


def main():  
    t = threading.Thread(target=uart_recv)
    t.start()
    while True:  
        #ser.write('hello')
        cmd = bytearray(random_package())
        send_cmd(cmd)
        cmd = bytearray([0x1b, 0x28, 0x53])
        send_cmd(cmd)
        cmd = bytearray([0x1b, 0x5b, 0x41])
        send_cmd(cmd)
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


