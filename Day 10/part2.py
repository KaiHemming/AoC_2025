from collections import deque

# Too slow to run on full input, had to implement a integer programming solution with z3

f = open("Day 10/testinput", "r")
lines = f.readlines()

allIndicators = deque()
allButtons = {}

# Parse
for i, line in enumerate(lines):
    tokens = line.split()

    indicatorsString = tokens[-1]
    indicators = indicatorsString[1:-1].split(",")
    for j in range(0, len(indicators)):
        indicators[j] = int(indicators[j])

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
    newIndicators = indicators[:]
    for i in range(0, len(button)):
        num = button[i]
        newIndicators[num] += 1
    return newIndicators

def bfs(goal, indicators, buttons):
    queue = deque()
    seen = set()
    presses = {tuple(indicators):0}

    orderedButtons = sorted(buttons, key = lambda b: -len(b)) # Heuristic press buttons that increase most first
    queue.append(indicators)


    while queue:
        next = queue.popleft()

        for i in range(0, len(orderedButtons)):
            curIndicator = next
            newIndicators = toggle(curIndicator, orderedButtons[i])
            tupNewIndicators = tuple(newIndicators)
            tupCurIndicators = tuple(curIndicator)

            if newIndicators == goal:
                return presses[tupCurIndicators] + 1

            tupNewIndicators = tuple(newIndicators)
            if tupNewIndicators in seen:
                continue

            skip = False
            for j in range(0, len(newIndicators)):
                if newIndicators[j] > goal[j]:
                    skip = True
                    break
            if skip:
                continue

            presses[tupNewIndicators] = presses[tupCurIndicators]+1            
            seen.add(tupNewIndicators)
            queue.append(newIndicators)
    return None

numButtonsPushed = 0
for i in range(0, len(allIndicators)):
    start = [0] * len(allIndicators[i])

    presses = bfs(allIndicators[i], start, allButtons[i])
    if presses:
        numButtonsPushed += presses
        print("Solved!", allIndicators[i], allButtons[i], presses, numButtonsPushed)
    else:
        print("Error: Could not find solution!", allIndicators[i], allButtons[i])
        break
print("Buttons pushed", numButtonsPushed)
