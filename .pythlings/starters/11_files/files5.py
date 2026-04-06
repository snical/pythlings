# files5
# Fix the program so it prints `8`.

# hint: Count the letters in the file text.
from pathlib import Path

path = Path("note5.txt")
path.write_text("pythling", encoding="utf-8")
print(len(path.name))
