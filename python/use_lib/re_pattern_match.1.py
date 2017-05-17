# encoding: UTF-8
# http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

import re

str1 = "swHandleInsertExtender(): PORT=63 EXT=50638331:1"
 
# 将正则表达式编译成Pattern对象, 工厂方法
pattern = re.compile(r'PORT=(\d+) EXT=(\d+)')
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.search(str1)
 
if match:
    # 使用Match获得分组信息
    print match.group(1), 
    print match.group(2)
 

