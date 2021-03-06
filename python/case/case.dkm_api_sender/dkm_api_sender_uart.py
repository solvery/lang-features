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
    logging.info("api get_system_time")
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
    logging.info("api switch_off_all_ports")
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
    logging.info("api get_cpu_to_con, conid=%04d" % (conid))
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
    logging.info("api get_con_to_cpu, cpuid=%04d" % (cpuid))
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

# 1B 5B 52--- 6.2.12 Get all connections
def get_all_connections():
    logging.info("api get_all_connections")
    cmd = [0x1b, 0x5b, 0x52]
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    # 有的会返回nak 
    if len(recv_bytes) == 1 :
        logging.warn("nak")
        return
        
    if check_size(recv_bytes) == False:
        logging.error("check_size error")
    else:
        cpu_cnt = recv_bytes[5]
        con_cnt = recv_bytes[7]
        for i in range(cpu_cnt):
            cpuid = recv_bytes[ 9+i*4] + recv_bytes[10+i*4]*0x100
            conid = recv_bytes[11+i*4] + recv_bytes[12+i*4]*0x100
            logging.info("GET CON=%04d, CPU=%04d" % (conid, cpuid))
        for i in range(con_cnt):
            conid = recv_bytes[ 9+cpu_cnt*4+i*4] + recv_bytes[10+cpu_cnt*4+i*4]*0x100
            cpuid = recv_bytes[11+cpu_cnt*4+i*4] + recv_bytes[12+cpu_cnt*4+i*4]*0x100
            logging.info("GET CON=%04d, CPU=%04d" % (conid, cpuid))

# 1B 5B 4E--- 6.2.8 Get CON devices connected to CPU devices
def get_con_to_cpus(cpuid_list):
    logging.info("api get_con_to_cpus")
    cpu_cnt = len(cpuid_list)
    cmd_size = 7+cpu_cnt*2
    cmd = [0x1b, 0x5b, 0x4e, cmd_size, 0x00, cpu_cnt, 0x00]
    for i in range(cpu_cnt):
        cpu = [cpuid_list[i]%0x100, cpuid_list[i]/0x100]
        logging.info("get_con_to_cpus, cpuid=%04d" % (cpuid_list[i]))
        cmd += cpu 
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
        con_cnt = recv_bytes[5]
        for i in range(con_cnt):
            cpuid = recv_bytes[7+i*4] + recv_bytes[8+i*4]*0x100
            conid = recv_bytes[9+i*4] + recv_bytes[10+i*4]*0x100
            logging.info("GET CON=%04d, CPU=%04d" % (conid, cpuid))

# 6.2.23 Get CON List
def get_con_list(index):
    logging.info("api get_con_list")
    cmd = [0x1b, 0x5b, 0x68, 0x07, 0x00, index, 0x00]
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
        cnt = recv_bytes[5]
        nxt = recv_bytes[7]
        if cnt > 0:
            logging.info("cnt=%d next=%s" % (cnt, nxt))
            for i in range(cnt):
                conid = recv_bytes[9+i*24] + recv_bytes[10+i*24]*0x100
                name = ''
                for i in range(13+i*24, 33+i*24):
                    if recv_bytes[i] != 0x0:
                        name += struct.pack('B', recv_bytes[i])
                logging.info("conid=%04d name=%s" % (conid, name))
        else:
            logging.info("no con in list")


# 6.2.23 Get User List
def get_user_list(index):
    logging.info("api get_user_list")
    cmd = [0x1b, 0x5b, 0x69, 0x07, 0x00, index, 0x00]
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
        cnt = recv_bytes[5]
        nxt = recv_bytes[7]
        if cnt > 0:
            logging.info("cnt=%d next=%s" % (cnt, nxt))
            for i in range(cnt):
                userid = recv_bytes[9+i*24] + recv_bytes[10+i*24]*0x100
                name = ''
                for i in range(13+i*24, 33+i*24):
                    if recv_bytes[i] != 0x0:
                        name += struct.pack('B', recv_bytes[i])
                logging.info("userid=%04d name=%s" % (userid, name))
        else:
            logging.info("no user in list")

