# -*- coding: utf-8 -*  
import sys
import serial  
import struct
import time  

serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 115200)

def uart_recv():
    data = ''
    for i in range(1,10):
        time.sleep(0.2)
        count = ser.inWaiting()
        if count != 0:
            buf = ser.read(count)
            data += buf
        else:
            if data != '':
                return data
            else:
                return '\b0'

def print_hex(data):
    print (" ".join(("%02x" % n) for n in data))

def gen_sum(data):
    data_sum = 0
    for d in data:
        data_sum = data_sum + d
    d1 = data_sum % 0x100
    d2 = data_sum / 0x100 % 0x100
    return [d1, d2]

def cmd_get_version():
    print sys._getframe().f_code.co_name
    cmd = [0x1b, 0x3c, 0x55, 0x03]
    cmd = cmd + gen_sum(cmd)
    #print_hex(cmd)
    return cmd


def cmd_get_data(addr):
    print sys._getframe().f_code.co_name

    a1 = addr%0x100
    a2 = addr/0x100%0x100
    a3 = addr/0x10000%0x100
    cmd = [0x1b, 0x3c, 0x55, 0x02, a1, a2, a3]
    cmd = cmd + gen_sum(cmd)
    #print_hex(cmd)
    return cmd

def cmd_flash_erase(addr):
    print sys._getframe().f_code.co_name
    a1 = addr%0x100
    a2 = addr/0x100%0x100
    a3 = addr/0x10000%0x100
    cmd = [0x1b, 0x3c, 0x55, 0x00, a1, a2, a3] 
    cmd = cmd + gen_sum(cmd)
    #print_hex(cmd)
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
    #print "data len: %d" % len(data)
    #print_hex(cmd)
    return cmd

def partition(lst, partition_size):
    if partition_size < 1:
        partition_size = 1
    return [
        lst[i:i + partition_size]
        for i in range(0, len(lst), partition_size)
    ]

def get_file_data(fn):
    print sys._getframe().f_code.co_name

    with open(fn,'rb') as fd_in:
        data_in = fd_in.read()
    print "data package len: 0x%x" % len(data_in)

    data_append = '\0'*(0x100 - len(data_in)%0x100)
    data = data_in + data_append
    print "data append  len: 0x%x" % len(data)
    return data

def bin2hex(data_bin):
    data_hex_array = []
    for d in data_bin:
        data_hex = struct.unpack('B', d)
        data_hex_array = data_hex_array + [data_hex[0]]
    return data_hex_array

def main():  

    flash_start_addr = 0x0
    #flash_start_addr = 0x10000
    #flash_start_addr = 0x400000
    #cmd = cmd_get_version()
    #ser.write(cmd)
    #recv = uart_recv()
    #recv_bytes = bin2hex(recv)
    #print_hex(recv_bytes)
    #time.sleep(0.5)  

    data_out = ''
    for i in range(0x40):
        cmd = cmd_get_data(flash_start_addr + 0x10000 * i)
        ser.write(cmd)
        recv = uart_recv()
        data_out = data_out + recv[4:]
        recv_bytes = bin2hex(recv)
        print_hex(recv_bytes)
        time.sleep(0.3)  

    with open("data_out.bin",'wb') as fd_in:
        fd_in.write(data_out)
    

    i = 0
    cmd  = cmd_flash_erase(flash_start_addr + 0x10000 * i)
    #cmd  = cmd_flash_erase(0x400000 + 0x10000 * i)
    ser.write(cmd)
    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    time.sleep(0.3)  
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


