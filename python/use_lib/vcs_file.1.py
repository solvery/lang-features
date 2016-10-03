
file_in = 'file_cvs.1.in'

import csv  
def loadCSVfile1():
    list_file = []
    with open(file_in,'rb') as csv_file:  
        all_lines=cvs.reader(csv_file)  
        for one_line in all_lines:  
            list_file.append(one_line)  
    list_file.remove(list_file[0])
    arr_file = array(list_file)
    label = arr_file[:, 0]
    data = arr_file[:, 1:]
    return data, label  
