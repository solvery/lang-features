
import struct

data_bin_array=''
for data in range(0x0,0x100):
    data_bin = struct.pack('B', data) 
    data_bin_array = data_bin_array + data_bin[0];

with open("data.bin",'wb') as fd:
    fd.write(data_bin_array)

