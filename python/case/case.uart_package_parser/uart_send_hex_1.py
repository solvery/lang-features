# -*- coding: utf-8 -*  
import serial  
import time  
import datetime
import struct 

ser = serial.Serial("/dev/ttyUSB0", 115200)  

def main():  
    pkg_body = [0x1b, 0x3c, 0x08, 0x00, 0x01, 0x00, 0x06]
	ser.write(pkg_body)
    while True:  
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            for d in recv:
                data_hex = struct.unpack('B', d)
                print '%02x' % data_hex,
        ser.flushInput()  
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  
