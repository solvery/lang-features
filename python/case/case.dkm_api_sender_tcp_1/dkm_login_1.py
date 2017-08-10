import socket
import datetime
import logging
import random
import threading
import struct 
import time
import sys
import os
from ftplib import FTP

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


ftp = FTP('192.168.100.99')
for i in range(10):
    print ftp.login(user='admin', passwd='admin')
