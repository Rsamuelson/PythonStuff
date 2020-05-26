import csv

with open('sample.csv', 'r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    somedata = list(reader)

with open('selected_cols.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(somedata)):
        writer.writerow([somedata[i][0],somedata[i][1],somedata[i][-1]])