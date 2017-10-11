
import struct

mac_addr = [0xd8, 0x80, 0x39, 0xa1, 0xca, 0x50]
data_bin_array=''
for data in range(0x0,0x100-6):
    data_bin = struct.pack('B', 0x0) 
    data_bin_array = data_bin_array + data_bin[0];

for data in mac_addr:
    data_bin = struct.pack('B', data) 
    data_bin_array = data_bin_array + data_bin[0];


with open("aptovision_mac.bin",'wb') as fd:
    fd.write(data_bin_array)

