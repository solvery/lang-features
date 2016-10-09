# encoding: UTF-8

import re

## 一行完成
m = re.match(r'hello', 'hello world!')
print m.group()

#escape(string)，用于将string中的正则表达式元字符如*/+/?等之前加上转义符再返回
