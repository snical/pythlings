# exceptions3
# Fix the program so it prints `bad number`.

# hint: `int("hi")` raises `ValueError`.
text = "hi"
try:
    print(int(text))
except TypeError:
    print("bad number")
