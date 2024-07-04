#Part 1
arrayMin = []
arrayMax = []
arrayCharacter = []
arrayPassword = []

with open("input day2", 'r') as file:
    for row in file:
        arrayMin.append(int(row[:row.find('-')]))
        arrayMax.append(int(row[row.find('-')+1:row.find(' ')]))
        arrayCharacter.append(row[row.find(' ')+1:row.find(": ")])
        arrayPassword.append(row[row.find(": ")+2:-1])

validPasswords = 0
for i in range(len(arrayPassword)):
    if arrayPassword[i].count(arrayCharacter[i]) >= arrayMin[i] and arrayPassword[i].count(arrayCharacter[i]) <= arrayMax[i]:
        validPasswords+=1
print("Valid passwords (part 1):", validPasswords)

#Part 2

arrayIndex1 = []
arrayIndex2 = []
arrayCharacter = []
arrayPassword = []

with open("input day2", 'r') as file:
    for row in file:
        arrayIndex1.append(int(row[:row.find('-')]))
        arrayIndex2.append(int(row[row.find('-')+1:row.find(' ')]))
        arrayCharacter.append(row[row.find(' ')+1:row.find(": ")])
        arrayPassword.append(row[row.find(": ")+2:-1])

validPasswords = 0
for i in range(len(arrayPassword)):
    password = arrayPassword[i]
    i1 = arrayIndex1[i]
    i2 = arrayIndex2[i]
    if len(password)>=i1 and password[i1-1] == arrayCharacter[i] and len(password)>=i2 and password[i2-1] != arrayCharacter[i]:
        validPasswords += 1
    elif len(password)>=i2 and password[i2-1] == arrayCharacter[i] and len(password)>=i1 and password[i1-1] != arrayCharacter[i]:
        validPasswords += 1
print("Valid passwords (part 2):", validPasswords)