# 6.2.22 Get CPU List
def get_cpu_list(index):
    logging.info("api get_cpu_list")
    cmd = [0x1b, 0x5b, 0x67, 0x07, 0x00, index, 0x00]
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
        cnt = recv_bytes[5]
        nxt = recv_bytes[7]
        if cnt > 0:
            logging.info("cnt=%d next=%s" % (cnt, nxt))
            for i in range(cnt):
                cpuid = recv_bytes[9+i*24] + recv_bytes[10+i*24]*0x100
                name = ''
                for i in range(13+i*24, 33+i*24):
                    if recv_bytes[i] != 0x0:
                        name += struct.pack('B', recv_bytes[i])
                logging.info("cpuid=%04d name=%s" % (cpuid, name))
        else:
            logging.info("no cpu in list")


# 1B 5B 4A--- 6.2.4 Get CPU devices connected to CON devices
def get_cpu_to_cons(conid_list):
    logging.info("api get_cpu_to_cons")
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


# 6.2.14 Set extended connection
def set_extended_connection(cpu_con_mode):
    logging.info("api set_extended_connection")
    cmd = [0x1b, 0x5b, 0x62, 0x0b, 0x00]
    con = [cpu_con_mode[0]%0x100, cpu_con_mode[0]/0x100]
    cpu = [cpu_con_mode[1]%0x100, cpu_con_mode[1]/0x100]
    mod = [cpu_con_mode[2]%0x100, cpu_con_mode[2]/0x100]
    logging.info("set_extended_connection, conid=%04d cpuid=%04d, mode=%d" % (cpu_con_mode[0], cpu_con_mode[1], cpu_con_mode[2]))
    cmd += cpu + con + mod# notice
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    if len(recv_bytes) != 1 :
        logging.error("respone len != 1")
        return
    if recv_bytes[0] == 0x06:
        logging.info("set_con_and_cpu ok")
    else:
        logging.error("nak")

# 6.2.15 Set connection of CON device to CPU device (bidirectional, port mode)
def set_port_con_and_cpu(conport, cpuport):
    logging.info("api set_port_con_and_cpu")
    cmd = [0x1b, 0x5b, 0x43, 0x09, 0x00]
    con = [conport%0x100, conport/0x100]
    cpu = [cpuport%0x100, cpuport/0x100]
    logging.info("set_port_con_and_cpu, conport=%04d cpuport=%04d" % (conport, cpuport))
    cmd += con + cpu # notice
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    if len(recv_bytes) != 1 :
        logging.error("respone len != 1")
        return
    if recv_bytes[0] == 0x06:
        logging.info("set_port_con_and_cpu ok")
    else:
        logging.error("nak")

# 1B 5B 50--- 6.2.10 Set CON device connection to CPU device(bidirectional)
def set_con_and_cpu(cpu_con):
    logging.info("api set_con_and_cpu")
    cmd = [0x1b, 0x5b, 0x50, 0x09, 0x00]
    con = [cpu_con[0]%0x100, cpu_con[0]/0x100]
    cpu = [cpu_con[1]%0x100, cpu_con[1]/0x100]
    logging.info("set_con_and_cpu, conid=%04d cpuid=%04d" % (cpu_con[0], cpu_con[1]))
    cmd += cpu + con # notice
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    if len(recv_bytes) != 1 :
        logging.error("respone len != 1")
        return
    if recv_bytes[0] == 0x06:
        logging.info("set_con_and_cpu ok")
    else:
        logging.error("nak")

# 1B 5B 4F--- 6.2.9 Set connection of CON devices to CPU devices
def set_con_to_cpus(con_cpu_pairs):
    logging.info("api set_con_to_cpus")
    con_cnt = len(con_cpu_pairs)/2
    cmd_size = 7+con_cnt*4
    cmd = [0x1b, 0x5b, 0x4f, cmd_size, 0x00, con_cnt, 0x00]
    for i in range(con_cnt):
        con = [con_cpu_pairs[i*2]%0x100, con_cpu_pairs[i*2]/0x100]
        cpu = [con_cpu_pairs[i*2+1]%0x100, con_cpu_pairs[i*2+1]/0x100]
        logging.info("set_cpu_to_cons, conid=%04d cpuid=%04d" % (con_cpu_pairs[i*2+1], con_cpu_pairs[i*2]))
        cmd += cpu + con # notice
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

