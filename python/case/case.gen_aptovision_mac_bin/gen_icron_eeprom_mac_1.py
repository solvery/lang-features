
import struct
import sys
import os

production_num=int(sys.argv[1])
box_num=int(sys.argv[2])

def gen_mac_head(mac_p1, mac_p2):
    a = mac_p2/1000%10
    b = mac_p2/100%10
    c = mac_p2/10%10
    d = mac_p2/1%10
    mac_addr = [0x01, 0xd8, 0x80, 0x30, mac_p1, a*16+b, c*16+d]
    data_bin_array=''
    for data in mac_addr:
        data_bin = struct.pack('B', data) 
        data_bin_array = data_bin_array + data_bin[0];
    mac_str = "-".join(("%02x" % n) for n in mac_addr)
    return data_bin_array, mac_str

fn_tx_body=open("icron_demo_tx_body.bin",'rb').read()
fn_rx_body=open("icron_demo_rx_body.bin",'rb').read()
for i in range(1,box_num+1):
    data_tx, mac_str = gen_mac_head(0xA0+production_num, i) 
    fn = "icron_eeprom_tx_mac_" + mac_str + ".bin"
    with open(fn,'wb') as fd:
        fd.write(data_tx + fn_tx_body)

    data_rx, mac_str = gen_mac_head(0xB0+production_num, i)
    fn = "icron_eeprom_rx_mac_" + mac_str + ".bin"
    with open(fn,'wb') as fd:
        fd.write(data_rx + fn_rx_body)




