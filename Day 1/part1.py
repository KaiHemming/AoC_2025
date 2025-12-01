f = open("Day 1/input","r")
lines = f.readlines()

dial = 50
num0s = 0

for line in lines:
    char, num = line[0:1],int(line[1:])
    if char == "L":
        dial -= num
        if dial < 0:
            dial = dial % 100
    if char == "R":
        dial += num
        if dial > 99:
            dial = dial % 100
    if dial == 0:
        num0s += 1

print(num0s)
