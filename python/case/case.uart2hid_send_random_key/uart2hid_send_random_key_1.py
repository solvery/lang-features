
# -*- coding: utf-8 -*  
import serial  
import struct
import time  
import datetime
import random
import sys

#  COMx修改成您老的使用的串口 
serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 9600)  

list_delay_time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

def hex2bin(data):
    data_bin_array=''
    for d in data:
        data_bin_array = data_bin_array + struct.pack('B', d)
    return data_bin_array

def hid_send(data, sleep=0.1):
    for d in data:
        ser.write(d)
        time.sleep(random.choice(list_delay_time))
    time.sleep(sleep)

key_lctrl_d = hex2bin([0x81, 0x07])
key_lctrl_c = hex2bin([0x81, 0x06])
key_f12     = hex2bin([0x80, 0x45])


def main():  
    hid_send(key_f12)
    hid_send(key_lctrl_c)
    while 1:
        data_fn="keyboard_data_"+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d.%H.%M.%S.%f')
        print data_fn
        hid_send('\n')
        hid_send('cat > ' + data_fn + '\n')
        with open('data.txt', 'r') as fd:
            data = fd.read()
            hid_send(data)
        hid_send(key_lctrl_d)
        time.sleep(1)
        #hid_send('md5sum data\n')
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        hid_send(key_lctrl_c)
        hid_send(key_f12)
        if ser != None:  
            ser.close()  



