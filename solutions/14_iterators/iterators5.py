# iterators5
# Fix the program so it prints `['a', 'b', 'c', 'd']`.

# hint: Chain both lists completely.
from itertools import chain

letters = list(chain(["a", "b"], ["c", "d"]))
print(letters)

