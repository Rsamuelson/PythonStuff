import csv
import operator
from collections import Counter

fileName = input('what is the name of the file: ')
#fileName = '../../Iowa-Liquor-Sales-2018.csv'

#dictionary for columns
columnDictionary = {"INVOICE_NUM" : 0, "DATE" : 1, "STORE_NUM" : 2, "STORE_NAME" : 3, "CITY" : 5, "COUNTY_NUM" : 8, "COUNTY_NAME" : 9, "VENDOR_NUM" : 12, "VENDOR_NAME" : 13, "ITEM_NUM" : 14, "ITEM_NAME" : 15, "BOTTLE_SIZE" : 17, "SALE" : 21, "VOLUME_LITERS" : 22, "VOLUME_GALS" : 23}
countyDictionary = {}

#create reader
with open(fileName, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #filter by county
        if row[columnDictionary.get('COUNTY_NAME')] == 'STORY':

            storeName = row[columnDictionary.get('STORE_NAME')]
            rowVolumeLiters = float(row[columnDictionary.get('VOLUME_LITERS')])
            itemName = row[columnDictionary.get('ITEM_NAME')]
            #add store to countyDictionary if not there
            if storeName not in countyDictionary:
                countyDictionary[storeName] = {}

            #add item to storeDictionary if not there
            if itemName not in countyDictionary[storeName]:
                countyDictionary[storeName][itemName] = 0.0
            
            #add liters to item
            countyDictionary[storeName][itemName] += rowVolumeLiters

#make orderd list from dictionary https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
orderedListOfStores = sorted(countyDictionary.items(), key=lambda kv: kv[0])

print("Most popular product by volume in each store in STORY county:")
index = 0
for store in orderedListOfStores:
    item = sorted(store[1].items(), key=lambda kv: kv[1], reverse=True)[0]
    index += 1
    print("{:3d}. {:40s} {:30s} {:10.2f}".format(index, store[0], item[0], item[1]))
