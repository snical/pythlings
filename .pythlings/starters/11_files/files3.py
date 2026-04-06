# files3
# Fix the program so it prints `True`.

# hint: Create the file before checking it.
from pathlib import Path

path = Path("note3.txt")
path.write("ready", encoding="utf-8")
print(path.exists())
