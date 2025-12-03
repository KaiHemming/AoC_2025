import math

f = open("Day 03/input","r")
lines = f.readlines()

total = 0
numBatteries = 12

# Monotonic Stack - Store values greater than the current value.
# Make sure that at all times there are enough values left to fill batteries.
for line in lines:
    stack = []
    line = line.strip()
    if len(line) < numBatteries:
        continue
    for i in range(0, len(line)):
        num = int(line[i])
        # print(num)
        while len(stack) > 0 and stack[len(stack)-1] < num and len(line) - i + len(stack) > numBatteries:
            stack.pop()
            # print("popped")
        if len(stack) < numBatteries:
            stack.append(num)
            # print("pushed")

    subTot = 0
    for i in range(0,len(stack)):
        subTot += stack[i] * math.pow(10, numBatteries-i-1)
    total += subTot
    print(line, stack, len(stack), subTot, total)

print(total)
