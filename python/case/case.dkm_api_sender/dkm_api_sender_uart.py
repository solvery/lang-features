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

    if len(recv_bytes) != 1 :
        logging.error("respone len != 1")
        return
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

    # 有的conid会返回nak 
    if len(recv_bytes) == 1 :
        logging.warn("nak")
        return
        
    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        conid = recv_bytes[5] + recv_bytes[6]*0x100
        cpuid = recv_bytes[7] + recv_bytes[8]*0x100
        logging.info("CON=%04d, CPU=%04d" % (conid, cpuid))

# 1B 5B 4C--- 6.2.6 Get CON device connected to CPU device
def get_con_to_cpu(cpuid):
    logging.info("get_con_to_cpu, cpuid=%04d" % (cpuid))
    cmd = [0x1b, 0x5b, 0x4c, 0x07, 0x00, cpuid%0x100, cpuid/0x100]
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    # 有的cpuid会返回nak 
    if len(recv_bytes) == 1 :
        logging.warn("nak")
        return
        
    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        cpuid = recv_bytes[5] + recv_bytes[6]*0x100
        conid = recv_bytes[7] + recv_bytes[8]*0x100
        logging.info("CON=%04d, CPU=%04d" % (conid, cpuid))

# 1B 5B 4A--- 6.2.4 Get CPU devices connected to CON devices
# 获得的是主机内部的连接关系，外设不存在也可以获得
def get_cpu_to_cons(conid_list):
    logging.info("get_cpu_to_cons")
    con_cnt = len(conid_list)
    cmd_size = 7+con_cnt*2
    cmd = [0x1b, 0x5b, 0x4a, cmd_size, 0x00, con_cnt, 0x00]
    for i in range(con_cnt):
        con = [conid_list[i]%0x100, conid_list[i]/0x100]
        logging.info("get_cpu_to_cons, conid=%04d" % (conid_list[i]))
        cmd += con
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    # 有的conid会返回nak 
    if len(recv_bytes) == 1 :
        logging.warn("nak")
        return
        
    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        con_cnt = recv_bytes[5]
        for i in range(con_cnt):
            conid = recv_bytes[7+i*4] + recv_bytes[8+i*4]*0x100
            cpuid = recv_bytes[9+i*4] + recv_bytes[10+i*4]*0x100
            logging.info("GET CON=%04d, CPU=%04d" % (conid, cpuid))


# 1B 5B 4B--- 6.2.5 Set connections of CPU devices to CON devices
def set_cpu_to_cons(cpu_con_list):
    logging.info("set_cpu_to_cons")
    con_cnt = len(cpu_con_list)/2
    cmd_size = 7+con_cnt*4
    cmd = [0x1b, 0x5b, 0x4b, cmd_size, 0x00, con_cnt, 0x00]
    for i in range(con_cnt):
        con = [cpu_con_list[i*2]%0x100, cpu_con_list[i*2]/0x100]
        cpu = [cpu_con_list[i*2+1]%0x100, cpu_con_list[i*2+1]/0x100]
        logging.info("set_cpu_to_cons, conid=%04d cpuid=%04d" % (cpu_con_list[i*2], cpu_con_list[i*2+1]))
        cmd += con + cpu
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    if len(recv_bytes) != 1 :
        logging.error("respone len != 1")
        return
    if recv_bytes[0] == 0x06:
        logging.info("set_cpu_to_cons ok")
    else:
        logging.error("nak")


# 1B 5B 49--- 6.2.3 Set CPU device connection to CON device
def set_cpu_to_con(conid, cpuid):
    logging.info("set_cpu_to_con, conid=%04d, cpuid=%04d" % (conid, cpuid))
    cmd = [0x1b, 0x5b, 0x49, 0x09, 0x00, conid%0x100, conid/0x100, cpuid%0x100, cpuid/0x100]
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    if len(recv_bytes) != 1 :
        logging.error("respone len != 1")
        return
    if recv_bytes[0] == 0x06:
        logging.info("SET CON=%04d CPU=%04d" % (conid, cpuid))
    else:
        logging.error("nak")
    

def check_size(data):
    #print "%d %d" % (data[3], len(data))
    if len(data) < 4:
        logging.info("check size <3")
        return False

    if (data[3]) == (len(data)):
        return True
    else: 
        return False

def uart_send(data):
    ser.write(data)  
    logging.info("uart write")

def uart_recv():
    for i in range(1,10):
        logging.info("uart read")
        count = ser.inWaiting()  
        if count != 0:  
            recv = ser.read(count)  
            return recv
        #ser.flushInput()
        time.sleep(0.1)  
    return '\b0'

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
    logging.info("dkm_api_sender_uart start")
    while True:  
        get_con_to_cpu(cpuid=1003)
        time.sleep(2)  
    while False:  
        get_system_time()
        switch_off_all_ports()

        for conid in range(3001, 3009):
            get_cpu_to_con(conid)
            time.sleep(1)  

        switch_off_all_ports()
        set_cpu_to_con(cpuid=1003, conid=3006)

        get_cpu_to_cons(conid_list=[3001, 3002, 3003, 3004, 3005, 3006])
        set_cpu_to_cons(cpu_con_list=[3006, 1003])
        set_cpu_to_cons(cpu_con_list=[3001, 1001, 3002, 1002])

        time.sleep(1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


