
import struct

str1 = "hello"
for i in range(len(str1)):
    print str1[i], '(%d)' % i

for s in str1:
    print s

for d in foo:
	d1 = struct.unpack('b', d)
	print '%x' % d1
	if (d1[0] == 0x61):
		print "match"

