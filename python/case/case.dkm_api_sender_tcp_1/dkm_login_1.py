import socket
import datetime
import logging
import random
import threading
import struct 
import time
import sys
import os
import ftplib 

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

ip_addr = sys.argv[1]
logging.info("login test, ip addr: %s" % ip_addr)

for i in range(10000):
    ret = ''
    try:
        ftp = ftplib.FTP(ip_addr, timeout=2)
        ftp.connect()
        ret =  ftp.login(user='admin', passwd='admin')
        ftp.quit()
    except ftplib.all_errors as e:
        logging.info("error: %s" % e)

    if ret == '230 User logged in':
        logging.info("loggin ok")
