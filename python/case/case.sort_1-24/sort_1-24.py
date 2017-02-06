
for x in range(1,24+1):
    for y in range(1,24+1):
        val = float(x)/y
        val_x27 = val *27 
        print ("%02.08f = %02d/%02d    %02.08f" % (val, x, y, val_x27))
