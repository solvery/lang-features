
import sys
import struct

production_num=int(sys.argv[1])
box_num=int(sys.argv[2])

def gen_mac(type_id, mac_id):
    a = mac_id/1000%10
    b = mac_id/100%10
    c = mac_id/10%10
    d = mac_id/1%10
    mac_addr = [0xd8, 0x80, 0x30, type_id, a*16+b, c*16+d]
    data_bin_array=''
    for data in range(0x0,0x100-6):
        data_bin = struct.pack('B', 0x0) 
        data_bin_array = data_bin_array + data_bin[0];
    
    for data in mac_addr:
        data_bin = struct.pack('B', data) 
        data_bin_array = data_bin_array + data_bin[0];
    mac_str = "-".join(("%02x" % n) for n in mac_addr)
    return data_bin_array, mac_str


for i in range(1,box_num+1):
    data_bin_array, mac_str = gen_mac(0x10+production_num, i)
    fn = "apto_mac_fiber_tx_" + mac_str + ".bin"
    with open(fn,'wb') as fd:
        fd.write(data_bin_array)

    data_bin_array, mac_str = gen_mac(0x20+production_num, i)
    fn = "apto_mac_fiber_rx_" + mac_str + ".bin"
    with open(fn,'wb') as fd:
        fd.write(data_bin_array)

#    fn = "apto_v2p1_mac_copper_tx_" + str(i) + ".bin"
#    data_bin_array = gen_mac(0x32, i)
#    with open(fn,'wb') as fd:
#        fd.write(data_bin_array)
#
#    fn = "apto_v2p1_mac_copper_rx_" + str(i) + ".bin"
#    data_bin_array = gen_mac(0x42, i)
#    with open(fn,'wb') as fd:
#        fd.write(data_bin_array)
#
