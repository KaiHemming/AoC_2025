f = open("AoC_2025/Day 06/input","r")
lines = f.readlines()

operators = []
nums = []
totals = [] * len(operators)

for x in range(0, len(lines[-1]) - 1):
    if lines[-1][x] == " ":
        continue
    operators.append((lines[-1][x], x))

for i in range(0, len(operators)):
    if operators[i][0] == '*':
        totals.append(1)
    else:
        totals.append(0)

longestLineLength = 0
for line in lines:
    if len(line) > longestLineLength:
        longestLineLength = len(line)
        
for x in range(longestLineLength, -1, -1):
    number = ""
    for y in range(0, len(lines) - 1):
        if len(lines[y]) <= x: 
            continue
        number += lines[y][x]
    
    number = number.strip()
    if not number:
        continue
    number = int(number)

    for i in range(0, len(operators)-1):
        if operators[i+1][1] > x:
            if operators[i][0] == "+":
                totals[i] += number
                break
            elif operators[i][0] == "*":
                totals[i] = totals[i] * number
                break
    else:
        i += 1
        if operators[i][0] == "+":
            totals[i] += number
        elif operators[i][0] == "*":
            totals[i] = totals[i] * number

    # print(totals, number)
    
total = 0
for subtotal in totals:
    total += subtotal
print(total)
