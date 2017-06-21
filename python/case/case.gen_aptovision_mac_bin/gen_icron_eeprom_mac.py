
import struct
import sys

mac_p1 = int(sys.argv[1], 0)
mac_p2 = int(sys.argv[2], 0)

mac_addr = [0x01, 0x34, 0x1b, 0x22, 0x80, mac_p1, mac_p2]
data_bin_array=''
for data in mac_addr:
    data_bin = struct.pack('B', data) 
    data_bin_array = data_bin_array + data_bin[0];


with open("icron_mac_head.bin",'wb') as fd:
    fd.write(data_bin_array)

