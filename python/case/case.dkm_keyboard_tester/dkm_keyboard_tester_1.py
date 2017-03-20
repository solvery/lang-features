# -*- coding: utf-8 -*  
import serial  
import struct
import time  

ascii_code = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+\|';:/?.,<>~"

#  COMx修改成您老的使用的串口 
ser = serial.Serial("COM4", 9600)  
def main():  
    while True:  
        ser.write(ascii_code)  
            
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  



