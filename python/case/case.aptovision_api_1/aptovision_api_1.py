import time
    
def do_telnet():
    import telnetlib
    host='127.0.0.1'
    port=6970
    tn = telnetlib.Telnet(host, port, timeout=20)
    tn.set_debuglevel(2)

    tn.write("mode human on" + '\n')
    ret = tn.read_until('{')
    ret += tn.read_very_eager()
    print "read: \n" + ret 
    tn.close() 


if __name__=='__main__':
    do_telnet()
