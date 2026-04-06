# files4
# Fix the program so it prints `ABC`.

# hint: Change the file text to uppercase.
from pathlib import Path

path = Path("note4.txt")
path.write_text("abc", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
