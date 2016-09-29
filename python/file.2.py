
import struct

binfile=open("file.3.in",'rb')    
data = binfile.read()

d_bin_all=''

for d in data:
	d_hex = struct.unpack('B', d)
	d_bin = struct.pack('B', d_hex[0])
	d_bin_all = d_bin_all + d_bin;

binfile2=open("file.2.in",'wb')    
binfile2.write(d_bin_all)
