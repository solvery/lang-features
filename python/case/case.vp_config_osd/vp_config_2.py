# -*- coding: utf-8 -*  
import serial  
import struct
import time  

config_data_hex = [0x80, 0x81, 0x82, 0x83, 0x00, 0x00, 0xc8, 0x00, 0xc8, 0x01, 0x90, 0x00, 0x50, 0x80, 0x23];

#  COM3修改成您老的使用的串口 
ser = serial.Serial("COM3", 115200)  
def main():  
    data_bin_array=''
    while True:  
        for data in config_data_hex:
            data_bin = struct.pack('B', data) 
            data_bin_array = data_bin_array + data_bin[0]
        ser.write(data_bin_array)
        ser.flushInput()  
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


