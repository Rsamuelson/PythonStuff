import csv

with open('sales.csv', newline='') as csvfile:
    Reader = csv.reader(csvfile)
    fileData = list(Reader)

numberOfSales = 0
LargestSale = 0.00
totalSales = 00

for lineNumber in range(1, len(fileData)):
    numberOfSales += 1

    saleAmount = float(fileData[lineNumber][4])
    if saleAmount > LargestSale:
        LargestSale = saleAmount

    totalSales += float(fileData[lineNumber][4])

    # print("LineNumber = ", lineNumber)
    # print("totalSales = ",totalSales)
    # print()

averageSale = totalSales/numberOfSales
print("Number of sales: {}".format(numberOfSales))
print("Largest sale: {}".format(LargestSale))
print("Average sale: {}".format(averageSale))