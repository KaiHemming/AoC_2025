from functools import cache

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False
    
    def print(self):
        childValues = []
        for child in self.children:
            childValues.append(child.value)
        print(self.value, ":", childValues)
    
def parse(dir):
    # Read connections
    f = open(dir, "r")
    lines = f.readlines()
    connections = {}
    seen = set()

    global nodes
    nodes = {}

    connections["out"] = []

    for line in lines:
        tokens = line.split()
        value = tokens[0][:-1]
        connections[value] = tokens[1:]

    def buildNode(value):
        if value in seen:
            return nodes[value]
        
        seen.add(value)
        children = []
        if len(connections[value]) > 0:
            childrenString = connections[value]
            while len(childrenString) < 2 and childrenString[0] not in ["out", "dac", "fft"]:
                childrenString = connections[childrenString[0]]
            for childString in childrenString:
                children.append(buildNode(childString))

        node = Node(value, children)
        nodes[node.value] = node
        
        if node.value == "svr":
            global startingNode
            startingNode = node

        return node

    for connection in connections:
        buildNode(connection)
        
    return startingNode

@cache
def dfs(nodeValue, foundDAC, foundFFT):
    # print(nodeValue)
    match nodeValue:
        case "out":
            if foundDAC and foundFFT:
                # print("FOUND END")
                return 1
            # print("END")
            return 0
        case "dac":
            foundDAC = True
        case "fft":
            foundFFT = True

    paths = 0

    node = nodes[nodeValue]
    for child in node.children:
        if child.value not in seen:
            paths += dfs(child.value, foundDAC, foundFFT)
    return paths

print("Parsing...")
startingNode = parse("Day 11/input")

startingNode.print()
print("...")

seen = set()
paths = dfs(startingNode.value, False, False)

print("Paths found", paths)
