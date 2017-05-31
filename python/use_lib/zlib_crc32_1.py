import zlib 
import binascii

s = b'hello'
print zlib.crc32(s)
print binascii.crc32(s)
