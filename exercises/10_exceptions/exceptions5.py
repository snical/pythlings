# exceptions5
# Fix the program so it prints `safe`.

# hint: Return from the `except` block too.
def read_number(text):
    try:
        return int(text)
    except TypeError:
        print("safe")

read_number("oops")
