f = open("input","r")
lines = f.readlines()

dial = 50
num0s = 0

for line in lines:
    char, num = line[0:1],int(line[1:])

    if char == "L":
        started = dial # If started on 0, don't count on first loop.
        dial -= num

        while (dial < 0):
            dial = 100 + dial
            if started != 0:
                num0s += 1
            started = dial

        if dial == 0: # Count if ended on 0
            num0s += 1

    if char == "R":
        dial += num
        while (dial > 99):
            dial = dial - 100
            num0s += 1

print(num0s)