import struct

int_array = range(1,10)
bytearray(int_array)
struct.pack('B' * len(int_array), *int_array)
bytes(int_array)

"".join( chr( val ) for val in int_array )
"".join(map(chr, int_array))
