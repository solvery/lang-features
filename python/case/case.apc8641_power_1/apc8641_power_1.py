#encoding=utf-8
import sys
import telnetlib
import time

port        = sys.argv[1]
delay_on    = int(sys.argv[2])
delay_off   = int(sys.argv[3])

# 配置选项
Host = '192.168.2.108'
username = 'apc'
password = 'apc'
finish = '>'
commands = ["whoami"]

tn = telnetlib.Telnet(Host, port=23, timeout=20)
tn.set_debuglevel(0)

def do_telnet():
    tn.read_until('User Name : ')
    tn.write(username + '\r')
    
    tn.read_until('Password  : ')
    tn.write(password + '\r')
      
    tn.read_until(finish)
    while True:
        tn.write('olOn ' + port + '\r')
        tn.read_until(finish)
        time.sleep(delay_on)

        tn.write('olOff ' + port + '\r')
        tn.read_until(finish)
        time.sleep(delay_off)
    
    tn.read_until(finish)
    tn.close() # tn.write('exit\n')

if __name__=='__main__':
    try:
        do_telnet()
    except KeyboardInterrupt:
        tn.write('%s\r' % 'olOff ' + port)
        tn.close() 
