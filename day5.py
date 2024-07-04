import math

seeds = []
with open("input day5", 'r') as file:
    for row in file:
        seeds.append(row)

ids = []
maxID = 0
for i in range(len(seeds)):
    row = [0, 127]
    for c in seeds[i][:7]:
        if c == 'F':
            row[1] -= math.ceil((row[1]-row[0])/2)
        elif c == 'B':
            row[0] += math.ceil((row[1]-row[0])/2)

    column = [0, 7]
    for c in seeds[i][7:]:
        if c == 'L':
            column[1] -= math.ceil((column[1]-column[0])/2)
        elif c == 'R':
            column[0] += math.ceil((column[1]-column[0])/2)
    
    id = row[0] * 8 + column[0]
    if id > maxID:
        maxID = id
    ids.append(id)
print("Max ID:", maxID)

#Part 2

for i in range(maxID):
    if i not in ids and (i-1) in ids and (i+1) in ids:
        print("Own seatID:", i)

