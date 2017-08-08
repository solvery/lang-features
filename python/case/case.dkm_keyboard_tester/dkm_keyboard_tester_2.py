# -*- coding: utf-8 -*  
import serial  
import struct
import time  
import sys

#  COMx修改成您老的使用的串口 
serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 9600)  

def hex2bin(data):
    data_bin_array=''
    for d in data:
        data_bin_array = data_bin_array + struct.pack('B', d)
    return data_bin_array

def hid_send(data, sleep=0):
    ser.write(data)  
    time.sleep(sleep)  

key_lshift  = hex2bin([0x82, 0x00])
key_esc     = hex2bin([0x1b])
key_enter   = hex2bin([0x0a])
key_bs      = hex2bin([0x08])
key_space   = hex2bin([0x20])
key_add     = hex2bin([0x2b])
key_sub     = hex2bin([0x2d])
key_tab     = hex2bin([0x80, 0x2b])
key_pageup  = hex2bin([0x80, 0x4b])
key_pagedown= hex2bin([0x80, 0x4e])
key_right   = hex2bin([0x80, 0x4f])
key_left    = hex2bin([0x80, 0x50])
key_down    = hex2bin([0x80, 0x51])
key_up      = hex2bin([0x80, 0x52])

key_f12     = hex2bin([0x80, 0x45])

sso=key_lshift + key_lshift + 'o'
escx2=key_esc + key_esc

def main():  
    #while True:  
    
    hid_send(key_lshift + key_esc)
    hid_send(key_f12, 3)
    hid_send(key_enter, 3)
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  



