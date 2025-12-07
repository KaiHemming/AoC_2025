f = open("Day 07/input","r")
lines = f.readlines()
grid = [list(line.strip()) for line in lines]

def move(tup):
    if grid[tup[1] + 1][tup[0]] == ".":
        return (tup[0], tup[1] + 1), None
    # If not free space, split
    beam1 = (tup[0] + 1, tup[1] + 1)
    beam2 = (tup[0] - 1, tup[1] + 1)

    return beam1, beam2

def insertDict(beam, count, dict):
    if beam in dict.keys():
        dict[beam] += count
    else:
        dict[beam] = count

beams = {}

for x in range(0, len(grid[0]) - 1):
    if grid[0][x] == "S":
        beams[(x,0)] = 1

for y in range(0, len(grid) - 1):
    newBeams = {}
    for beam in beams.keys():
        beam1, beam2 = move(beam)
        if beam2:
            insertDict(beam1, beams[beam], newBeams)
            insertDict(beam2, beams[beam], newBeams)
            continue
        insertDict(beam1, beams[beam], newBeams)
    beams = newBeams

total = 0
for beam in beams.keys():
    total += beams[beam]
print(total)