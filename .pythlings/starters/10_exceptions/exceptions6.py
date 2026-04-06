# exceptions6
# Fix the program so it prints `cannot divide`.

# hint: Catch the error that happens when the second number is 0.
def safe_divide(a, b):
    try:
        return a / b
    except ValueError:
        return "cannot divide"

print(safe_divide(8, 0))
