

pin_dict_1={}
with open('pin1.txt','rb') as f:
    for line in f:
        pin_dict_1[line] = 1

pin_dict_2={}
with open('pin2.txt','rb') as f:
    for line in f:
        pin_dict_2[line] = 1

for key_pin1 in pin_dict_1:
    if (key_pin1 not in pin_dict_2.keys()):
        print key_pin1,
