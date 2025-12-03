f = open("Day 03/input","r")
lines = f.readlines()

total = 0
for line in lines:
    line = line.strip()
    battery1 = int(line[0])
    battery2 = int(line[1])
    curNum = int(str(battery1) + str(battery2))
    # print(battery1, battery2)

    for i in range(2, len(line)):
        numString = line[i]
        num = int(numString)

        # Check for swap
        if num * 10 > curNum and num * 10 < int(str(battery2)+str(num)):
            battery1 = battery2
            battery2 = num
            curNum = int(str(battery1) + str(battery2))
            # print(battery1, battery2)
        elif i < len(line) - 1 and int(numString + str(battery2)) > curNum:
            battery1 = num
            battery2 = 0
            curNum = int(str(battery1) + str(battery2))
            # print(battery1, battery2)
        elif int(str(battery1) + numString) > curNum:
            battery2 = num
            curNum = int(str(battery1) + str(battery2))
            # print(battery1, battery2)
    
    total += curNum
    print(line, curNum, total)

print(total)
