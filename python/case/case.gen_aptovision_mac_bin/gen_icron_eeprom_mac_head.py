
import struct
import sys
import os

def gen_mac_head(mac_p1, mac_p2):
    mac_addr = [0x01, 0xd8, 0x80, 0x30, mac_p1, 0x00, mac_p2]
    data_bin_array=''
    for data in mac_addr:
        data_bin = struct.pack('B', data) 
        data_bin_array = data_bin_array + data_bin[0];
    return data_bin_array

fn_tx=open("icron_demo_tx_body.bin",'rb').read()
fn_rx=open("icron_demo_rx_body.bin",'rb').read()
for i in range(1,4+1):
    fn = "icron_eeprom_tx_mac_" + str(i) + ".bin"
    data_bin_array = gen_mac_head(0xA2, i) + fn_tx
    with open(fn,'wb') as fd:
        fd.write(data_bin_array)


