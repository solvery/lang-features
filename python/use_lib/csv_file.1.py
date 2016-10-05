
file_in = 'csv_file.1.in'

import csv

with open('egg.csv','rb') as f:
reader = csv.reader(f)
	for row in reader:
	print row
