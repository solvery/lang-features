
import struct

d_bin_all=''

for d in range(0x0,0xff):
	d_bin = struct.pack('B', d)
	d_bin_all = d_bin_all + d_bin;

with open("file.3.in",'wb') as fd_in:
	fd_in.write(d_bin_all)

