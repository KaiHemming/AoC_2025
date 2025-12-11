from collections import deque
from copy import deepcopy

f = open("Day 10/testinput", "r")
lines = f.readlines()

allIndicators = deque()
allButtons = {}

# Parse
for i, line in enumerate(lines):
    tokens = line.split()

    indicatorsString = tokens[0]
    indicators = list(indicatorsString[1:-1])

    for j in range(0, len(indicators)):
        if indicators[j] == "#":
            indicators[j] = True
        else: 
            indicators[j] = False

    buttonsString = tokens[1:-1]
    buttons = []
    for bs in buttonsString:
        buttons.append(bs[1:-1].split(","))
    for bl in buttons:
        for j in range(0, len(bl)):
            bl[j] = int(bl[j])
    
    allIndicators.append(indicators)
    allButtons[i] = buttons

def printStatus():
    print(allIndicators)
    print(allButtons)

def toggle(indicators, button):
    for i in range(0, len(button)):
        num = button[i]
        indicators[num] = not indicators[num]
    return indicators

def bfs(goal, indicators, buttons):
    queue = deque()
    seen = set()
    best = {}
    for button in buttons:
        queue.append((indicators, {}, button))

    while queue:
        next = queue.popleft()
        newIndicators = next[0][:]
        newPath = deepcopy(next[1])

        if tuple(next[2]) in newPath:
                newPath[tuple(next[2])] += 1
        else:
            newPath[tuple(next[2])] = 1

        toggle(newIndicators, next[2])

        solved = True
        for i in range(0, len(newIndicators)):
            if newIndicators[i] != goal[i]:
                solved = False
        if solved:
            return newPath
        
        # print(newIndicators, newPath)
        
        num = numPushed(newPath)
        if tuple(newIndicators) in seen:
            if num > best[tuple(newIndicators)]:
                continue

        best[tuple(newIndicators)] = num
        seen.add(tuple(newIndicators))

        for i in range(0, len(buttons)):
            queue.append((newIndicators, newPath, buttons[i]))
    return None

def numPushed(dict):
    tot = 0
    for item in dict:
        tot += dict[item]
    return tot

numButtonsPushed = 0
for i in range(0, len(allIndicators)):
    stack = deque()
    seen = set()

    start = [False] * len(allIndicators[i])

    path = bfs(allIndicators[i], [False] * len(allIndicators[i]), allButtons[i])
    if path:
        num = numPushed(path)
        print("Solved!", allIndicators[i], allButtons[i], path, num)
        numButtonsPushed += num
    else:
        print("Error: Could not find solution!", allIndicators[i], allButtons[i], path)
        break
print("Buttons pushed", numButtonsPushed)
