# every byte bit reverse
import struct

binfile=open("file_in",'rb')    
data = binfile.read()

def reverse(x, n):
    result = 0
    for i in xrange(n):
        if (x >> i) & 1: result |= 1 << (n - 1 - i)
    return result

d_bin_all=''
for d in data:
    d_hex = struct.unpack('B', d)
    d_bin = struct.pack('B', reverse(d_hex[0], 8))
    d_bin_all = d_bin_all + d_bin;

binfile2=open("file_reverse",'wb')    
binfile2.write(d_bin_all)

