
name_len = map(len, ["hao", "chen", "coolshell"])
print name_len
# 输出 [3, 4, 9]

def toUpper(item):
    return item.upper()

upper_name = map(toUpper, ["hao", "chen", "coolshell"])
print upper_name
# 输出 ['HAO', 'CHEN', 'COOLSHELL']

# not functional
upname =['HAO', 'CHEN', 'COOLSHELL']
lowname =[] 
for i in range(len(upname)):
    lowname.append( upname[i].lower() )

## lambda
squares = map(lambda x: x * x, range(9))
	print squares
# 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64]

## not functional
num =[2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8]
positive_num_cnt = 0
positive_num_sum = 0
for i in range(len(num)):
    if num[i] > 0:
        positive_num_cnt += 1
        positive_num_sum += num[i]
 
if positive_num_cnt > 0:
    average = positive_num_sum / positive_num_cnt
 
print average
# 输出 5

positive_num = filter(lambda x: x>0, num)
average = reduce(lambda x,y: x+y, positive_num) / len( positive_num )

