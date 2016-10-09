
import csv

#read csv type file.
file_in = 'csv_file.1.in'
with open(file_in,'rb') as f:
    csv_contents = csv.reader(f)
    for row in csv_contents:
        print row[3]

