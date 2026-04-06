# comprehensions4
# Fix the program so it prints `[1, 2, 3, 4]`.

# hint: Take each number out of each row.
grid = [[1, 2], [3, 4]]
flat = [number for row in grid for number in row]
print(flat)
