from pathlib import Path

path = Path("note5.txt")
path.write_text("pythling", encoding="utf-8")
print(len(path.read_text(encoding="utf-8")))
