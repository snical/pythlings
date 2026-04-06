# iterators3
# Fix the program so it prints `['bb', 'ccc']`.

# hint: Keep the words whose length is greater than 1.
words = ["a", "bb", "ccc"]
result = list(filter(lambda word: len(word) > 1, words))
print(result)

