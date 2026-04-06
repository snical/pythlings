# comprehensions5
# Fix the program so it prints `[(0, 'ant'), (2, 'cat')]`.

# hint: Keep the words at even indexes.
words = ["ant", "bee", "cat"]
indexed = [(index, word) for index, word in enumerate(words) if index % 2 == 1]
print(indexed)
