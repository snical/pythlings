from pathlib import Path

path = Path("note3.txt")
path.write_text("ready", encoding="utf-8")
print(path.exists())
