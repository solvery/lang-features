#encoding=utf-8

# 用逗号分割模块名称就可以同时导入多个模块
# import socket, os, regex模块导入时可以使用 as 关键字来改变模块的引用对象名字
# 使用from语句可以将模块中的对象直接导入到当前的名字空间
# import 语句可以在程序的任何位置使用
# sys.modules字典中保存着所有被导入模块的模块名到模块对象的映射
# 每个模块都拥有 __name__ 属性
# 最顶层的模块名称是 __main__ 

# 检查是单独执行还是被导入
if __name__ == '__main__':
      # Yes
      statements
else:
      # No (可能被作为模块导入)
      statements 

# 导入模块时,解释器会搜索sys.path列表

