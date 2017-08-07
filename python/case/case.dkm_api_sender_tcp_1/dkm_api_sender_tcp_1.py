import socket
import datetime
import logging
import random
import threading
import struct 
import time
import sys
import os

# logging
formatter="%(asctime)s %(levelname)-12s %(message)s"

# to file
log_filename="log_"+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d.%H.%M.%S.%f')
logging.basicConfig( filename=log_filename, filemode="a", format=formatter, level=logging.INFO);

# to console
formatter = logging.Formatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_addr = sys.argv[1]
server_address = (ip_addr, 5555)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def data_recv():
    while True:  
        data = ''
        for i in range(1,10):
            time.sleep(0.2)
            data = sock.recv(8192)
            count = len(data)
            if count != 0:
                if data != '':
                    logging.info("recv: " + (" ".join(("%02x" % struct.unpack('B', n)) for n in data)))


def random_package():
    len = random.randint(100,255)
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    rand_list = [0x1b, c1, c2, len]
    for i in range(len):
        rand_list +=[random.randint(1,255)]
    return rand_list

def print_hex(data):
    logging.info(" ".join(("%02x" % n) for n in data))

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin

def send_cmd(cmd):
    ser.write(cmd)
    logging.info("send: ")
    print_hex(cmd)
    time.sleep(1.1)  

def random_cmd():
    logging.info(sys._getframe().f_code.co_name)
    cmd = bytearray(random_package())
    send_cmd(cmd)

def get_system_time():
    logging.info(sys._getframe().f_code.co_name)
    cmd = bytearray([0x1b, 0x28, 0x53])
    send_cmd(cmd)

def get_cpu_to_con():
    logging.info(sys._getframe().f_code.co_name)
    conid = random.randint(3000,3020)
    cmd = [0x1b, 0x5b, 0x48, 0x07, 0x00, conid%0x100, conid/0x100]
    send_cmd(bytearray(cmd))

def get_con_to_cpu():
    logging.info(sys._getframe().f_code.co_name)
    cpuid = random.randint(1000,1020)
    cmd = [0x1b, 0x5b, 0x4c, 0x07, 0x00, cpuid%0x100, cpuid/0x100]
    send_cmd(bytearray(cmd))

def get_all_connections():
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x5b, 0x52]
    send_cmd(bytearray(cmd))

def get_con_to_cpus():
    logging.info(sys._getframe().f_code.co_name)
    cpuid_list_len = random.randint(1,510)
    cpuid_list = []
    for i in range(cpuid_list_len):
        cpuid_list += [random.randint(1001, 1999)]
    cpu_cnt = len(cpuid_list)
    cmd_size = 7+cpu_cnt*2
    cmd = [0x1b, 0x5b, 0x4e, cmd_size%0x100, cmd_size/0x100, cpu_cnt%0x100, cpu_cnt/0x100]
    for i in range(cpu_cnt):
        cpu = [cpuid_list[i]%0x100, cpuid_list[i]/0x100]
        cmd += cpu
    logging.info("cmd len: %d" % len(cmd))
    send_cmd(bytearray(cmd))

def get_cpu_to_cons():
    logging.info(sys._getframe().f_code.co_name)
    conid_list_len = random.randint(1,510)
    conid_list = []
    for i in range(conid_list_len):
        conid_list += [random.randint(1001, 1999)]
    con_cnt = len(conid_list)
    cmd_size = 7+con_cnt*2
    cmd = [0x1b, 0x5b, 0x4a, cmd_size%0x100, cmd_size/0x100, con_cnt%0x100, con_cnt/0x100]
    for i in range(con_cnt):
        cpu = [conid_list[i]%0x100, conid_list[i]/0x100]
        cmd += cpu
    logging.info("cmd len: %d" % len(cmd))
    send_cmd(bytearray(cmd))

def get_con_list():
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x5b, 0x68, 0x07, 0x00, 0x00, 0x00]
    send_cmd(bytearray(cmd))

def get_user_list():
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x5b, 0x69, 0x07, 0x00, 0x00, 0x00]
    send_cmd(bytearray(cmd))

def get_cpu_list():
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x5b, 0x67, 0x07, 0x00, 0x00, 0x00]
    send_cmd(bytearray(cmd))


case_list1 = [random_cmd, get_system_time, get_cpu_to_con, get_con_to_cpu, get_cpu_to_cons, get_con_to_cpus, get_con_list, get_user_list, get_cpu_list]
case_list2 = [get_cpu_list]
case_list = case_list1

def send_cmd(cmd):
    sock.sendall(cmd)
    logging.info("")
    logging.info("send: ")
    print_hex(cmd)
    time.sleep(0.1)  

data_send1 = 'hello'

def main():  
    t = threading.Thread(target=data_recv)
    t.setDaemon(True)
    t.start()
    try:
        while True:  
            random.choice(case_list)()
            time.sleep(1.5)  
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

         
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if sock != None:  
            sock.close()


