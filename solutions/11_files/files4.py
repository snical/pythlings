from pathlib import Path

path = Path("note4.txt")
path.write_text("abc", encoding="utf-8")
print(path.read_text(encoding="utf-8").upper())
