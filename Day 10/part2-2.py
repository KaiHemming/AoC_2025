import z3

# Faster solution using z3

f = open("Day 10/input", "r")
lines = f.readlines()

total = 0
for i, line in enumerate(lines):
    # Parse
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

    # Solve using optimizer
    # Optimizer lets you find the lowest/greatest value
    solver = z3.Optimize()

    # Buttons cannot be pressed negative number of times.
    vars = z3.Ints(f"b{j}" for j in range(len(buttons)))
    for var in vars:
        solver.add(var >= 0)

    # Add constraints for each indicator:
    # Every button that increments that indicator must total to the target value, e.g.,
    # For buttons [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
    # indicator3 = n0 + n1 + n3
    for i, indicator in enumerate(indicators):
        equation = 0
        for j, button in enumerate(buttons):
            if i in button:
                equation += vars[j]
        solver.add(equation == indicator)

    # Optimize for the lowest sum of buttons pressed
    solver.minimize(sum(vars))
    solver.check()

    subTotal = solver.model().eval(sum(vars)).as_long()
    total += subTotal
    print(indicators, buttons, subTotal, total)

print(total)