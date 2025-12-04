f = open("Day 04/input","r")
lines = f.readlines()

total = 0
maxRolls = 4
aoe = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

for y in range (0, len(lines)):
    for x in range(0, len(lines[y])):
        if lines[y][x] == '@':
            adjacent = 0
            for position in aoe:
                if adjacent > maxRolls:
                    break

                if y + position[0] < 0 or x + position[1] < 0 or y + position[0] >= len(lines) or x + position[1] >= len(lines[y]):
                    continue

                target = lines[y + position[0]][x + position[1]]
                if target == '@' or target == 'x':
                    # print(f"Found adjacent at {x + position[1]},{y + position[0]}")
                    adjacent += 1

            if adjacent < maxRolls:
                total += 1
                # lines[y] = lines[y][:x] + 'x' + lines[y][x+1:]

            # print(f"Processing {x},{y} found {adjacent} adjacent")

# for line in lines:
#     print(line.strip())
print(total)