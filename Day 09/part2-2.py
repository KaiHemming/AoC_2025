from collections import deque

f = open("Day 09/input","r")
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
            row.extend(['.'] * (xDiff + 1))
    if len(grid) <= coord[1]:
        yDiff = coord[1] - len(grid)
        for _ in range(0, yDiff+1):
            grid.append(['.'] * len(grid[0]))

def drawLine(coord1, coord2):
    grid[coord1[1]][coord1[0]] = "#"
    grid[coord2[1]][coord2[0]] = "#"
    xDiff = coord1[0] - coord2[0]
    yDiff = coord1[1] - coord2[1]

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

# px, py on AB
def isOnLine(px, py, ax, ay, bx, by):
    cross = (px - ax) * (by - ay) - (py - ay) * (bx - ax)
    if cross != 0:
        return False
    if min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by):
        return True
    return False

def inPolyRaycast(x, y, poly):
    m = len(poly)
    for i in range(m):
        ax, ay = poly[i]
        bx, by = poly[(i + 1) % m]
        if isOnLine(x, y, ax, ay, bx, by):
            return True
        
    # False if crosses even number of edges where x=x and y=y
    inside = False
    for i in range(m):
        ax, ay = poly[i] # curVertex
        bx, by = poly[(i + 1) % m] # nextVertex

        if ((ay > y) != (by > y)): # Intersects at y=y
            # X coord where inf y intersects inf x
            intersectsX = ax + (y - ay) * (bx - ax) / (by - ay)
            if intersectsX > x:
                inside = not inside
    return inside

def fill(lastCoord):
    lx, ly = lastCoord[0], lastCoord[1]

    # Try neighbours of lastCoord
    poly = list(coords)
    candidates = [(lx, ly), (lx, ly-1), (lx, ly+1), \
                  (lx+1, ly), (lx+1, ly-1), (lx+1, ly+1), \
                  (lx-1, ly), (lx-1, ly-1), (lx-1, ly+1)]
    
    start = None
    for x, y in candidates:
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == '.':
            if inPolyRaycast(xSorted[x], ySorted[y], poly):
                start = (x, y)
                print("Found candidate",start ,"for fill...")
                break

    stack = [start]
    while stack:
        x, y = stack.pop()
        if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
            continue
        if grid[y][x] != '.':
            continue
        grid[y][x] = 'X'
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '.':
                stack.append((nx, ny))
            
def printGrid():
    print("Printing Grid")
    for line in grid:
        for ch in line:
            print(ch, end=" ")
        print()

# Build lines and get coords
for line in lines:
    stringX, stringY = line.split(",")
    mx = int(stringX)
    my = int(stringY)
    coords.append((mx,my))

# Compress coordinates and build grid
xSorted = sorted({coord[0] for coord in coords})
ySorted = sorted({coord[1] for coord in coords})

mapX = {x:i for i,x in enumerate(xSorted)}
mapY = {y:i for i,y in enumerate(ySorted)}

expandGrid((len(xSorted) - 1, len(ySorted) - 1))
# printGrid()
print("Built grid, drawing...")

for coord in coords:
    mx = mapX[coord[0]]
    my = mapY[coord[1]]
    if len(curLineBuild) == 0:
        curLineBuild = ((mx, my),(-1, -1))
    else:
        curLineBuild = (curLineBuild[0], (mx,my))
        drawLine(curLineBuild[0], (mx,my))
        areaLines.append(curLineBuild)
        curLineBuild = ((mx,my),(-1,-1))

# Build final line
mappedLast = (mapX[coords[-1][0]], mapY[coords[-1][1]])
mappedFirst = (mapX[coords[0][0]], mapY[coords[0][1]])
areaLines.append((mappedLast, mappedFirst))
drawLine(mappedLast, mappedFirst)
# printGrid()
print("Filling...")

fill([mappedFirst[0], mappedLast[1]])
print("Filled")
# printGrid()

# print(areaLines)
# printGrid()

# Assumed no diagonals
def isInBoundsGrid(coord1, coord2):
    lx, rx = min(coord1[0], coord2[0]), max(coord1[0], coord2[0])
    ty, by = min(coord1[1], coord2[1]), max(coord1[1], coord2[1])

    # Check horizontal edges (top and bottom)
    for x in range(lx, rx + 1):
        if grid[ty][x] not in ("#", "X"):
            return False
        if grid[by][x] not in ("#", "X"):
            return False

    # Check vertical edges (left and right)
    for y in range(ty, by + 1):
        if grid[y][lx] not in ("#", "X"):
            return False
        if grid[y][rx] not in ("#", "X"):
            return False
    return True
    
highestArea = 0
bestCoords = []
for i in range(0, len(coords)):
    for j in range(i + 1, len(coords)):
        x, y = coords[i][0], coords[i][1]
        x1, y1 = coords[j][0], coords[j][1]

        mx, my = mapX[x], mapY[y]
        mx1, my1 = mapX[x1], mapY[y1]
        area = (abs(x1 - x) + 1) * (abs(y1 - y) + 1)
        inBounds = isInBoundsGrid((mx, my), (mx1, my1))

        # print((x, y), (x1, y1), inBounds)
        if inBounds and area > highestArea:
            bestCoords = [(x,y),(x1,y1)]
            bestMCoords = [(mx,my),(mx1, my1)]
            highestArea = area

grid[bestMCoords[0][1]][bestMCoords[0][0]] = "O"
grid[bestMCoords[1][1]][bestMCoords[1][0]] = "O"
# printGrid()
print(bestCoords)
print(highestArea)