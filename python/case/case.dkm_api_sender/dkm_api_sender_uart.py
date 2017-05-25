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
cmd_get_system_time = \
    [0x1b, 0x28, 0x53]
cmd_switch_off_all_ports = \
    [0x1b, 0x5b, 0x41]

def get_system_time():
    logging.info("get_system_time")
    uart_send(hex2bin(cmd_get_system_time))

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        second  = recv_bytes[5]
        minute  = recv_bytes[6]
        hour    = recv_bytes[7]
        day     = recv_bytes[8]
        date    = recv_bytes[9]
        month   = recv_bytes[10]
        year    = recv_bytes[11]
        logging.info("system time is: 20%02x-%02x-%02x 02x:%02x:%02x day:%02x" % (year, month, date, hour, minute, second))

def switch_off_all_ports():
    logging.info("switch_off_all_ports")
    uart_send(hex2bin(cmd_switch_off_all_ports))
    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    if (len(recv_bytes) == 1):
        if recv_bytes == 0x06:
            logging.info("ack")
        else:
            logging.error("nak")

def get_conn_ext(conid):
    cmd = [0x1b, 0x5b, 0x48, 0x07, 0x00, conid%0x100, conid/100]
    uart_send(hex2bin(cmd))

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        conid = recv_bytes[5] + recv_bytes[6]*0x100
        cpuid = recv_bytes[7] + recv_bytes[8]*0x100
        logging.info("conid=%04d, cpuid=%04d" % (conid, cpuid))

def check_size(data):
    if data[3] == len(data):
        return True
    else: 
        return False

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
        get_system_time()
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


