
file_in = 'csv_file.1.in'

import csv

with open(file_in,'rb') as f:
    #read cvs type file.
    reader = csv.reader(f)
    for row in reader:
        print row[3]
