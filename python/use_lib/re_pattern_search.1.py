# encoding: UTF-8 
import re 
 
# 将正则表达式编译成Pattern对象 
pattern = re.compile(r'world') 
 
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None 
# 这个例子中使用match()无法成功匹配  star
match1 = pattern.search('hello world!') 
match2 = pattern.match ('hello world!') 
 
if match1 : 
    print match1.group() 
if match2 : 
    print match2.group() 

