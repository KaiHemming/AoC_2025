import heapq

f = open("Day 08/input","r")
lines = f.readlines()

coords = []
coordsToCircuit = {}
circuitsToCoords = {}
joins = 1000
nLargest = 3

# Parse
for i in range(0,len(lines)):
    coordsString = lines[i].strip().split(",")
    coord = (int(coordsString[0]), int(coordsString[1]), int(coordsString[2]))
    coords.append(coord)
    coordsToCircuit[coord] = i + 1
    circuitsToCoords[i+1] = [coord]

# Returns closest coordinates in min-heap
def getClosestCoords(coordList):
    distances = []
    combinations = set()

    for l in range(0, len(coordList)):
        coordL = coordList[l]
        for r in range(0, len(coordList)):
            if l == r or (l,r) in combinations or (r,l) in combinations: 
                continue
            coordR = coordList[r]

            # Don't need to sqrt, all distances d^2
            dist = (coordL[0] - coordR[0]) ** 2 + \
                    (coordL[1] - coordR[1]) ** 2 + \
                    (coordL[2] - coordR[2]) ** 2
            
            distances.append((dist,(l,r)))
            combinations.add((l,r))
    heapq.heapify(distances)
    return distances

heap = getClosestCoords(coords)
# print(heap)

# Join circuits joins times
for _ in range(0, joins):
    curNode = heapq.heappop(heap)
    coord1 = coords[curNode[1][0]]
    coord2 = coords[curNode[1][1]]
    
    circuit1 = coordsToCircuit[coord1]
    circuit2 = coordsToCircuit[coord2]

    if coordsToCircuit[coord2] != coordsToCircuit[coord1]:
        coordsToChange = circuitsToCoords[circuit2][:]
        for coord in coordsToChange:
            coordsToCircuit[coord] = circuit1
            circuitsToCoords[circuit1].append(coord)
            circuitsToCoords[circuit2].remove(coord)
        circuitsToCoords.pop(circuit2)
        # print("Joined", coordsToChange, "to", circuit1, circuitsToCoords[circuit1])

# Get 3 largest circuits
largest = [0] * nLargest
for circuit in circuitsToCoords:
    numInCircuit = len(circuitsToCoords[circuit])

    for i in range(0, len(largest)):
        if largest[i] < numInCircuit:
            largest.insert(i, numInCircuit)
            break

    if len(largest) > 3:
        largest.pop()
    
print(largest)

# Mult largest 3 num in circuits
total = 1
for num in largest:
    total *= num
print(total)
