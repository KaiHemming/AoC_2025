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
        
        if node.value == "you":
            global startingNode
            startingNode = node

        return node

    for connection in connections:
        buildNode(connection)
        
    return startingNode

def dfs(node, path):
    if node.value not in seen:
        seen.add(node.value)
    if node.value == "out":
        paths.append(path[:])
    for child in node.children:
        if child.value not in seen:
            path.append(child.value)
            dfs(child, path)
            path.pop(-1)
            seen.remove(child.value)

print("Parsing...")
startingNode = parse("Day 11/input")
print("Starting from")
startingNode.print()
print("...")
seen = set()
paths = []
dfs(startingNode, [])
print("Paths found", paths)
print("Num Paths", len(paths))
