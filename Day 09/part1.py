from collections import deque

f = open("Day 09/input","r")
lines = f.readlines()

coords = deque()
for line in lines:
    stringX, stringY = line.split(",")
    x = int(stringX)
    y = int(stringY)
    coords.append((x,y))

highestArea = 0
bestCoords = []
for i in range(0, len(coords)):
    for j in range(i + 1, len(coords)):
        x, y = coords[i]
        x1, y1 = coords[j]
        area = (abs(x1 - x) + 1) * (abs(y1 - y) + 1)
        if area > highestArea:
            bestCoords = [(x,y),(x1,y1)]
            highestArea = area

print(bestCoords)
print(highestArea)