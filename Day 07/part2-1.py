f = open("Day 07/input","r")
lines = f.readlines()
grid = [list(line.strip()) for line in lines]

# This version is quite slow.
# I should've instead kept track of how many beams are at x,y
# and perform one calculation for all beams at x,y.
# Implemented in part2-2.py

def move(tup):
    if grid[tup[1] + 1][tup[0]] == ".":
        return (tup[0], tup[1] + 1), None
    # If not free space, split
    beam1 = (tup[0] + 1, tup[1] + 1)
    beam2 = (tup[0] - 1, tup[1] + 1)

    return beam1, beam2

beams = []
def printBeams():
    for i in range(0,len(beams)):
        beams[i].print()

for x in range(0, len(grid[0]) - 1):
    if grid[0][x] == "S":
        beams.append((x, 0))

for y in range(0, len(grid) - 1):
    print("y",y,"beams", len(beams))
    newBeams = []
    for i in range(0, len(beams)):
        beam1, beam2 = move(beams[i])
        newBeams.append(beam1)
        if beam2:
            newBeams.append(beam2)
    beams = newBeams
print(len(beams))
