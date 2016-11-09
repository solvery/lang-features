# -*- coding: utf-8 -*  
import serial  
import time  
import datetime
import struct 

ser = serial.Serial("/dev/ttyUSB0", 230400)  


def main():  
    pkg_cnt = 0
    pkg_body = ''
    pkg_body_last = ''
    pkg_body_match = [0x1b]
    is_pkg_body_match = False
    while True:  
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            for d in recv:
                data_hex = struct.unpack('B', d)
                if data_hex[0] == 0x1b:
                	print "\033[1;32;40m%02x\033[0m" % data_hex,  # set color
                else:
                	print '%02x' % data_hex,
                pkg_cnt = pkg_cnt + 1
                if (pkg_cnt % 32 == 0):
                	print
        ser.flushInput()  
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  
