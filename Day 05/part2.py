f = open("Day 05/input","r")
lines = f.readlines()

# Insert ranges in asc order
ranges = []
for rs in lines:
    rs = rs.strip()
    ints = rs.split("-")
    if len(ints) != 2:
        break
    ints = (int(ints[0]), int(ints[1]))

    for i in range(0, len(ranges)):
        if ranges[i][0] > int(ints[0]):
            ranges.insert(i, (int(ints[0]),int(ints[1])))
            break
    else:
        ranges.append((int(ints[0]),int(ints[1])))

reduced = []
for range in ranges:
    if len(reduced) == 0:
        reduced.append(range)
        continue
    # print("Processing", range, "and last reduced is", reduced[-1])

    # Skip duplicates
    if range == reduced[-1]:
        # print("Skipping duplicate", range)
        continue

    # Merge
    if range[0] <= reduced[-1][1] and range[1] >= reduced[-1][0]:
        # print("Merging", range, "with", reduced[-1])
        # Merge
        newRange = (min(range[0], reduced[-1][0]), max(range[1], reduced[-1][1]))
        reduced[-1] = newRange
    else:
        reduced.append(range)

# print(reduced)

total = 0
for range in reduced:
    total += range[1] - range[0] + 1

print(total)