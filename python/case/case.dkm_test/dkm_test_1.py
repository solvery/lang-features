# -*- coding: utf-8 -*  
import serial  
import struct
import time  

#  COM3修改成您老的使用的串口 
ser = serial.Serial("COM4", 115200)  
def main():  
    dkm_uart_send([0x16], [0x20])
    data = dkm_uart_read([0x16])
    print_hex(bin2hex(data))
    time.sleep(0.1)  

def uart_send(data):
    ser.write(data)  

def uart_recv():
    while True:  
        ser.flushInput()
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            return recv
        time.sleep(0.1)  

def dkm_uart_send(reg_addr, data):
    head = [0xAA, 0xAA, 0x55, 0x55, 0x01]
    pkg1 = head + reg_addr 
    checksum = cal_sum(pkg1)
    checksum_hex = list((checksum%0x100, checksum/0x100))
    pkg2 = pkg1 + checksum_hex
    uart_send(hex2bin(pkg2))
    print_hex(pkg2)
    ack = uart_recv()
    ack_hex = struct.unpack('B', ack[0])
    print_hex(ack_hex)
    if (ack_hex != 0xA5):
        print "write error"

def dkm_uart_read(reg_addr):
    head = [0xAA, 0xAA, 0x55, 0x55, 0x02]
    pkg1 = head + reg_addr
    checksum = cal_sum(pkg1)
    checksum_hex = list((checksum%0x100, checksum/0x100))
    pkg2 = pkg1 + checksum_hex
    print_hex(pkg2)
    uart_send(hex2bin(pkg2))
    data = uart_recv()
    return data

def cal_sum(data):
    data_sum = 0
    for d in data:
        data_sum = data_sum + d
    return data_sum
     
def bin2hex(data_bin):
    for d in data_bin:
        data_hex = data_hex + struct.unpack('B', d)
    return data_hex

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin

def print_hex(data):
    for d in data:
        print '%02x' % d,
    print
    return

if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


