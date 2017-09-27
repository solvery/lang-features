import time
import json

def nt_read(tn):
    s = tn.read_until('{')
    s += tn.read_very_eager()
    print "read: \n" + s
    return s
    
def do_telnet():
    import telnetlib
    #host='127.0.0.1'
    host='192.168.2.7'
    port=6970
    tn = telnetlib.Telnet(host, port, timeout=20)
    tn.set_debuglevel(0)

    tn.write("mode human on" + '\n')
    nt_read(tn)
    tn.write("require blueriver_api 2.11.0" + '\n')
    nt_read(tn)

    tn.write("test ALL memory" + '\r')
    json_str = nt_read(tn)
    json_parsed = json.loads(json_str)
    request_id = str(json_parsed['request_id'])
    
    time.sleep(2)
    tn.write('request ' + request_id + '\r\n')
    json_str = nt_read(tn)
    json_parsed = json.loads(json_str)
    device_test = json_parsed['result']['device_test']
    for i in range(len(device_test)):
        result = json_parsed['result']['device_test'][i]['memory']
        device_id = str(json_parsed['result']['device_test'][i]['device_id'])
        if result == 'PASS':
            print device_id, " PASS"
            tn.write('set ' + device_id +' property nodes[LED:0].configuration.function.value 8\r\n')
            tn.read_very_eager()
        else:
            print device_id, " FAIL"
            tn.write('set ' + device_id +' property nodes[LED:0].configuration.function.value 1\r\n')
            tn.read_very_eager()

    tn.close() 


if __name__=='__main__':
    do_telnet()
