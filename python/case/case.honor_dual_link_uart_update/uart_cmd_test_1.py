# -*- coding: utf-8 -*  
import sys
import serial  
import struct
import time  

serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 115200)

def gen_sum(data):
    data_sum = 0
    for d in data:
        data_sum = data_sum + d
    d1 = data_sum % 0x100
    d2 = data_sum / 0x100 % 0x100
    return [d1, d2]

def cmd_flash_erase(addr):
    a1 = addr%0x100
    a2 = addr/0x100%0x100
    a3 = addr/0x10000%0x100
    cmd = [0x1b, 0x3c, 0x55, 0x00, a1, a2, a3] 
    cmd = cmd + gen_sum(cmd)
    return cmd

def main():  
    cmd  = cmd_flash_erase(0x10000 * 0)
    ser.write(cmd)
    while True:  
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            ser.write(recv)  
            
            for data in recv:
                data_hex = struct.unpack('B', data)
                print '%02x' % data_hex,
            print 
        ser.flushInput()  
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


