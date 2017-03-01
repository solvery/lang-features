# -*- coding: utf-8 -*  
import serial  
import struct
import time  

#  COM3修改成您老的使用的串口 
ser = serial.Serial("COM3", 115200)  
def main():  
    while True:  
            
            for data in recv:
                data_hex = struct.unpack('B', data)
                print '%02x' % data_hex,
            print 
        ser.flushInput()  
        time.sleep(0.1)  

def uart_send(data):
    ser.write(data)  

def uart_recv():
    count = ser.inWaiting()  
    if count != 0:  
        recv = ser.read(count)  
        return recv

def dkm_uart_send(reg_addr, data):
    write_head = [0xAA, 0xAA, 0x55, 0x55, 0x01]
    write_checksum = cal_sum(data)
    write_pkg = write_head + reg_addr + write_checksum
    uart_send(write_pkg)
    write_ack = uart_recv()
    write_ack_hex = struct.unpack('B', write_ack)
    if (write_ack_hex != 0xA5):
        print "write error"

def dkm_uart_read(reg_addr):
    read_head = [0xAA, 0xAA, 0x55, 0x55, 0x02]
    read_pkg = read_head + reg_addr
    uart_send(read_pkg)
    read_data = uart_recv()
    read_data_hex = 
    read_checksum = cal_sum(read_data)

def cal_sum(data):
    data_sum = 0
    for d in data:
        data_sum = data_sum + d
    return data_sum
     
def bin2hex(data_hex):
    data=''
    for d in data_hex:
        data_hex = data_hex + struct.pack('B', d)
    return data_hex

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin

if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