# 1B 5B 51--- 6.2.11 Set connection of CON devices to CPU devices(bidirectional)
def set_con_and_cpus(con_cpu_pairs):
    logging.info("api set_con_and_cpus")
    con_cnt = len(con_cpu_pairs)/2
    cmd_size = 7+con_cnt*4
    cmd = [0x1b, 0x5b, 0x51, cmd_size, 0x00, con_cnt, 0x00]
    for i in range(con_cnt):
        con = [con_cpu_pairs[i*2]%0x100, con_cpu_pairs[i*2]/0x100]
        cpu = [con_cpu_pairs[i*2+1]%0x100, con_cpu_pairs[i*2+1]/0x100]
        logging.info("set_con_and_cpus, conid=%04d cpuid=%04d" % (con_cpu_pairs[i*2], con_cpu_pairs[i*2+1]))
        cmd += cpu + con # notice
    uart_send(hex2bin(cmd))
    print_hex(cmd)

    recv = uart_recv()
    recv_bytes = bin2hex(recv)
    print_hex(recv_bytes)

    if len(recv_bytes) != 1 :
        logging.error("respone len != 1")
        return
    if recv_bytes[0] == 0x06:
        logging.info("set_con_and_cpus ok")
    else:
        logging.error("nak")


# 1B 5B 53--- 6.2.13 Set connection for all CON devices and CPU devices
def set_all_connections(con_cpu_pairs1, con_cpu_pairs2):
    logging.info("api set_all_connections")

    pairs_cnt1 = len(con_cpu_pairs1)/2
    pairs_cnt2 = len(con_cpu_pairs2)/2
    cmd_size = 9+pairs_cnt1*4+pairs_cnt2*4
    cmd = [0x1b, 0x5b, 0x53, cmd_size, 0x00, pairs_cnt1, 0x00, pairs_cnt2, 0x00]
    for i in range(pairs_cnt1):
        con = [con_cpu_pairs1[i*2]%0x100, con_cpu_pairs1[i*2]/0x100]
        cpu = [con_cpu_pairs1[i*2+1]%0x100, con_cpu_pairs1[i*2+1]/0x100]
        logging.info("set_cpu_to_cons, conid=%04d cpuid=%04d" % (con_cpu_pairs1[i*2], con_cpu_pairs1[i*2+1]))
        cmd += cpu + con
    for i in range(pairs_cnt2):
        con = [con_cpu_pairs2[i*2]%0x100, con_cpu_pairs2[i*2]/0x100]
        cpu = [con_cpu_pairs2[i*2+1]%0x100, con_cpu_pairs2[i*2+1]/0x100]
        logging.info("set_con_and_cpus, conid=%04d cpuid=%04d" % (con_cpu_pairs2[i*2], con_cpu_pairs2[i*2+1]))
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
        logging.info("set_all_connections ok")
    else:
        logging.error("nak")


# 1B 5B 4B--- 6.2.5 Set connections of CPU devices to CON devices
def set_cpu_to_cons(con_cpu_pairs):
    logging.info("api set_cpu_to_cons")
    con_cnt = len(con_cpu_pairs)/2
    cmd_size = 7+con_cnt*4
    cmd = [0x1b, 0x5b, 0x4b, cmd_size, 0x00, con_cnt, 0x00]
    for i in range(con_cnt):
        con = [con_cpu_pairs[i*2]%0x100, con_cpu_pairs[i*2]/0x100]
        cpu = [con_cpu_pairs[i*2+1]%0x100, con_cpu_pairs[i*2+1]/0x100]
        logging.info("set_cpu_to_cons, conid=%04d cpuid=%04d" % (con_cpu_pairs[i*2], con_cpu_pairs[i*2+1]))
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


