import csv

with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = list(sampleReader)

for data in sampleData:
    print(data, end= '\n')