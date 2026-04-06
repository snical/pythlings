# exceptions7
# Fix the program so it prints `missing`.

# hint: `ValueError("missing")` needs to be raised.
def require_name(name):
    if name == "":
        raise ValueError("missing")
    return name

try:
    require_name("")
except ValueError as error:
    print(error)
