import heapq

f = open("Day 08/input","r")
lines = f.readlines()

coords = []
coordsToCircuit = {}
circuitsToCoords = {}
joins = 1000
nLargest = 3

for i in range(0,len(lines)):
    coordsString = lines[i].strip().split(",")
    coord = (int(coordsString[0]), int(coordsString[1]), int(coordsString[2]))
    coords.append(coord)
    coordsToCircuit[coord] = i + 1
    circuitsToCoords[i+1] = [coord]

# print(coords)
# print(coordsToCircuit)

# Returns closest coordinates indexes in list
def getClosestIndexes(coordList):
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

heap = getClosestIndexes(coords)
# print(heap)

for _ in range(0, joins):
    curNode = heapq.heappop(heap)
    # print(coords[curNode[1][0]], coords[curNode[1][1]])
    circuit1 = coordsToCircuit[coords[curNode[1][0]]]
    circuit2 = coordsToCircuit[coords[curNode[1][1]]]
    if coordsToCircuit[coords[curNode[1][1]]] != coordsToCircuit[coords[curNode[1][0]]]:
        coordsToChange = circuitsToCoords[circuit2][:]
        for coord in coordsToChange:
            coordsToCircuit[coord] = circuit1
            circuitsToCoords[circuit1].append(coord)
            circuitsToCoords[circuit2].remove(coord)
        circuitsToCoords.pop(circuit2)
        print("Joined", coordsToChange, "to", circuit1, circuitsToCoords[circuit1])

# print(circuitsToCoords)

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

total = 1
for num in largest:
    total *= num
print(total)
