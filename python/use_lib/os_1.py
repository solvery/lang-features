
import os 

print os.name
print os.getcwd()
print os.listdir('.')

print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
