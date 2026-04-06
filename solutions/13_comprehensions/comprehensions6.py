# comprehensions6
# Fix the program so it prints `{'a': [1, 3], 'b': [2, 4]}`.

# hint: For each letter, collect the values whose key matches that letter.
records = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
grouped = {
    letter: [value for key, value in records if key == letter]
    for letter in ["a", "b"]
}
print(grouped)
