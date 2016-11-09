# -*- coding: utf-8 -*  
import serial  
import time  
import datetime
import struct 
import sys

ser = serial.Serial("/dev/ttyUSB0", 230400)  

def main():  
    pkg_cnt = 0
    pkg_body = ''
    pkg_body_last = ''
    pkg_body_match = [0x1b, 0x28, 0x4a]
    is_pkg_body_match = False
    is_diff = False

    while True:  
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            for d in recv:
                data_hex = struct.unpack('B', d)
                if data_hex[0] == 0x1b:

                    # check if the package is match the pkg_body_match.
                    for i in (range(len(pkg_body_match))):
                        if ((len(pkg_body_match) <= len(pkg_body)) and (pkg_body_match[i] == ord(pkg_body[i]))):
                            is_pkg_body_match = True
                        else:
                            is_pkg_body_match = False
                            break

                    # only print out the matched package.
                    if (is_pkg_body_match == True):
                        print "package size : %d" % pkg_cnt
                        print datetime.datetime.strftime(datetime.datetime.now(), '%y-%m-%d %H:%M:%S.%f')
                        for i in range(len(pkg_body)):
                            if (i < len(pkg_body_last) and pkg_body_last[i] == pkg_body[i]):
                        	    print "%02x" % ord(pkg_body[i]), 
                            else:
                        	    print "\033[1;32;40m%02x\033[0m" % ord(pkg_body[i]),  # set color
                        	    #print "%02x" % ord(pkg_body[i]),  # without color
                        	    is_diff = True;

                            if ((i+1) % 50 == 0): # line return 
                        	    print " -- %d" % ((i+1)/50) 

                        print "" # end of print package body.

                        if (is_diff == True):
                        	print "diff -----------------------------------------------"
                        print ""

                        pkg_body_last = pkg_body
                        is_diff = False

                    pkg_cnt = 0 
                    pkg_body = ''
                    is_pkg_body_match = False
                #print '%02x' % data_hex,
                pkg_cnt = pkg_cnt + 1
                pkg_body = pkg_body + chr(data_hex[0]) 

        ser.flushInput()  
        sys.stdout.flush()
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  

