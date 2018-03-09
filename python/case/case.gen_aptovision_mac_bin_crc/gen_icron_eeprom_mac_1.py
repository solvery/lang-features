import crcmod
import struct
import sys
import os

production_num=int(sys.argv[1])
box_num=int(sys.argv[2])
crc16 = crcmod.predefined.mkCrcFun('crc-16')

icron_config_table1 = [\
#	0x01, 0xD8, 0x80, 0x30, 0xA4, 0x00, 0x01, 0x00, 0x00, 0x00, 0xD1, 0xDE, 0xFF, 0xFF, 0xFF, 0xFF, \
	0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x01, 0xC9, 0xA5, 0xFF, 0xFF, 0xFF, 0xFF, \
	0x01, 0x34, 0x1B, 0x22, 0x80, 0x36, 0xEF, 0x00, 0x00, 0x02, 0xE8, 0x16, 0x00, 0x00, 0x00, 0x00, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x03, 0x8C, 0x43, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x04, 0x0E, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x05, 0x8D, 0x03, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x06, 0x8F, 0x83, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x07, 0x0C, 0x80, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x08, 0x0E, 0xA0, 0xFF, 0xFF, 0xFF, 0xFF, \
	0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x09, 0x39, 0xCA, 0xFF, 0xFF, 0xFF, 0xFF]

icron_config_table2 = [\
#	0x01, 0xA9, 0xFE, 0x04, 0x01, 0x00, 0x00, 0x00, 0x00, 0x0A, 0x91, 0x32, 0x00, 0x00, 0x00, 0x00, \
	0x01, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0B, 0x58, 0x4F, 0x00, 0x00, 0x00, 0x00, \
	0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x8A, 0x03, 0x00, 0x00, 0x00, 0x00, \
	0x01, 0xC0, 0xA8, 0x02, 0x01, 0x00, 0x00, 0x00, 0x00, 0x0D, 0x97, 0x53, 0x00, 0x00, 0x00, 0x00, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0E, 0x0F, 0xE0, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0F, 0x8C, 0xE3, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x10, 0x0E, 0xF0, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x11, 0x8D, 0xF3, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x12, 0x8F, 0x73, 0xFF, 0xFF, 0xFF, 0xFF, \
	0x01, 0x2E, 0x2C, 0x6F, 0x4F, 0x00, 0x00, 0x00, 0x00, 0x13, 0x6A, 0xBB, 0x00, 0x00, 0x00, 0x00, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x14, 0x8E, 0x33, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0x01, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0B, 0x58, 0x4F, 0x00, 0x00, 0x00, 0x00, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

icron_config_table3 = [\
#	0x01, 0xA9, 0xFE, 0x04, 0x01, 0x00, 0x00, 0x00, 0x00, 0x0A, 0x91, 0x32, 0x00, 0x00, 0x00, 0x00, \
	0x01, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0B, 0x58, 0x4F, 0x00, 0x00, 0x00, 0x00, \
	0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x8A, 0x03, 0x00, 0x00, 0x00, 0x00, \
	0x01, 0xC0, 0xA8, 0x02, 0x01, 0x00, 0x00, 0x00, 0x00, 0x0D, 0x97, 0x53, 0x00, 0x00, 0x00, 0x00, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0E, 0x0F, 0xE0, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0F, 0x8C, 0xE3, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x10, 0x0E, 0xF0, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x11, 0x8D, 0xF3, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x12, 0x8F, 0x73, 0xFF, 0xFF, 0xFF, 0xFF, \
	0x01, 0xC4, 0xA1, 0x77, 0x5B, 0x00, 0x00, 0x00, 0x00, 0x13, 0xCD, 0xAA, 0x00, 0x00, 0x00, 0x00, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x14, 0x8E, 0x33, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, \
	0x01, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0B, 0x58, 0x4F, 0x00, 0x00, 0x00, 0x00, \
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

def byte_bit_reverse(n):
    tab={}
    tab['0']='0' 
    tab['1']='8'
    tab['2']='4'
    tab['3']='c'
    tab['4']='2'
    tab['5']='a'
    tab['6']='6'
    tab['7']='e'
    tab['8']='1'
    tab['9']='9'
    tab['a']='5'
    tab['b']='d'
    tab['c']='3'
    tab['d']='b'
    tab['e']='7'
    tab['f']='f'
    return tab[n]

def icron_crc_result(s):
    r1 = "".join(chr(i) for i in s)
    r2 = "%04x" % crc16(r1)
    a=byte_bit_reverse(r2[0])
    b=byte_bit_reverse(r2[1])
    c=byte_bit_reverse(r2[2])
    d=byte_bit_reverse(r2[3])
    return list(bytearray.fromhex(d+c+b+a))


def gen_mac_head(mac_p1, mac_p2):
    a = mac_p2/1000%10
    b = mac_p2/100%10
    c = mac_p2/10%10
    d = mac_p2/1%10
    mac_addr = [0xd8, 0x80, 0x30, mac_p1, a*16+b, c*16+d]
    for data in mac_addr:
        data_bin = struct.pack('B', data) 
    mac_str = "-".join(("%02x" % n) for n in mac_addr)
    return mac_addr, mac_str


for i in range(1,box_num+1):
    mac_addr, mac_str = gen_mac_head(0xA0+production_num, i) 
    r0 = [0x01] + mac_addr + [0x00, 0x00, 0x00]
    mac_addr_crc = icron_crc_result(r0)

    icron_data1 = r0 + mac_addr_crc + [0xFF, 0xFF, 0xFF, 0xFF]
    ip_addr = [0x01, 0xa9, 0xfe, 10+production_num, i, 0x00, 0x00, 0x00, 0x00, 0x0a]
    ip_addr_crc = icron_crc_result(ip_addr)
    icron_data2 = ip_addr + ip_addr_crc + [0x00, 0x00, 0x00, 0x00]
    icron_data = icron_data1 + icron_config_table1 + icron_data2 + icron_config_table2
    icron_data_bin = "".join(chr(i) for i in icron_data)

    fn = "icron_eeprom_tx_mac_" + mac_str + ".bin"
    with open(fn,'wb') as fd:
        fd.write(icron_data_bin)

    mac_addr, mac_str = gen_mac_head(0xB0+production_num, i) 
    r0 = [0x01] + mac_addr + [0x00, 0x00, 0x00]
    mac_addr_crc = icron_crc_result(r0)

    icron_data1 = r0 + mac_addr_crc + [0xFF, 0xFF, 0xFF, 0xFF]
    ip_addr = [0x01, 0xa9, 0xfe, 10+production_num, i, 0x00, 0x00, 0x00, 0x00, 0x0a]
    ip_addr_crc = icron_crc_result(ip_addr)
    icron_data2 = ip_addr + ip_addr_crc + [0x00, 0x00, 0x00, 0x00]
    icron_data = icron_data1 + icron_config_table1 + icron_data2 + icron_config_table3
    icron_data_bin = "".join(chr(i) for i in icron_data)

    fn = "icron_eeprom_rx_mac_" + mac_str + ".bin"
    with open(fn,'wb') as fd:
        fd.write(icron_data_bin)

