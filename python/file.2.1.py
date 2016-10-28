
import struct

binfile=open("file.3.in",'rb')    
data = binfile.read()

d_bin_all=''

for d in data:
	d_bin_all = d_bin_all + d;

binfile2=open("file.2.in",'wb')    
binfile2.write(d_bin_all)
