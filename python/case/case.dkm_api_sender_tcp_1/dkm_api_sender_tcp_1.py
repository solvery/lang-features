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
log_filename="log/log_"+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d.%H.%M.%S.%f')
logging.basicConfig( filename=log_filename, filemode="a", format=formatter, level=logging.INFO);

# to console
formatter = logging.Formatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_addr = sys.argv[1]
server_address = (ip_addr, 5555)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
logging.info("ip addr: %s" % ip_addr)

def data_recv():
    logging.info("start read")
    while True:  
        data = ''
        for i in range(1,10):
            time.sleep(0.2)
            try:
                data = sock.recv(8192)
            except:
                logging.info("disconnect")
                sys.exit(0)
            count = len(data)
            if count != 0:
                if data != '':
                    logging.info("recv: " + (" ".join(("%02x" % struct.unpack('B', n)) for n in data)))

def gen_random_data(a,b):
    len = random.randint(a,b)
    rand_list = []
    for i in range(len):
        rand_list +=[random.randint(28,255)]
    return rand_list

def random_package():
    len = random.randint(100,255)
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    rand_list = [0x1b, c1, c2, len]
    for i in range(len):
        rand_list +=[random.randint(28,255)]
    return rand_list

def print_hex(data):
    logging.info(" ".join(("%02x" % n) for n in data))

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin

def get_system_time_with_random_data(a,b):
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x28, 0x53]
    rand1 = gen_random_data(a,b)
    rand2 = gen_random_data(a,b)
    cmd = rand1 + cmd + rand2
    send_cmd(bytearray(cmd))

def get_system_time_with_random_data_split(a,b):
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x28, 0x53]
    rand1 = gen_random_data(a,b)
    rand2 = gen_random_data(a,b)
    cmd = rand1 + [0x1b]
    send_cmd(bytearray(cmd))
    cmd = [0x28, 0x53] + rand2
    send_cmd(bytearray(cmd))

def get_system_time_with_random_data_1():
    get_system_time_with_random_data( 5,10)
def get_system_time_with_random_data_2():
    get_system_time_with_random_data( 500,1001)
def get_system_time_with_random_data_3():
    get_system_time_with_random_data(16000,20001)
def get_system_time_with_random_data_split_1():
    get_system_time_with_random_data_split( 5,10)

def random_invalid_cmd():
    logging.info(sys._getframe().f_code.co_name)
    cmd = gen_random_data()
    send_cmd(bytearray(cmd))

def random_cmd():
    logging.info(sys._getframe().f_code.co_name)
    cmd = bytearray(random_package())
    send_cmd(cmd)

def get_system_time_split():
    logging.info(sys._getframe().f_code.co_name)
    cmd1 = bytearray([0x1b, 0x28])
    cmd2 = bytearray([0x53])
    send_cmd(cmd1)
    send_cmd(cmd2)

def get_system_time():
    logging.info(sys._getframe().f_code.co_name)
    cmd = bytearray([0x1b, 0x28, 0x53])
    send_cmd(cmd)

def get_cpu_to_con():
    logging.info(sys._getframe().f_code.co_name)
    conid = random.randint(0x0, 0xffff)
    cmd = [0x1b, 0x5b, 0x48, 0x07, 0x00, conid%0x100, conid/0x100]
    send_cmd(bytearray(cmd))

def get_con_to_cpu():
    logging.info(sys._getframe().f_code.co_name)
    cpuid = random.randint(0x0, 0xffff)
    cmd = [0x1b, 0x5b, 0x4c, 0x07, 0x00, cpuid%0x100, cpuid/0x100]
    send_cmd(bytearray(cmd))

def get_all_connections():
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x5b, 0x52]
    send_cmd(bytearray(cmd))

