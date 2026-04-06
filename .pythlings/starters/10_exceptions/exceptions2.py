# exceptions2
# Fix the program so it prints `missing name`.

# hint: The dictionary does not have the key `name`.
data = {}
try:
    print(data["name"])
except ValueError:
    print("missing name")
