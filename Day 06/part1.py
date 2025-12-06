f = open("AoC_2025/Day 06/input","r")
lines = f.readlines()

operators = lines[-1].split()
totals = []

for i in range(0, len(operators)):
    if operators[i] == '*':
        totals.append(1)
    else:
        totals.append(0)

for i in range(0, len(lines)-1):
    nums = lines[i].split()
    # print(nums)
    for j in range (0, len(nums)):
        if operators[j] == '+':
            totals[j] += int(nums[j])
        elif operators[j] == '*':
            totals[j] = int(nums[j]) * totals[j]
        # print(j, nums[j], operators[j], totals[j])

print(totals)
total = 0
for subtotal in totals:
    total += subtotal

print(total)