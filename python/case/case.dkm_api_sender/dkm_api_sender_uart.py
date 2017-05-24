#encoding=utf-8

import serial  
import struct
import time  

cmd_get_system_time = [0x1b, 0x28, 0x53]

#  COM3修改成您老的使用的串口 
ser = serial.Serial("COM3", 115200)  


def get_system_time()
    uart_send(hex2bin(cmd_get_system_time))
    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    

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

def bin2hex(data_bin):
    for d in data_bin:
        data_hex = data_hex + struct.unpack('B', d)
    return data_hex

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin


def main():  
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


