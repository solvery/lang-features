# encoding: UTF-8
import re

str1 = 'hello world! hello'
 
# 将正则表达式编译成Pattern对象, 工厂方法
pattern = re.compile(r'hello')
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match(str1)
 
if match:
    # 使用Match获得分组信息
    print match.group()
 
# 一行完成
m = re.match(r'hello', 'hello world!')
print m.group()
