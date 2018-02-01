import sys
import time
import json

def nt_read(tn):
    s = tn.read_until('{')
    s += tn.read_very_eager()
    #print "read: \n" + s
    return s
    
def do_telnet():
    import telnetlib
    #host='127.0.0.1'
    ip_addr = sys.argv[1]
    host=ip_addr
    port=6970
    tn = telnetlib.Telnet(host, port, timeout=20)
    tn.set_debuglevel(0)

    tn.write("mode human on" + '\r\n')
    nt_read(tn)
    tn.write("require blueriver_api 2.11.0" + '\r\n')
    nt_read(tn)

    tn.write("get ALL list" + '\r\n')
    json_str = nt_read(tn)
    json_parsed = json.loads(json_str)
    devices = json_parsed['result']['devices']
    for i in range(len(devices)):
        status = json_parsed['result']['devices'][i]['status']['active']
        device_id = str(json_parsed['result']['devices'][i]['device_id'])
        if status == True:
            print device_id, status

    tn.close() 


if __name__=='__main__':
    do_telnet()
