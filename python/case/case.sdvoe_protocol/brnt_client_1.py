import socket
import sys
import struct
import time

bc_addr=('<broadcast>', 6969)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

def hex2bin(data_hex):
    data_bin=''
    for d in data_hex:
        data_bin = data_bin + struct.pack('B', d)
    return data_bin


data=hex2bin([0x07, 0x13, 0x03, 0x03, 0x01, 0x13, 0x97, 0x08, 0x01, 0x00, 0xd8, 0x80, 0x39, 0xa1, 0xca, 0x75, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00])
s.sendto(data, bc_addr)
time.sleep(0.1)

data=hex2bin([0x07, 0x13, 0x03, 0x03, 0x01, 0x13, 0x97, 0x08, 0x01, 0x00, 0xd8, 0x80, 0x39, 0xa1, 0xca, 0x75, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00])
s.sendto(data, bc_addr)
time.sleep(0.1)

data=hex2bin([0x07, 0x13, 0x03, 0x03, 0x01, 0x13, 0x97, 0x08, 0x11, 0x00, 0x4b, 0x17, 0x00, 0x00, 0x5e, 0x0f, 0x00, 0x00, 0x97, 0x08, 0x00, 0x00, 0x3b, 0x13, 0x00,0x00, 0xb0, 0x00, 0x05, 0x00, 0x80, 0x01, 0x1e, 0x22, 0x07, 0x00, 0x02, 0x00, 0x2f, 0x00, 0x02, 0x41, 0x00, 0x02, 0x20, 0x01, 0x77, 0x97, 0x00, 0x00,0x01, 0x03, 0x04, 0x06, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x41, 0x27, 0x27, 0x00, 0x02, 0x80, 0x22, 0x1b, 0x34, 0x00, 0x00,0x7f, 0x7b, 0x00, 0x00, 0x03])
s.sendto(data, bc_addr)
time.sleep(0.1)

data=hex2bin([0x07, 0x13, 0x03, 0x03, 0x01, 0x13, 0x97, 0x08, 0x14, 0x00, 0x08, 0x00, 0xd8, 0x80, 0x39, 0xa1, 0xca, 0x75, 0x00, 0xe1, 0x00, 0x00, 0x08, 0x01, 0x00,0x00, 0x00, 0x00, 0x00, 0x01, 0xa9, 0xfe, 0x76, 0xca, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x44, 0x38, 0x38, 0x30, 0x33, 0x39, 0x41, 0x31,0x43, 0x41, 0x37, 0x35, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x01, 0x01, 0x02, 0x40, 0x06, 0x84, 0x03, 0x00, 0x00, 0x00, 0x00, 0x3c,0x04, 0x03, 0x10, 0x00, 0x00, 0x00, 0x00, 0x78, 0x05, 0x1a, 0x04, 0x00, 0x00, 0x00, 0x00, 0x3c, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x01, 0x01, 0x04, 0x04, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0xa8, 0x02,0x71, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x11, 0x3c, 0x40,0x06, 0x84, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe1, 0x00, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0xe1, 0x00, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0xe1,0x00, 0x00, 0x08, 0x01, 0x00, 0x00, 0x02, 0x01, 0x18, 0x00, 0x71, 0x4a, 0x6e, 0x06, 0x08, 0x07, 0xe8, 0x03, 0x50, 0x00, 0x03, 0x00, 0x18, 0x00, 0x00,0x00, 0x00, 0x00, 0x0c, 0x08, 0x00, 0x00, 0x00, 0x00, 0x04, 0x01, 0x04, 0x00, 0x08, 0x00, 0x00, 0x00, 0x06, 0x01, 0x14, 0x00, 0xe0, 0x01, 0x01, 0xfd,0xe0, 0x01, 0x01, 0xfe, 0x5b, 0x3f, 0x39, 0x00, 0xe0, 0x01, 0x01, 0x01, 0xe0, 0x01, 0x03, 0xff, 0x07, 0x01, 0x04, 0x00, 0x04, 0x01, 0x00, 0x00, 0x08,0x01, 0x04, 0x00, 0x04, 0x07, 0x00, 0x00])
s.sendto(data, bc_addr)
time.sleep(0.1)

