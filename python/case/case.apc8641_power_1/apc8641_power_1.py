#encoding=utf-8
import sys
import telnetlib
import time
import logging
import datetime

port        = sys.argv[1]
delay_on    = int(sys.argv[2])
delay_off   = int(sys.argv[3])

# 配置选项
Host = '192.168.2.108'
username = 'apc'
password = 'apc'
finish = '>'
commands = ["whoami"]

# log
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

# telnet
tn = telnetlib.Telnet(Host, port=23, timeout=20)
tn.set_debuglevel(0)

def do_telnet():
    tn.read_until('User Name : ')
    tn.write(username + '\r')
    
    tn.read_until('Password  : ')
    tn.write(password + '\r')
      
    tn.read_until(finish)
    while True:
        logging.info('power on')
        tn.write('olOn ' + port + '\r')
        tn.read_until(finish)
        time.sleep(delay_on)

        logging.info('power off')
        tn.write('olOff ' + port + '\r')
        tn.read_until(finish)
        time.sleep(delay_off)
    
    tn.read_until(finish)
    tn.close() # tn.write('exit\n')

if __name__=='__main__':
    try:
        logging.info('port=%s on=%d off=%d' % (port, delay_on, delay_off))
        do_telnet()
    except KeyboardInterrupt:
        logging.info('ctrl-c')
        tn.write('%s\r' % 'olOff ' + port)
        tn.close() 
