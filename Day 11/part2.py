from copy import deepcopy

# Way too slow.
# Removed deep copy, storing paths, and added caching in part2-2

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
        childrenString = connections[value]
        children = []
        for childString in childrenString:
            children.append(buildNode(childString))

        node = Node(value, children)
        nodes[node.value] = node
        
        if node.value == "svr":
            global startingNode
            startingNode = node
        elif node.value == "fft":
            global fft
            fft = node
        elif node.value == "dac":
            global dac
            dac = node

        return node

    for connection in connections:
        buildNode(connection)
        
    return startingNode, fft, dac

def dfs(node, path, target):
    if node.value not in seen:
        seen.add(node.value)
    if node.value == target and "dac" in seen and "fft" in seen:
        paths.append(deepcopy(path))
    for child in node.children:
        if child.value not in seen:
            path.add(child.value)
            dfs(child, path, target)
            path.remove(child.value)
            seen.remove(child.value)

print("Parsing...")
startingNode, fft, dac = parse("Day 11/testinput2")

# FFT to server
print("svr to out")
startingNode.print()
print("...")

seen = set()
paths = []
dfs(startingNode, set(), "out")

print("Paths found", paths)
print("Num Paths", len(paths))
