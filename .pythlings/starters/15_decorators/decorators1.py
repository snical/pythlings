# decorators1
# Fix the program so it prints `HELLO ADA`.

# hint: The decorator should make the wrapped result uppercase.
def loud(function):
    def wrapper(name):
        return function(name).lower()
    return wrapper


@loud
def greet(name):
    return "Hello " + name


print(greet("Ada"))
