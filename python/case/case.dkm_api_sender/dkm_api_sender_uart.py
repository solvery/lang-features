#encoding=utf-8

import sys
import serial  
import struct
import time  
import logging

#  COM3修改成您老的使用的串口 
serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 115200)  

# logging
formatter="%(asctime)s %(levelname)-12s %(message)s"

logging.basicConfig(
        filename="dkm_api_sender_uart.log",
        filemode="a",
        format=formatter,
        level=logging.INFO);

#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象
formatter = logging.Formatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# API命令

def get_system_time():
    logging.info("get_system_time")
    cmd = [0x1b, 0x28, 0x53]
    uart_send(hex2bin(cmd))

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)
    
    if len(recv_bytes) >= 1:
        if recv_bytes == 0x1b:
            logging.error("head is not 0x1b")
    else:
        logging.error("recv size == 0")

    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        second  = recv_bytes[5]
        minute  = recv_bytes[6]
        hour    = recv_bytes[7]
        week    = recv_bytes[8]
        date    = recv_bytes[9]
        month   = recv_bytes[10]
        year    = recv_bytes[11]
        logging.info("system time is: 20%02x-%02x-%02x %02x:%02x:%02x week:%x" % (year, month, date, hour, minute, second, week))

def switch_off_all_ports():
    logging.info("switch_off_all_ports")
    cmd = [0x1b, 0x5b, 0x41]
    uart_send(hex2bin(cmd))
    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    if (len(recv_bytes) == 1):
        if recv_bytes[0] == 0x06:
            logging.info("ack")
        else:
            logging.error("nak")

# 1B 5B 48--- 6.2.2 Get CPU device connected to CON device
def get_cpu_to_con(conid):
    logging.info("get_cpu_to_con, conid=%04d" % (conid))
    cmd = [0x1b, 0x5b, 0x48, 0x07, 0x00, conid%0x100, conid/0x100]
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    if len(recv_bytes) == 1 :
        logging.warn("nak")
        return
        
    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        conid = recv_bytes[5] + recv_bytes[6]*0x100
        cpuid = recv_bytes[7] + recv_bytes[8]*0x100
        logging.info("CON=%04d, CPU=%04d" % (conid, cpuid))

def check_size(data):
    #print "%d %d" % (data[3], len(data))
    if (data[3]) == (len(data)):
        return True
    else: 
        return False

def uart_send(data):
    ser.write(data)  
    logging.info("uart write")

def uart_recv():
    while True:  
        #ser.flushInput()
        logging.info("uart read")
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            return recv
        time.sleep(0.1)  

def print_hex(data):
    logging.info(" ".join(("%02x" % n) for n in data))

def bin2hex(data_bin):
    data_hex_array = []
    for d in data_bin:
        data_hex = struct.unpack('B', d)
        data_hex_array = data_hex_array + [data_hex[0]]
    return data_hex_array

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin


def main():  
    while True:  
        get_system_time()
        switch_off_all_ports()

        for conid in range(3001, 3009):
            get_cpu_to_con(conid)
            time.sleep(1)  
        time.sleep(1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


