# files7
# Fix the program so it prints `6`.

# hint: Turn each line into a number before adding it.
from pathlib import Path

path = Path("note7.txt")
path.write_text("1\n2\n3\n", encoding="utf-8")
numbers = path.read_text(encoding="utf-8").splitlines()
total = 0

for number in numbers:
    total = total + int(number)

print(total)
