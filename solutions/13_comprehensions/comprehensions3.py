# comprehensions3
# Fix the program so it prints `{'ADA': 3, 'BOB': 5}`.

# hint: The name should be the key, and the score should be the value.
pairs = [("ada", 3), ("bob", 5)]
scores = {name.upper(): score for name, score in pairs}
print(scores)
