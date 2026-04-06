def read_number(text):
    try:
        return int(text)
    except ValueError:
        return "safe"

print(read_number("oops"))
