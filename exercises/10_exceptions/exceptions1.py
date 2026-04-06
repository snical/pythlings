# exceptions1
# Fix the program so it prints `cannot divide by zero`.

# hint: Catch `ZeroDivisionError`.
try:
    print(5 / 0)
except TypeError:
    print("cannot divide by zero")
