
import struct

foo = "abc"
for i in range(len(foo)):
    print foo[i], '(%d)' % i

for d in foo:
	d1 = struct.unpack('b', d)
	print '%x' % d1
	print type(d1[0])
	if (d1[0] == 0x61):
		print "match"

