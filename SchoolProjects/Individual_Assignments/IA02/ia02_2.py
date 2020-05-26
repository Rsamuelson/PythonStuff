import csv

with open('sample.csv', 'r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    somedata = list(reader)

with open('second_row.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(somedata)):
        if i%2 == 1:    
            writer.writerow(somedata[i])
        
