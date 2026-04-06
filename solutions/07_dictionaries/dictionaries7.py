# dictionaries7
# Fix the program so it prints `5`.

# hint: Loop over the dictionary values.
prices = {"apple": 2, "pear": 3}
total = 0

for price in prices.values():
    total = total + price

print(total)
