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

    tn.write("mode human on" + '\n')
    nt_read(tn)
    tn.write("require blueriver_api 2.11.0" + '\n')
    nt_read(tn)

    tn.write("reboot ALL " + '\r')
    json_str = nt_read(tn)
    json_parsed = json.loads(json_str)
    request_id = str(json_parsed['request_id'])
    
    time.sleep(1)
    tn.write('request ' + request_id + '\r\n')
    json_str = nt_read(tn)
    print json_str
    tn.close() 


if __name__=='__main__':
    do_telnet()