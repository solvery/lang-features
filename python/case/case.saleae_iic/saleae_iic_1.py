
import csv

#read csv type file.
file_in = '1.txt'
with open(file_in,'rb') as f:
    csv_contents = csv.reader(f)
    for row in csv_contents:
        print row[0]
