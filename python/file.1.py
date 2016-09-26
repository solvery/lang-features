
import struct

binfile=open("file.1.in",'rb')    
data = binfile.read()

for i in range(0,len(data)):
	print "%c" % data[i]
	if (hex(data[i]) == '\x30'):
		print "hah"


