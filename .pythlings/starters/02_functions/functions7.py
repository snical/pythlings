# functions7
# Fix the program so it prints `Hello, Ada!`.

# hint: Call the `welcome` function with the name.
def welcome(name):
    return "Hello, " + name

def loud_welcome(name):
    return welcome + "!"

print(loud_welcome("Ada"))
