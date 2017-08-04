# -*- coding: utf-8 -*  
import sys
import datetime 
import serial  
import struct
import time  
import logging
import random
import threading
import struct

serial_port = sys.argv[1]
ser = serial.Serial(serial_port, 115200)

# logging
formatter="%(asctime)s %(levelname)-12s %(message)s"

# to file
log_filename="log_"+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d.%H.%M.%S.%f')
logging.basicConfig( filename=log_filename, filemode="a", format=formatter, level=logging.INFO);

# to console
formatter = logging.Formatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def uart_recv():
    logging.info("uart read")
    while True:  
        data = ''
        for i in range(1,10):
            time.sleep(0.4)
            count = ser.inWaiting()
            if count != 0:
                buf = ser.read(count)
                data += buf
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

def get_con_list():
    logging.info(sys._getframe().f_code.co_name)
    cmd = [0x1b, 0x5b, 0x68, 0x07, 0x00, 0x00, 0x00]
    send_cmd(bytearray(cmd))

case_list1 = [random_cmd, get_system_time, get_cpu_to_con]
case_list2 = [get_con_list]
case_list = case_list2

def main():  
    t = threading.Thread(target=uart_recv)
    t.start()
    while True:  
        logging.info("")
        random.choice(case_list)()
        time.sleep(1.5)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


