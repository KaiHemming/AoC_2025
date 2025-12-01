f = open("input","r")
lines = f.readlines()

dial = 50
num0s = 0

for line in lines:
    char, num = line[0:1],int(line[1:])
    if char == "L":
        dial -= num
        while (dial < 0):
            dial = 100 + dial
    if char == "R":
        dial += num
        while (dial > 99):
            dial = dial - 100
    if dial == 0:
        num0s += 1

print(num0s)