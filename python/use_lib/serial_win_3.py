# -*- coding: utf-8 -*  
import sys
import serial  
import struct
import time  
import logging
import random
import threading

serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 115200)

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

def uart_recv():
    logging.info("uart read")
    while True:  
        data = ''
        for i in range(1,10):
            time.sleep(1)
            count = ser.inWaiting()
            if count != 0:
                buf = ser.read(count)
                data += buf
                print "s"
                if data != '':
                    logging.info(" ".join(("%02x" % n) for n in data))

def random_package():
    len = random.randint(2,30)
    rand_list = []
    for i in range(len):
        rand_list +=[random.randint(1,255)]
    return rand_list

def main():  
    t = threading.Thread(target=uart_recv)
    t.start()
    while True:  
        ser.write('hello')
        #ser.write(bytearray(random_package()))
        time.sleep(1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


