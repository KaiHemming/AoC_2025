f = open("Day 07/input","r")
lines = f.readlines()

class Beam:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def print(self):
        print("Beam:", self.x, ",", self.y)

    # Returns two new beams if split
    def move(self, lines):
        # print("Next", lines[self.y + 1][self.x])
        if lines[self.y + 1][self.x] == ".":
            return Beam(self.x, self.y + 1), None
        # If not free space, split
        beam1 = Beam(self.x + 1, self.y + 1)
        beam2 = Beam(self.x - 1, self.y + 1)
        # print("In split move")

        return beam1, beam2

beams = set()
def printBeams():
    for beam in beams:
        beam.print()

for x in range(0, len(lines[0]) - 1):
    if lines[0][x] == "S":
        beams.add(Beam(x, 0))

numSplits = 0
uniquePaths = 0
for y in range(0, len(lines) - 1):
    print("y",y)
    toRemove = set()
    toAdd = set()
    for beam in beams:
        toRemove.add(beam)
        beam1, beam2 = beam.move(lines)
        toAdd.add(beam1)
        if beam2:
            uniquePaths += 2
            numSplits += 1
            toAdd.add(beam2)

    # printBeams()
    for removal in toRemove:
        print(f"Removing beam: {removal.x}, {removal.y}") 
        beams.remove(removal)
    for addition in toAdd:
        beams.add(addition)

print("Beams",len(beams))
print("Splits",numSplits)