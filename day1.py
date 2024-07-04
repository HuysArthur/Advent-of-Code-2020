array = []
with open("input day1", 'r') as file:
    for row in file:
        array.append(int(row))

for x1 in array:
    for x2 in array:
        if x1 + x2 == 2020:
            print("Part 1:" + str(x1 * x2))
        for x3 in array:
            if x1 + x2 + x3 == 2020:
                print("Part 2:" + str(x1 * x2 * x3))