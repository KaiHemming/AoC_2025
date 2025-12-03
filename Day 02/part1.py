import math

f = open("Day 2/input","r")
line = f.readline().strip()

rangesString = line.split(",")

# Insert ranges
ranges = []
for rs in rangesString:
    ints = rs.split("-")
    ranges.append((int(ints[0]),int(ints[1])))

print(ranges)

# Build doubles in ranges
curNumber = 1
curNumberDoubled = 1
total = 0
for range in ranges:
    # print(range)
    curNumber = range[0]
    curNumberString =  str(curNumber)
    halfLength = math.floor(len(curNumberString)/2) # Checks excessively
    if not halfLength:
        halfLength = 1

    curNumber = int(curNumberString[:halfLength])
    curNumberDoubled = int(str(curNumber)*2)

    while curNumberDoubled <= range[1]:
        if curNumberDoubled >= range[0]:
            total += curNumberDoubled
            # print(curNumberDoubled)

        curNumber += 1
        curNumberDoubled = int(str(curNumber)*2)

print(total)
