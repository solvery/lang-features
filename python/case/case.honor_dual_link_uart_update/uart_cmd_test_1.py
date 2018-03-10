# -*- coding: utf-8 -*  
import sys
import serial  
import struct
import time  

serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 115200)

def print_hex(data):
    print (" ".join(("%02x" % n) for n in data))

def gen_sum(data):
    data_sum = 0
    for d in data:
        data_sum = data_sum + d
    d1 = data_sum % 0x100
    d2 = data_sum / 0x100 % 0x100
    return [d1, d2]

def cmd_flash_erase(addr):
    print sys._getframe().f_code.co_name
    a1 = addr%0x100
    a2 = addr/0x100%0x100
    a3 = addr/0x10000%0x100
    cmd = [0x1b, 0x3c, 0x55, 0x00, a1, a2, a3] 
    cmd = cmd + gen_sum(cmd)
    print_hex(cmd)
    return cmd

def cmd_flash_write(addr, data):
    print sys._getframe().f_code.co_name

    a1 = addr%0x100
    a2 = addr/0x100%0x100
    a3 = addr/0x10000%0x100

    #cmd = [0x1b, 0x3c, 0x55, 0x01, a1, a2, a3] + range(0x0,0x100,2)+ range(0x0,0x100,2)
    #cmd = [0x1b, 0x3c, 0x55, 0x01, a1, a2, a3] + range(0x0,0x100)
    cmd = [0x1b, 0x3c, 0x55, 0x01, a1, a2, a3] + data

    cmd = cmd + gen_sum(cmd)
    print "data len: %d" % len(data)
    print_hex(cmd)
    return cmd

def partition(lst, partition_size):
    if partition_size < 1:
        partition_size = 1
    return [
        lst[i:i + partition_size]
        for i in range(0, len(lst), partition_size)
    ]

def get_file_data(fn):
    with open(fn,'rb') as fd_in:
        data_in = fd_in.read()
    data = []
    for d in data_in:
        d_hex = struct.unpack('B', d)
	data = data + [d_hex[0]]
    data_append = [0]*(0x100 - len(data)%0x100)
    data = data + data_append
    data_matrix = partition(data, 0x100)
    return data_matrix

def main():  

    for i in range(0x100):
        cmd  = cmd_flash_erase(0x10000 * i)
        ser.write(cmd)
        time.sleep(0.2)  

    data_matrix = get_file_data("ten_gig_eth_pcs_pma_0_example_design.bin")
    #data_matrix = get_file_data("data.bin")
    print "data package len: %d" % len(data_matrix)
    for i in range(len(data_matrix)):
        cmd  = cmd_flash_write(0x10000 * i, data_matrix[i])
        ser.write(cmd)
        time.sleep(0.1)  
    exit()
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


