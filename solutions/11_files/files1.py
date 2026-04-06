from pathlib import Path

path = Path("note1.txt")
path.write_text("Hello file", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
