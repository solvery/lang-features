#!/usr/local/bin/io

# 散列表的结构和Io对象很像——散列表的键就是一个个绑定了值的槽

a := Map clone
a atPut("1", "a1")
a at("1") println
a atPut("2","a2")
a asObject println
a asList println
a keys println
a size println
