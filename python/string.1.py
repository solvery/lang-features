
import struct

foo = "abc"
for i in range(len(foo)):
    print foo[i], '(%d)' % i

for d in foo:
	print '%x' % struct.unpack('b', d)

