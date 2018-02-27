import crcmod

crc16 = crcmod.predefined.mkCrcFun('crc-16')

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
    a=byte_bit_reverse(s[0])
    b=byte_bit_reverse(s[1])
    c=byte_bit_reverse(s[2])
    d=byte_bit_reverse(s[3])
    return [d+c, b+a]

t1 = [0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x09]
string = "".join(chr(i) for i in t1)
r1 = "%04x" % crc16(string)
r2 = icron_crc_result(r1)
print r2
