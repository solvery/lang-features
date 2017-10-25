
import struct

def gen_mac(type_id, mac_id):
    mac_addr = [0xd8, 0x80, 0x30, type_id, 0xca, mac_id]
    data_bin_array=''
    for data in range(0x0,0x100-6):
        data_bin = struct.pack('B', 0x0) 
        data_bin_array = data_bin_array + data_bin[0];
    
    for data in mac_addr:
        data_bin = struct.pack('B', data) 
        data_bin_array = data_bin_array + data_bin[0];
    return data_bin_array


for i in range(1,2+1):
    fn = "apto_v2p1_mac_fiber_tx_" + str(i) + ".bin"
    data_bin_array = gen_mac(0x12, i)
    with open(fn,'wb') as fd:
        fd.write(data_bin_array)

    fn = "apto_v2p1_mac_fiber_rx_" + str(i) + ".bin"
    data_bin_array = gen_mac(0x22, i)
    with open(fn,'wb') as fd:
        fd.write(data_bin_array)

    fn = "apto_v2p1_mac_copper_tx_" + str(i) + ".bin"
    data_bin_array = gen_mac(0x32, i)
    with open(fn,'wb') as fd:
        fd.write(data_bin_array)

    fn = "apto_v2p1_mac_copper_rx_" + str(i) + ".bin"
    data_bin_array = gen_mac(0x42, i)
    with open(fn,'wb') as fd:
        fd.write(data_bin_array)

