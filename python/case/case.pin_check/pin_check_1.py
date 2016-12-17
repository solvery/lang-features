
pin_dict_1={}
with open('pin1.txt','rb') as f:
    for line in f:
        pin_dict_1[line] = 1

for key in pin_dict_1:
    print key,
