
import csv

# write contents to cvs file.
file_out = 'csv_file.2.out.csv'
with open(file_out,'wb') as f:
    spamwriter = csv.writer(f,dialect='excel')
    spamwriter.writerow(['a', '1', '1', '2', '2'])
    spamwriter.writerow(['b', '3', '3', '6', '4'])
    spamwriter.writerow(['c', '7', '7', '10', '4'])
    spamwriter.writerow(['d', '11','11','11', '1'])
    spamwriter.writerow(['e', '12','12','14', '3'])

