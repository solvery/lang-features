
import re

file_in=open("file_read_line.1.txt",'rb')    
for line in file_in.readlines(): 
	line_split = re.split(',', line)
	print line_split
