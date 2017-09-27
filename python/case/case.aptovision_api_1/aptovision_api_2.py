import time
import json

def nt_read(tn):
    s = tn.read_until('{')
    s += tn.read_very_eager()
    print "read: \n" + s
    return s
    
def do_telnet():
    import telnetlib
    host='192.168.2.7'
    port=6970
    tn = telnetlib.Telnet(host, port, timeout=20)
    tn.set_debuglevel(2)

    tn.write("mode human on" + '\n')
    json_str = nt_read(tn)
    tn.write("require blueriver_api 2.11.0" + '\n')
    json_str = nt_read(tn)

    tn.write(b"request 25\r\n")
    json_str = nt_read(tn)

    tn.close() 


if __name__=='__main__':
    do_telnet()
