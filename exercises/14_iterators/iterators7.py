# iterators7
# Fix the program so it prints `{'Ada': 11, 'Lin': 11}`.

# hint: Add each bonus to its matching score before building the report.
names = ["Ada", "Mina", "Lin"]
scores = [10, 8, 9]
bonuses = [1, 0, 2]

totals = map(lambda pair: pair[1] - pair[2], zip(names, scores, bonuses))
report = {name: total for name, total in zip(names, totals) if total > 9}
print(report)