def get_con_to_cpus(a,b):
    logging.info(sys._getframe().f_code.co_name)
    cpuid_list_len = random.randint(a,b)
    cpuid_list = []
    for i in range(cpuid_list_len):
        cpuid_list += [random.randint(0x0, 0xffff)]
    cpu_cnt = len(cpuid_list)
    cmd_size = 7+cpu_cnt*2
    cmd = [0x1b, 0x5b, 0x4e, cmd_size%0x100, cmd_size/0x100, cpu_cnt%0x100, cpu_cnt/0x100]
    for i in range(cpu_cnt):
        cpu = [cpuid_list[i]%0x100, cpuid_list[i]/0x100]
        cmd += cpu
    logging.info("cmd len: %d" % len(cmd))
    send_cmd(bytearray(cmd))

def get_con_to_cpus_1():
    get_con_to_cpus(1,510)
def get_con_to_cpus_2():
    get_con_to_cpus(510,1024)
def get_con_to_cpus_3():
    get_con_to_cpus(4000,4096)


def get_cpu_to_cons():
    logging.info(sys._getframe().f_code.co_name)
    conid_list_len = random.randint(1,510)
    conid_list = []
    for i in range(conid_list_len):
        conid_list += [random.randint(0x0, 0xffff)]
    con_cnt = len(conid_list)
    cmd_size = 7+con_cnt*2
    cmd = [0x1b, 0x5b, 0x4a, cmd_size%0x100, cmd_size/0x100, con_cnt%0x100, con_cnt/0x100]
    for i in range(con_cnt):
        con = [conid_list[i]%0x100, conid_list[i]/0x100]
        cmd += con 
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

def set_con_and_cpu():
    logging.info(sys._getframe().f_code.co_name)
    cpu_con = [random.randint(0x00, 0xffff), random.randint(0x0, 0xffff)]
    #cpu_con = [3001,1001]
    cmd = [0x1b, 0x5b, 0x50, 0x09, 0x00]
    con = [cpu_con[0]%0x100, cpu_con[0]/0x100]
    cpu = [cpu_con[1]%0x100, cpu_con[1]/0x100]
    cmd += cpu + con
    send_cmd(bytearray(cmd))

case_list1 = [get_system_time, get_cpu_to_con, get_con_to_cpu, get_con_to_cpus_1, get_cpu_to_cons, set_con_and_cpu]
case_list2 = [random_cmd]
case_list3 = [get_con_list, get_user_list, get_cpu_list]
case_list = case_list1

case_all_rand_1 = []
case_all_rand_2 = [get_system_time]
case_get_system_time_with_random_data = [get_system_time_with_random_data_1]
case_get_system_time_with_random_data_1 = [get_system_time_with_random_data_1]
case_get_system_time_with_random_data_2 = [get_system_time_with_random_data_2]
case_get_system_time_with_random_data_3 = [get_system_time_with_random_data_3]
case_get_system_time_split = [get_system_time_split]
case_get_system_time_with_random_data_split_1 = [get_system_time_with_random_data_split_1]
case_get_system_time = [get_system_time]

def send_cmd(cmd):
    try:
        sock.sendall(cmd)
    except:
        logging.info("disconnect")
        sys.exit(0)
    logging.info("send: ")
    print_hex(cmd)
    logging.info("")

data_send1 = 'hello'

def run_case(case, delay, times=0):
    logging.info("run %s" % case)
    t = threading.Thread(target=data_recv)
    t.setDaemon(True)
    t.start()
    try:
        if times == 0:
            while True:
                random.choice(case)()
                time.sleep(delay)
        else:
            for i in range(times):
                random.choice(case)()
                time.sleep(delay)
        logging.info("end test")
        sock.close()
        sys.exit(1)
    except KeyboardInterrupt:  
        logging.info("ctrl-c")
        sock.close()
        sys.exit(1)
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

         
if __name__ == '__main__':  
    try:  
        run_case(case_list2, 0.1)
    except KeyboardInterrupt:  
        if sock != None:  
            sock.close()

