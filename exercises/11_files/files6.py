# files6
# Fix the program so it prints `3`.

# hint: Split the file text into lines.
from pathlib import Path

path = Path("note6.txt")
path.write_text("red\nblue\ngreen\n", encoding="utf-8")
text = path.read_text(encoding="utf-8")
print(len(text.split(",")))
