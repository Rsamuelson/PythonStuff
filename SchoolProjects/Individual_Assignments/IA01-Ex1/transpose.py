import sys

key = input("Enter Key (comma-separated list of numbers):")
#key = "3,2,1,0" #test entry

#check to make sure each key value is an int
splitKey = key.split(',')
i = 0
for keyString in splitKey:
    splitKey[i] = int(keyString)
    i = i + 1

#check for missing numbers in splitKey List
#note: I changed the error to show the missing key value, because it solved more potential problems 
#      like key value duplication and missing key values. ex: 0,0,1,2,3 would be a valid key if you only 
#      check to see if each key value exists between "0-N", N being the key list length. but if you check 
#      to see all posible key values are represented in the key, then you don't have these problems. If we use
#      the example above, key value 4 is missing.
for i in range(len(splitKey)):
    if splitKey[i] < 0 or splitKey[i] > (len(splitKey) - 1):
        print("Error: Key value {value} is not a valid key (must be between 0 - {length})".format(value = splitKey[i], length = len(splitKey) - 1))
        sys.exit()
    if i not in splitKey:
        print("Error: key value {} is missing ".format(i))
        sys.exit()

inputString = input("Enter text to encript:")
#inputVar = "32105"  #test entry

#find the amount of periods to add
periodsToAdd = len(splitKey) - len(inputString)%len(splitKey)

#set periodsToAdd to 0 if splitkey is the same length as the inputString
if periodsToAdd == len(splitKey):
    periodsToAdd = 0

#pad end of string with '.'
while periodsToAdd > 0:
    inputVar = inputString + '.'
    periodsToAdd = periodsToAdd - 1

#use key to encript input
keyLength = len(splitKey)
outputString = ""
for i in range(len(inputString)):
    lengthMutliplier = int(i/keyLength)
    keyValue = int(splitKey[i%keyLength])
    inputVarIndex = int(lengthMutliplier * keyLength + keyValue)
    outputString = outputString + inputString[inputVarIndex]

print("Encrypted text:",outputString)