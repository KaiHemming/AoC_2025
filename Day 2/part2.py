import sys


f = open("Day 2/input","r")
line = f.readline().strip()

rangesString = line.split(",")

# Insert ranges in asc order
ranges = []
for rs in rangesString:
    ints = rs.split("-")
    for i in range(0, len(ranges)):
        if ranges[i][0] > int(ints[0]):
            ranges.insert(i, (int(ints[0]),int(ints[1])))
            break
    else:
        ranges.append((int(ints[0]),int(ints[1])))

# print(ranges)

# Build all doubles

def duplicate(curNumber, ranges, curRangeIndex, n, seen) -> int:
    curNumberDuplicated = int(str(curNumber) * n)
    subtotal = 0
    if curNumberDuplicated in seen:
        return subtotal
    seen.add(curNumberDuplicated)

    while curRangeIndex < len(ranges) and ranges[curRangeIndex][1] < curNumberDuplicated:
        curRangeIndex += 1

    if curRangeIndex >= len(ranges):
        return subtotal

    if (curNumberDuplicated <= ranges[len(ranges)-1][1]):
        subtotal += duplicate(curNumber, ranges, curRangeIndex, n+1, seen)
    
    if ranges[curRangeIndex][0] <= curNumberDuplicated <= ranges[curRangeIndex][1]:
        return subtotal + curNumberDuplicated

    return subtotal

curNumber = 1
curRangeIndex = 0
total = 0
curNumberDoubled = 11
seen = set() # Keeps track of seen duplicates, this could probably be faster.
while curNumberDoubled <= ranges[len(ranges)-1][1]:
    total += duplicate(curNumber, ranges, curRangeIndex, 2, seen)
    curNumber += 1
    curNumberDoubled = int(str(curNumber) * 2)

print(total)