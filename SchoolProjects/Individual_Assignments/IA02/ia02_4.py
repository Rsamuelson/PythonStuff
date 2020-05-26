import csv

with open('sample.csv', 'r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    somedata = list(reader)
MNcounter = 0
MOcounter = 0

for i in range(len(somedata)):
    if somedata[i][6] == 'MN':
        MNcounter += 1
    elif somedata[i][6] == 'MO':
        MOcounter += 1

print('MN: total = {}'.format(MNcounter))
print('MO: total = {}'.format(MOcounter))