#http://www.jb51.net/article/47999.htm

import struct

binfile=open("file.1.in",'rb')    
data = binfile.read()

d_sum=0

for d in data:
	d_hex = struct.unpack('B', d)
	d_sum = d_sum + d_hex[0]
	print "%02x %02x" % (d_hex[0], d_sum)
	
print "%02x" % (d_sum%256)
