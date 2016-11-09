# -*- coding: utf-8 -*  
import serial  
import struct
import time  

#  COM3修改成您老的使用的串口 
ser = serial.Serial("COM5", 115200)  
def main():  

    pkg_len = 0
    pkg_size = 254
    pkg_sum = 0
    pkg_cnt = 0
    pkg_index = 0

    # 读取数据到数组
    with open("data.bin",'rb') as fd_in:
        data_in = fd_in.read()

    pkg_len = len(data_in)
    print 'pkg len %d' % pkg_len

    while True:  
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            
            for data in recv:
                data_hex = struct.unpack('B', data)
                if data_hex[0] == 0x0A:
                    # 收到ack
                    # 准备数据
                    pkg_data = data_in[pkg_index:pkg_index+pkg_size];
                    pkg_len  = len(pkg_data)

                    # 文件末尾，补充补充数据
                    if pkg_len<pkg_size:
                        for i in range(pkg_len, pkg_size):
                            pkg_data = pkg_data+ '\0'
                            
                    # 文件内容为0，退出
                    if pkg_len == 0:
                        return

                    pkg_sum = cal_sum(pkg_data)

                    print 'pkg_cnt = %d' % pkg_cnt ,
                    print 'pkg_len = %d' % pkg_len ,
                    print 'pkg_sum = %04X' % pkg_sum 

                    # 发送数据
                    pkg_sum_str = struct.pack('BB', pkg_sum/0x100, pkg_sum%0x100)
                    pkg_data = pkg_data + pkg_sum_str
                    ser.write(pkg_data)

                    pkg_cnt = pkg_cnt + 1;
                    pkg_index = pkg_index + pkg_size
                      
                if data_hex[0] == 0xA0:
                    print 'get nak'
            #print 
        ser.flushInput()  
        time.sleep(0.1)  

def cal_sum(data):
    data_sum = 0
    for d in data:
        d_hex = struct.unpack('B', d)
        data_sum = data_sum + d_hex[0];
    return data_sum

if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


