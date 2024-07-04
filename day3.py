originalArea = []
with open("input day3", 'r') as file:
    for row in file:
        originalArea.append(row.removesuffix("\n"))

area = originalArea
x=0
y=0
treesEncountered=0

while (y+1)!=len(originalArea):
    x+=1
    y+=2

    while x+1 > len(area[y]):
        area[y] += originalArea[y]
    if area[y][x] == '#':
        treesEncountered+=1

print("Trees encountered (part 1):", treesEncountered)

# Part 2

area = originalArea
result = 0
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for slope in slopes:
    x=0
    y=0
    treesEncountered=0

    while (y+1)<=len(originalArea):
        while x+1 > len(area[y]):
            area[y] += originalArea[y]
        if area[y][x] == '#':
            treesEncountered+=1
        
        x+=slope[0]
        y+=slope[1]

    if result==0:
        result = treesEncountered
    else:
        result *= treesEncountered

print("Result part 2:", result)