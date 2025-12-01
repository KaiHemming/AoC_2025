import math
f = open("Day 1/input","r")
lines = f.readlines()

dial = 50
num0s = 0

for line in lines:
    char, num = line[0:1],int(line[1:])

    if char == "L":
        started = dial # If started on 0, don't count on first loop.
        dial -= num

        if dial < 0:
            num0s += abs(math.floor(dial/100))
            dial = dial % 100
            if started == 0:
                num0s -= 1

        if dial == 0: # Count if ended on 0
            num0s += 1

    if char == "R":
        dial += num
        if dial > 99:
            num0s += abs(math.floor(dial/100))
            dial = dial % 100

print(num0s)
