from collections import deque

# WAAAAAAAAAAAY too slow

f = open("Day 09/testinput","r")
lines = f.readlines()

coords = deque()
areaLines = deque()
curLineBuild = ()

grid = [[]]

print("Building grid...")

def expandGrid(coord):
    # print("Expanding grid",coord)
    if len(grid[0]) <= coord[0]:
        xDiff = coord[0] - len(grid[0])
        for row in grid:
            row += ['.'] * (xDiff + 1)
    if len(grid) <= coord[1]:
        yDiff = coord[1] - len(grid)
        for _ in range(0, yDiff+1):
            grid.append(['.'] * len(grid[0]))

lastXDiff = 0
lastYDiff = 0
def drawLine(coord1, coord2):
    expandGrid(coord1)
    expandGrid(coord2)
    grid[coord1[1]][coord1[0]] = "#"
    grid[coord2[1]][coord2[0]] = "#"
    xDiff = coord1[0] - coord2[0]
    lastXDiff = xDiff
    yDiff = coord1[1] - coord2[1]
    lastYDiff = yDiff
    curX = coord1[0]
    curY = coord1[1]
    
    for _ in range(abs(xDiff) - 1):
        if xDiff > 0:
            curX -= 1
        else:
            curX += 1
        # print(coord1, coord2, xDiff, curX)
        grid[coord1[1]][curX] = "X"
    
    for _ in range(abs(yDiff) - 1):
        if yDiff > 0:
            curY -= 1
        else:
            curY += 1
        grid[curY][coord1[0]] = "X"
    # printGrid()
def fill(lastCoord):
    if lastXDiff < 0:
        lastCoord[0] += 1
    else:
        lastCoord[0] -= 1
    
    if lastYDiff < 0:
        lastCoord[1] -= 1
    else:
        lastCoord[1] += 1

    def fillNeighbours(coord):
        neighbours = [[-1,-1],[0,-1],[1,-1], \
                    [-1,0],[0,0],[1,0], \
                    [-1,1],[0,1],[1,1]]

        for neighbour in neighbours:
            newCoord = (coord[0] + neighbour[0], coord[1] + neighbour[1])
            if grid[newCoord[1]][newCoord[0]] == ".":
                grid[newCoord[1]][newCoord[0]] = "X"
                fillNeighbours(newCoord)

    fillNeighbours(lastCoord)
            


def printGrid():
    print("Printing Grid")
    for line in grid:
        for ch in line:
            print(ch, end=" ")
        print()

# Build lines and get coords
for line in lines:
    stringX, stringY = line.split(",")
    x = int(stringX)
    y = int(stringY)
    coords.append((x,y))

    if len(curLineBuild) == 0:
        curLineBuild = ((x, y),(-1, -1))
    else:
        curLineBuild = (curLineBuild[0], (x,y))
        drawLine(curLineBuild[0], (x,y))
        areaLines.append(curLineBuild)
        curLineBuild = ((x,y),(-1,-1))

# Build final line
areaLines.append((coords[-1], coords[0]))
drawLine(coords[-1], coords[0])
print("Built grid, filling...")
fill([coords[-1][0], coords[-1][1]])
print("Filled")
# printGrid()

# print(areaLines)
# printGrid()

# Corner must be # or X
def getCorners(coord1, coord2):
    if coord1[0] < coord2[0]:
        lowestX = coord1[0]
        highestX = coord2[0]
    else:
        lowestX = coord2[0]
        highestX = coord1[0]

    if coord1[1] < coord2[1]:
        lowestY = coord1[1]
        highestY = coord2[1]
    else:
        lowestY = coord2[1]
        highestY = coord1[1]

    return [(lowestX, lowestY), (highestX,lowestY), (highestX, highestY), (lowestX, highestY)]
    
# Assumed no diagonals
def isInBounds(coord1, coord2):
    corners = getCorners(coord1, coord2)
    # print(corners)
    left = 0
    for right in range(1, len(corners)):
        xDiff = corners[left][0] - corners[right][0]
        yDiff = corners[left][1] - corners[right][1]
        curX = corners[left][0]
        curY = corners[left][1]
        seenEdge = False
        
        for _ in range(abs(xDiff) + 1):
            val = grid[corners[left][1]][curX]
            if val in ["#","X"]:
                seenEdge = True
            else:
                return False
            if xDiff == 0:
                break
            elif xDiff > 0:
                curX -= 1
            else:
                curX += 1

        for _ in range(abs(yDiff) + 1):
            if val in ["#","X"]:
                seenEdge = True
            else:
                return False
            if yDiff == 0:
                break
            elif yDiff > 0:
                curY -= 1
            else:
                curY += 1
        
        if not seenEdge:
            return False

        left += 1

    return True
    

highestArea = 0
bestCoords = []
for i in range(0, len(coords)):
    for j in range(i + 1, len(coords)):
        x, y = coords[i]
        x1, y1 = coords[j]
        area = (abs(x1 - x) + 1) * (abs(y1 - y) + 1)
        inBounds = isInBounds((x, y), (x1, y1))

        # print((x, y), (x1, y1), inBounds)
        if inBounds and area > highestArea:
            bestCoords = [(x,y),(x1,y1)]
            highestArea = area

print(bestCoords)
grid[bestCoords[0][1]][bestCoords[0][0]] = "O"
grid[bestCoords[1][1]][bestCoords[1][0]] = "O"
printGrid()
print(highestArea)