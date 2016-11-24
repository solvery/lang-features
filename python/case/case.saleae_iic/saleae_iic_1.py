
import csv

#read csv type file.
file_in = 'untitled.txt'
# file_in = '1.txt'

sample_data_time = 0.0
with open(file_in,'rb') as f:
    csv_contents = csv.reader(f)
    headers = next(csv_contents)   # 去掉第一行
    for row in csv_contents:
        sample_data_time_last = sample_data_time
        sample_data_time = float(row[0])
        if ( sample_data_time - sample_data_time_last) > 0.0002 :
            print
        print row[2], row[3], row[4], row[5]