# 1B 5B 4D--- 6.2.7 Set CON device connection to CPU device
def set_con_to_cpu(conid, cpuid):
    logging.info("api set_cpu_to_con, conid=%04d, cpuid=%04d" % (conid, cpuid))
    cmd = [0x1b, 0x5b, 0x4d, 0x09, 0x00, cpuid%0x100, cpuid/0x100, conid%0x100, conid/0x100]
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

 # 1B 5B 49--- 6.2.3 Set CPU device connection to CON device
def set_cpu_to_con(conid, cpuid):
    logging.info("api set_cpu_to_con, conid=%04d, cpuid=%04d" % (conid, cpuid))
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

    size = data[3] + data[4]*0x100
    if (size) == (len(data)):
        return True
    else: 
        return False

def uart_send(data):
    ser.write(data)  
    logging.info("uart write")

def uart_recv():
    logging.info("uart read")
    data = ''
    for i in range(1,10):
        logging.info("uart read")
        time.sleep(0.2)  
        count = ser.inWaiting()  
        if count != 0:  
            buf = ser.read(count)  
            data += buf
        else:
            if data != '':
                return data
            else:
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
        get_user_list(0)
        time.sleep(2)
    while True:  
        set_extended_connection([3001, 1001, 1])

        get_all_connections()
        time.sleep(1)  
        
        switch_off_all_ports()
        time.sleep(1)  
        get_cpu_to_cons(conid_list=[3001, 3002, 3003, 3004, 3005, 3006])
        time.sleep(1)  
        set_con_and_cpus(con_cpu_pairs=[3001, 1001, 3002, 1002, 3006, 1003])
        time.sleep(1)  
        get_cpu_to_cons(conid_list=[3001, 3002, 3003, 3004, 3005, 3006])
        time.sleep(1)  

        switch_off_all_ports()
        time.sleep(1)  
        set_con_and_cpu([3006, 1003])
        time.sleep(1)  
        get_con_to_cpu(cpuid=1003)
        time.sleep(1)  

        switch_off_all_ports()
        time.sleep(1)  
        get_cpu_to_cons(conid_list=[3001, 3002, 3003, 3004, 3005, 3006])
        time.sleep(1)  
        set_con_to_cpus(con_cpu_pairs=[3001, 1001, 3002, 1002, 3006, 1003])
        time.sleep(1)  
        get_cpu_to_cons(conid_list=[3001, 3002, 3003, 3004, 3005, 3006])
        time.sleep(1)  

        set_cpu_to_cons(con_cpu_pairs=[3001, 1001, 3002, 1002, 3006, 1003])
        time.sleep(1)  
        get_con_to_cpus(cpuid_list=[1001, 1002, 1003, 1004, 1005, 1006])
        time.sleep(1)  
        get_cpu_to_cons(conid_list=[3001, 3002, 3003, 3004, 3005, 3006])
        time.sleep(1)  

        get_con_to_cpu(cpuid=1003)
        time.sleep(1)  
        get_con_to_cpus(cpuid_list=[1003])
        time.sleep(1)  
        set_cpu_to_cons(con_cpu_pairs=[3001, 1001, 3002, 1002])
        time.sleep(1)  
        get_con_to_cpus(cpuid_list=[1001, 1002, 1003, 1004, 1005, 1006])
        time.sleep(1)  

        get_system_time()
        time.sleep(1)  
        switch_off_all_ports()
        time.sleep(1)  

        for conid in range(3001, 3009):
            get_cpu_to_con(conid)
            time.sleep(1)  

        switch_off_all_ports()
        time.sleep(1)  
        set_cpu_to_con(cpuid=1003, conid=3006)
        time.sleep(1)  

        get_cpu_to_cons(conid_list=[3001, 3002, 3003, 3004, 3005, 3006])
        time.sleep(1)  
        set_cpu_to_cons(con_cpu_pairs=[3006, 1003])
        time.sleep(1)  
        set_cpu_to_cons(con_cpu_pairs=[3001, 1001, 3002, 1002])
        time.sleep(1)  

        get_con_to_cpu(cpuid=1003)
        for i in range(1001, 1020):
            get_con_to_cpu(cpuid=i)
            time.sleep(1)

        set_con_to_cpu(cpuid=1003, conid=3006)

        time.sleep(1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