data=hex2bin([0x07, 0x13, 0x03, 0x03, 0x01, 0x13, 0x97, 0x08, 0x05, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x8a, 0x00, 0x80, 0xff, 0x8a, 0x00, 0x80, 0xd8, 0x80, 0x39,0xa1, 0xca, 0x75, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x4c, 0x2d, 0x4c, 0x0c,0x46, 0x53, 0x4d, 0x30, 0x0b, 0x1b, 0x01, 0x03, 0x80, 0x3d, 0x23, 0x78, 0x2a, 0x5f, 0xb1, 0xa2, 0x57, 0x4f, 0xa2, 0x28, 0x0f, 0x50, 0x54, 0xbf, 0xef,0x80, 0x71, 0x4f, 0x81, 0x00, 0x81, 0xc0, 0x81, 0x80, 0x95, 0x00, 0xa9, 0xc0, 0xb3, 0x00, 0x01, 0x01, 0x08, 0xe8, 0x00, 0x30, 0xf2, 0x70, 0x5a, 0x80,0xb0, 0x58, 0x8a, 0x00, 0x60, 0x59, 0x21, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x00, 0xfd, 0x00, 0x18, 0x4b, 0x1e, 0x87, 0x3c, 0x00, 0x0a, 0x20, 0x20, 0x20,0x20, 0x20, 0x20, 0x00, 0x00, 0x00, 0xfc, 0x00, 0x55, 0x32, 0x38, 0x45, 0x35, 0x39, 0x30, 0x0a, 0x20, 0x20, 0x20, 0x20, 0x20, 0x00, 0x00, 0x00, 0xff,0x00, 0x48, 0x54, 0x50, 0x4a, 0x33, 0x30, 0x31, 0x36, 0x31, 0x37, 0x0a, 0x20, 0x20, 0x01, 0x4f, 0x02, 0x03, 0x34, 0xf0, 0x4d, 0x61, 0x12, 0x03, 0x13,0x04, 0x20, 0x22, 0x1f, 0x10, 0x5f, 0x60, 0x5d, 0x5e, 0x23, 0x09, 0x07, 0x07, 0x83, 0x01, 0x00, 0x00, 0x6d, 0x03, 0x0c, 0x00, 0x20, 0x00, 0x80, 0x3c,0x20, 0x10, 0x60, 0x01, 0x02, 0x03, 0x67, 0xd8, 0x5d, 0xc4, 0x01, 0x78, 0x80, 0x03, 0xe3, 0x0f, 0x01, 0x04, 0x02, 0x3a, 0x80, 0x18, 0x71, 0x38, 0x2d,0x40, 0x58, 0x2c, 0x45, 0x00, 0x60, 0x59, 0x21, 0x00, 0x00, 0x1e, 0x02, 0x3a, 0x80, 0xd0, 0x72, 0x38, 0x2d, 0x40, 0x10, 0x2c, 0x45, 0x80, 0x60, 0x59,0x21, 0x00, 0x00, 0x1e, 0x01, 0x1d, 0x00, 0x72, 0x51, 0xd0, 0x1e, 0x20, 0x6e, 0x28, 0x55, 0x00, 0x60, 0x59, 0x21, 0x00, 0x00, 0x1e, 0x56, 0x5e, 0x00,0xa0, 0xa0, 0xa0, 0x29, 0x50, 0x30, 0x20, 0x35, 0x00, 0x60, 0x59, 0x21, 0x00, 0x00, 0x1a, 0x00, 0x00, 0x00, 0x74])
s.sendto(data, bc_addr)
time.sleep(0.1)

data=hex2bin([0x07, 0x13, 0x03, 0x03, 0x01, 0x13, 0x97, 0x08, 0x05, 0x00, 0x03, 0x00, 0x00, 0x00, 0x14, 0x81, 0x00, 0x80, 0x17, 0x81, 0x00, 0x80, 0xd8, 0x80, 0x39,0xa1, 0xca, 0x75, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf1, 0x83, 0xb0, 0x1c])
s.sendto(data, bc_addr)
time.sleep(0.1)
