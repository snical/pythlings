# files1
# Fix the program so it prints `Hello file`.

# hint: Read the file after writing it.
from pathlib import Path

path = Path("note1.txt")
path.write_text("Hello file", encoding="utf-8")
print(path.name)
