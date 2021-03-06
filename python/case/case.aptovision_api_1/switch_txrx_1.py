import sys
import time
import random
import json

import telnetlib
#host='127.0.0.1'

if len(sys.argv) <= 1:
    ip_addr='127.0.0.1'
else:
    ip_addr = sys.argv[1]
host=ip_addr
port=6970
tn = telnetlib.Telnet(host, port, timeout=20)
tn.set_debuglevel(0)

def nt_read(tn):
    s = tn.read_until('{')
    s += tn.read_very_eager()
    #print "read: \n" + s
    return s
    
def cmd_send(cmd):
    tn.write(cmd + ' \r')
    json_str = nt_read(tn)
    json_parsed = json.loads(json_str)
    request_id = str(json_parsed['request_id'])
    
    time.sleep(1)
    tn.write('request ' + request_id + '\r\n')
    json_str = nt_read(tn)
    print cmd
    print json_str

def do_telnet():

    tn.write("mode human on" + '\n')
    nt_read(tn)
    tn.write("require blueriver_api 2.11.0" + '\n')
    nt_read(tn)

    tx_list = ['d8803012ca01', 'd8803012ca02','d8803032ca02','d88039a1ca75']
    rx_list = ['d8803022ca02', 'd88039a1d77f']
    while True:
        tx_id = random.choice(tx_list)
        for rx_id in rx_list:
            cmd = 'join ' + tx_id +':HDMI:0 ' + rx_id + ':HDMI:0'
            cmd_send(cmd)
        time.sleep(5)
    tn.close() 

if __name__=='__main__':
    do_telnet()

