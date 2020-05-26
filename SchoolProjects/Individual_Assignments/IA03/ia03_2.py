import csv
import operator
from collections import Counter

fileName = input('what is the name of the file: ')
#fileName = '../../Iowa-Liquor-Sales-2018.csv'

#dictionary for columns
columnDictionary = {"INVOICE_NUM" : 0, "DATE" : 1, "STORE_NUM" : 2, "STORE_NAME" : 3, "CITY" : 5, "COUNTY_NUM" : 8, "COUNTY_NAME" : 9, "VENDOR_NUM" : 12, "VENDOR_NAME" : 13, "ITEM_NUM" : 14, "ITEM_NAME" : 15, "BOTTLE_SIZE" : 17, "SALE" : 21, "VOLUME_LITERS" : 22, "VOLUME_GALS" : 23}
storeDictionary = {}

#create reader
with open(fileName, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #filter by county
        if row[columnDictionary.get('COUNTY_NAME')] == 'STORY':
            #add store to storeDictionary
            storeName = row[columnDictionary.get('STORE_NAME')]
            rowVolumeLiters = float(row[columnDictionary.get('VOLUME_LITERS')])
            
            if storeName not in storeDictionary:
                storeDictionary[storeName] = 0.0

            storeDictionary[storeName] += rowVolumeLiters


top_values = Counter(storeDictionary).most_common(5)
print("Top 5 stores in STORY county alcohol sales by volume:")
index = 0
for item in top_values:
    index += 1
    print("{:3d}. {:40s} {:10.2f}".format(index, item[0], item[1]))