inputstring = ""
rotorLength = 26
#where is the rotor do we start
rotor1StartingPostion = 24
rotor2StartingPostion = 24
rotor3StartingPostion = 25


alphabetDictonary = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o','16': 'p','17': 'q','18': 'r','19': 's','20': 't','21': 'u','22': 'v','23': 'w','24': 'x','25': 'y','26': 'z'}



#generates a rotorkey values; 1 - n
def GenerateRotorKey():
    rotorkey = []
    for i in range(1, rotorLength + 1):
        rotorkey.append(i)
    return rotorkey

#only for testing
def GenerateRotorOutput():
    rotorkey = []
    for i in range(1, rotorLength + 1):
        rotorkey.append((rotorLength + 1) - i)
    return rotorkey    

#moves the rotor one value pushes the first value to the last spot and then moves everyting else up one space
def RotateRotor(rotor):

    #store first value
    firstValue = rotor[0]
    # print(firstValue) 

    #move all values up one spot
    for i in range(len(rotor)):
        # print(i)
        if i == len(rotor) - 1:
            rotor[i] = firstValue
        else:
            rotor[i] = rotor[i + 1]
    return rotor

#call the rotateRotor method for the rotors if they need to rotate
def TakeRotorStep():
    RotateRotor(rotor1Key)
    RotateRotor(rotor1Output)
    if rotor1Key[0] == 1:
        RotateRotor(rotor2Key)
        RotateRotor(rotor2Output)
        if rotor2Key[0] == 1:
            RotateRotor(rotor3Key)
            RotateRotor(rotor3Output)





rotor1Key = GenerateRotorKey()
rotor1Output = GenerateRotorOutput()
rotor2Key = GenerateRotorKey()
rotor2Output = GenerateRotorOutput()
rotor3Key = GenerateRotorKey()
rotor3Output = GenerateRotorOutput()
print(rotor1Key)
print(rotor2Key)
print(rotor3Key)
print()
for i in range(rotor1StartingPostion):
    RotateRotor(rotor1Key)
for i in range(rotor2StartingPostion):
    RotateRotor(rotor2Key)
for i in range(rotor3StartingPostion):
    RotateRotor(rotor3Key)
print(rotor1Key)
print(rotor2Key)
print(rotor3Key)
print()
TakeRotorStep()
print(rotor1Key)
print(rotor2Key)
print(rotor3Key)
print()
TakeRotorStep()
print(rotor1Key)
print(rotor2Key)
print(rotor3Key)


rotor1Key = RotateRotor(rotor1Key)