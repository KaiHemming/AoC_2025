f = open("Day 05/input","r")
lines = f.readlines()

# Insert ranges in asc order
ranges = []
curLine = 0
for rs in lines:
    # print("Processing", rs, curLine)
    curLine += 1
    rs = rs.strip()
    ints = rs.split("-")

    if len(ints) != 2:
        curLine += 1
        break

    for i in range(0, len(ranges)):
        if ranges[i][0] > int(ints[0]):
            ranges.insert(i, (int(ints[0]),int(ints[1])))
            break
    else:
        ranges.append((int(ints[0]),int(ints[1])))

print(ranges)

total = 0
for j in range(curLine, len(lines)):
    num = int(lines[j].strip())
    for r in ranges:
        # print("Checking", num, "against", r)
        if num >= r[0] and num <= r[1]:
            print("Found", num)
            total += 1
            break

print(total)